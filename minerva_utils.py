# SPDX-License-Identifier: Apache-2.0
# Copyright 2025 Marie Corradi

import requests
import pandas as pd
from datetime import datetime

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
            if all(k in project for k in ['machine', 'projectId', 'mapName', 'license', 'createdAt', 'disease']):
                all_projects_list.append({
                    'machine': project['machine'].get('rootUrl'),
                    'project': project['projectId'],
                    'name': project['mapName'],
                    'license': project['license'],
                    'created': project['createdAt'],
                    'disease': project['disease']
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


    final_df = summarized_df[['machine', 'project', 'name']]
    projects = [{"project": row["project"], "name": row["name"],"machine_url": row["machine"]}for _, row in final_df.iterrows()]

    return projects