"""Module with functions for finding running processes"""

import re
import subprocess
from typing import List


def find_processes(name: str, full_match: bool, include_children: bool = True) -> List[int]:
    cmd = ["pgrep"]
    if full_match:
        cmd.append("-f")
    cmd.append(name)

    try:
        print("Call", *cmd)
        output = subprocess.check_output(cmd).decode().strip()
    except subprocess.CalledProcessError as error:
        if error.returncode == 1 and not error.output.decode().strip():
            return []
        raise error

    processes_ids = [int(line) for line in output.splitlines() if line]

    if include_children:
        for pid in list(processes_ids):
            processes_ids.extend(find_child_subprocesses(pid))

    return processes_ids


def find_child_subprocesses(parent_process_id: int) -> List[int]:
    cmd = ["pstree", "-p", str(parent_process_id)]
    print("Call", *cmd)
    output = subprocess.check_output(cmd).decode().strip()

    processes_ids: List[int] = list()
    for line in output.splitlines():
        subprocesses_ids = re.findall(r'\(.*?\)', line)
        subprocesses_ids = [int(sp.replace("(", "").replace(")", "")) for sp in subprocesses_ids]
        processes_ids.extend(subprocesses_ids)

    return processes_ids
