from .services.settings import load_json
from .services.process_finder import find_processes
from .services.process_modifier import set_ionice


def main():
    processes = load_json()
    for process in processes:
        process_pids = find_processes(
            name=process.name,
            full_match=process.match_full_name,
            include_children=True
        )
        if not process_pids:
            print("No running processes with name", process.name)
            continue

        if process.has_ionice:
            set_ionice(
                processes_ids=process_pids,
                scheduling_class=process.ionice_class_cli,
                scheduling_class_data=process.ionice_class_data
            )
