from warnings import warn
from os import path
import json


class Substitution:
    def __init__(self, local_path, language="en"):
        file_path = path.join(local_path, language, "substitutions.json")
        try:
            with open(file_path, encoding="utf-8") as f:
                self.substitutions = json.load(f)
        except FileNotFoundError:
            warn(
                f"substitution for language `{language}` not Implemented",
                ResourceWarning,
            )
            self.substitutions = {}
        if not isinstance(self.substitutions, dict):
            raise TypeError(
                f"Expected dictionary `{file_path}` in but found {type(self.substitutions)}"
            )

    def __getattr__(self, item):
        try:
            return self.substitutions[item]
        except KeyError:
            warn(f"substitutions does not have {item}", Warning)
        return {}
