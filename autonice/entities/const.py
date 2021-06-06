class IONice:
    """https://linux.die.net/man/1/ionice"""
    scheduling = {
        "none": 0,
        "real-time": 1,
        "best-effort": 2,
        "idle": 3
    }
