# Feature Plan: MINERVA Project Selection

This document outlines the plan to add a feature allowing users to select different MINERVA projects within the Fatty Acid Assistant application.

## Phase 1: Core Logic Modification (`ontox_client.py`)

**Objective:** Enable the `MinervaClient` to list available MINERVA projects and fetch data for a user-selected project.

**File:** `fatty-acid-assistant/ontox_client.py`

**Steps:**

1.  **In the `MinervaClient` class:**
    *   **Add new method `get_available_projects(self) -> List[Dict[str, Any]]`:**
        *   Makes a `GET` request to the `/projects/` endpoint.
        *   Parses the JSON response (expected to be a list of project objects).
        *   Extracts `projectId` and `name` (or defaults name to `projectId`) for each project.
        *   Returns a list of dictionaries: `[{'id': 'project_id', 'name': 'Project Name'}, ...]`.
        *   Example implementation sketch:
            ```python
            def get_available_projects(self) -> List[Dict[str, Any]]:
                log.info("Fetching available projects from: /projects/")
                projects_data = self._call_api("GET", "/projects/")
                formatted_projects = []
                if isinstance(projects_data, list):
                    for project in projects_data:
                        if isinstance(project, dict) and 'projectId' in project:
                            project_name = project.get('name', project['projectId'])
                            formatted_projects.append({'id': project['projectId'], 'name': project_name})
                        else:
                            log.warning(f"Skipping unexpected project item format: {project}")
                else:
                    log.warning(f"Received unexpected data format for projects list: {projects_data}")
                return formatted_projects
            ```
    *   **Modify `get_all_elements` method:**
        *   Change signature to: `def get_all_elements(self, project_id: str) -> List[Dict[str, Any]]:`
        *   Update path construction to use the `project_id` parameter: `elements_path = f"/projects/{project_id}/models/{MAP_ID}/bioEntities/elements/"`.
    *   **Modify `get_all_reactions` method:**
        *   Change signature to: `def get_all_reactions(self, project_id: str) -> List[Dict[str, Any]]:`
        *   Update path construction: `reactions_path = f"/projects/{project_id}/models/{MAP_ID}/bioEntities/reactions/"`.
    *   **Modify `_call_api` method:**
        *   Remove the automatic addition of `params['projectId'] = PROJECT_ID` for `/elements` or `/reactions` paths. This will now be handled by the explicit `project_id` in the path.
            ```diff
            # In _call_api method:
            # if 'projectId' not in path and 'projectId' not in params:
            #      if path.startswith(("/projects/", "/models/", "/bioEntities/")) or "/models/" in path :
            #          pass
            -      elif path.startswith(("/elements", "/reactions")): # REMOVE THIS BLOCK
            -          params['projectId'] = PROJECT_ID
            ```

2.  **Update the `@tool("ontox_map_data_retriever")` function:**
    *   Change signature to accept an optional `project_id`:
        `def ontox_map_data_retriever(question: Optional[str] = None, project_id: Optional[str] = PROJECT_ID) -> Dict[str, Any]:`
        (Uses the global `PROJECT_ID` as a default).
    *   Determine `effective_project_id`: `effective_project_id = project_id if project_id else PROJECT_ID`.
    *   Pass `effective_project_id` to `client.get_all_elements(project_id=effective_project_id)` and `client.get_all_reactions(project_id=effective_project_id)`.

## Phase 2: Workflow Integration (`workflow.py`)

**Objective:** Adapt the LangChain workflow to handle project selection.

**File:** `fatty-acid-assistant/workflow.py`

**Steps:**

1.  **Modify `assistant_chain` (or relevant part of LCEL chain):**
    *   When invoking the `ontox_map_data_retriever` tool, ensure the `project_id` selected by the user (passed from `app.py`) is correctly supplied to the tool.
    *   This might involve modifying how `RunnableParallel` or other LCEL components pass arguments. The `itemgetter` for `api_input` might need to be updated to include `project_id`.

## Phase 3: UI Implementation (`app.py`)

**Objective:** Provide a user interface for selecting MINERVA projects.

**File:** `fatty-acid-assistant/app.py`

**Steps:**

1.  **Fetch and Display Project List:**
    *   On application startup (or when a specific UI element is interacted with), instantiate `MinervaClient`.
    *   Call `client.get_available_projects()` to get the list of projects.
    *   Store this list in `st.session_state` to avoid re-fetching on every interaction.
    *   Use `st.selectbox` (recommended) or `st.radio` in the Streamlit sidebar to display project names and allow user selection. The value of the selectbox should be the `project_id`.
2.  **Pass Selected Project to Workflow:**
    *   When the user submits a question, retrieve the currently selected `project_id` from the UI element (or session state).
    *   Pass this `project_id` to the `assistant_chain.invoke()` call.
3.  **Handle Project Change:**
    *   Decide on behavior when a project is changed:
        *   Option A (Simpler): New project selection applies only to subsequent queries.
        *   Option B (More Complex): Clear current chat history or reload parts of the UI.
        *   Initially, Option A is recommended.
4.  **Error Handling:**
    *   If fetching the project list fails, display an appropriate error message in the UI.

## Phase 4: Testing

**Objective:** Ensure the new feature works correctly and reliably.

**Steps:**

1.  **Unit/Integration Tests (Conceptual):**
    *   Test `MinervaClient.get_available_projects()` against a mock API or live API if safe.
    *   Test `ontox_map_data_retriever` with and without a `project_id` argument.
2.  **End-to-End Testing:**
    *   Verify the project list is fetched and displayed correctly in the Streamlit UI.
    *   Test selecting different projects from the UI.
    *   Confirm that data retrieval and Q&A functionality work correctly for various selected projects.
    *   Test default project behavior (if no project is explicitly selected).
    *   Test error handling (e.g., if project list fetching fails).

## Phase 5: Documentation Update (Memory Bank)

**Objective:** Update all relevant Memory Bank files to reflect the new feature.

**Files:** `memory-bank/*.md`

**Steps:**

1.  **`activeContext.md`**: Document the new feature as a recent change and current focus if work is ongoing.
2.  **`systemPatterns.md`**: Update data flow diagrams and component descriptions to include project selection.
3.  **`techContext.md`**: Mention any new UI components or state management related to project selection.
4.  **`progress.md`**: Update "What Works" and "What's Left to Build" sections.
5.  **`projectbrief.md`**: If this feature significantly alters core requirements or goals, update accordingly.
6.  **`productContext.md`**: Update user journeys if impacted.

This plan provides a structured approach to implementing the project selection feature.
