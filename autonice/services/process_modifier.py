"""Module with functions for modifying nice values of processes"""

import subprocess
from typing import List, Optional


def set_ionice(processes_ids: List[int], scheduling_class: int, scheduling_class_data: Optional[int] = None):
    # TODO Manage failures when bulk set of processes fails because one process stops existing (Retry one by one or smaller batches)
    cmd = ["ionice", "-c", str(scheduling_class)]
    if scheduling_class_data is not None:
        cmd.extend(["-n", str(scheduling_class_data)])
    cmd.extend(["-p", *[str(pid) for pid in processes_ids]])

    print("Call", *cmd)
    subprocess.call(cmd)
