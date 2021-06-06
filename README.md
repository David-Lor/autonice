# autonice

Utility for setting nice in running applications based on settings.
Currently only supporting ionice.

**This project is experimental and might have undesirable effects.
Use it under your responsability!**

## Getting started

This utility only needs Python >= 3.6. Running as root may be required for modifying processes running as different users, and changing priorities to certain important levels.

To run autonice, cd to the project and run `python .`

## Config file

At this moment the settings must be provided via a JSON file; see the [example provided](settings.sample.json).
This file must be located within the current working directory and be named "settings.json", but its name and location can be changed by setting the environment variable "AUTONICE_SETTINGS", which refers to the absolute or relative path of the config file.

The complete config file format is the following:

- **processes**: array of processes to change; array of objects with the following format:
    - **name**: partial process name to match. All the processes that contain this name will be processed with the settings of the current Process object.
    - **match_full_name**: if true, match full processes names, including command arguments (default=false)
    - **ionice_class**: if set, change ionice of the matching processes. Must be one of "none", "idle", "best-effort", "real-time". See [ionice manual](https://linux.die.net/man/1/ionice) for more information.
    - **ionice_class_data**: additional arguments for ionice class, usually the process IO priority for certain classes. See [ionice manual](https://linux.die.net/man/1/ionice) for more information.

## TODO

- Add nice support
- Add Docker support (change priorities of processes running within a Docker container)
- Run as a "service", periodically checking processes
- Manage failures when setting ionice on multiple processes in batch fails because one process stops existing (retry with less processes or one by one)
- Add proper logging
