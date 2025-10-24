# SPDX-License-Identifier: Apache-2.0
# Copyright 2025 Marie Corradi

import requests
import pandas as pd
from datetime import datetime
import re

def get_available_projects():
    """
    Retrieves information about public licensed projects from MinervaNet machines.
    """
    base_url = "https://minerva-net.lcsb.uni.lu/api"

    machines_url = f"{base_url}/machines/"
    try:
        resp_machines = requests.get(machines_url)
        resp_machines.raise_for_status()
        machines_data = resp_machines.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching machine data: {e}")
        return pd.DataFrame()

    # Filter for machines with status "OK" and create a DataFrame
    ok_machines = [
        machine for machine in machines_data.get('pageContent', [])
        if machine.get('status') == "OK"
    ]

    all_projects_list = []
    for machine in ok_machines:
        machine_id = machine.get('id')
        machine_root_url = machine.get('rootUrl')
        if machine_id is None or machine_root_url is None:
            continue 
        projects_url = f"{base_url}/machines/{machine_id}/projects/"
        try:
            resp_projects = requests.get(projects_url)
            resp_projects.raise_for_status()
            projects_data = resp_projects.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching projects for machine {machine_id}: {e}")
            continue

        for project in projects_data.get('pageContent', []):
            # Ensure required keys exist before accessing
            if all(k in project for k in ['machine', 'projectId', 'mapName', 'license', 'createdAt', 'disease', 'statusUpdatedAt']):
                all_projects_list.append({
                    'machine': project['machine'].get('rootUrl'),
                    'project': project['projectId'],
                    'name': project['mapName'],
                    'license': project['license'],
                    'created': project['createdAt'],
                    'disease': project['disease'],
                    'updated': project['statusUpdatedAt']
                })

    if not all_projects_list:
        return pd.DataFrame()

    projects_df = pd.DataFrame(all_projects_list)

    projects_df['created'] = pd.to_datetime(projects_df['created'])

    licensed_projects = projects_df[projects_df['license'].str.startswith("Creative", na=False)].copy()

    if licensed_projects.empty:
        return pd.DataFrame()
    licensed_projects_sorted = licensed_projects.sort_values(by='created', ascending=False)

    # Pick the most recent entry
    summarized_df = licensed_projects_sorted.groupby(['machine', 'disease']).agg(
        project=('project', 'first'),
        name=('name', 'first'),
        license=('license', 'first'),
        created=('created', 'first')
    ).reset_index()


    final_df = summarized_df[['machine', 'project']]
    projects = [{"project": row["project"],"machine_url": row["machine"]}for _, row in final_df.iterrows()]
    final_df = summarized_df[['machine', 'project', 'name']]
    projects = [{"project": row["project"], "name": row["name"],"machine_url": row["machine"]}for _, row in final_df.iterrows()]

    return projects

def extract_reaction_ids(text):
    """
    Extract all alphanumeric reaction IDs from text.
    """
    # Match patterns like "Reaction ID(s): ..." or "Reactions ..."
    pattern = re.compile(
        r"(?:Reactions?\s*(?:IDs?|ID)?[:\s]*|RID[:\s]*)"      
        r"([\w\s,;and]+)",                        
        flags=re.IGNORECASE,
    )

    found_ids = []
    for chunk in pattern.findall(text):
        # Alphanumeric ID pattern: letters+numbers+letters (no spaces inside IDs)
        ids = re.findall(r"\b[A-Za-z]*\d+[A-Za-z]*\b", chunk)
        for rid in ids:
            if rid not in found_ids:
                found_ids.append(rid)
    return found_ids

def make_url(base_url, project_id, reactions_list):
    """
    Makes a url to MINERVA map with highlighted reactions
    """
    reactions_string = "%3B".join(map(str, reactions_list))
    return f"{base_url}index.html?id={project_id}&perfectMatch=true&searchValue={reactions_string}"

def append_reaction_links(text, base_url, project_id):
    """
    Appends URLs to any line or sentence that mentions Reaction IDs.
    Works for bullet points, lists, and irregular sentence structures.
    """

    lines = text.splitlines()
    updated_lines = []

    for line in lines:
        # Detect table lines (very simple heuristic)
        if line.strip().startswith('|') and line.strip().endswith('|'):
            # Split cells
            cells = [cell.strip() for cell in line.strip('|').split('|')]
            updated_cells = []
            for cell in cells:
                reactions_list = extract_reaction_ids(cell)
                if reactions_list:
                    url = make_url(base_url, project_id, reactions_list)
                    cell = f"{cell} ([link to MINERVA map]({url}))"
                updated_cells.append(cell)
            updated_line = "| " + " | ".join(updated_cells) + " |"
            updated_lines.append(updated_line)
        else:
            # Normal text: split by sentence endings or newlines
            segments = re.split(r'(?:\n+|(?<=[.!?])\s+)', line.strip())
            updated_segments = []
            for seg in segments:
                if not seg.strip():
                    continue
                reactions_list = extract_reaction_ids(seg)
                if reactions_list:
                    url = make_url(base_url, project_id, reactions_list)
                    seg = f"{seg.strip()} ([link to MINERVA map]({url}))"
                updated_segments.append(seg.strip())
            updated_lines.append(" ".join(updated_segments))

    return "\n".join(updated_lines)
