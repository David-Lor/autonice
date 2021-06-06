from .const import IONice


class Process:
    def __init__(self, **kwargs):
        self.name = kwargs["name"]
        self.match_full_name = kwargs.get("match_full_name", False)

        self.ionice_class = kwargs.get("ionice_class", None)
        if self.has_ionice:
            self.ionice_class_cli = IONice.scheduling[self.ionice_class]
            self.ionice_class_data = kwargs.get("ionice_class_data")
            if self.ionice_class_data is not None:
                self.ionice_class_data = int(self.ionice_class_data)

    @property
    def has_ionice(self):
        return bool(self.ionice_class is not None)
