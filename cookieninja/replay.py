"""
cookiecutter.replay.

-------------------
"""
import json
import os
from typing import Any, Mapping

from .utils import make_sure_path_exists


def get_file_name(replay_dir, template_name):
    """Get the name of file."""
    suffix = ".json" if not template_name.endswith(".json") else ""
    file_name = f"{template_name}{suffix}"
    return os.path.join(replay_dir, file_name)


def dump(
    replay_dir: "os.PathLike[str]", template_name: str, context: Mapping[str, Any]
):
    """Write json data to file."""
    make_sure_path_exists(replay_dir)

    if not isinstance(template_name, str):
        raise TypeError("Template name is required to be of type str")

    if not isinstance(context, dict):
        raise TypeError("Context is required to be of type dict")

    if "cookiecutter" not in context:
        raise ValueError("Context is required to contain a cookiecutter key")

    replay_file = get_file_name(replay_dir, template_name)

    with open(replay_file, "w") as outfile:
        json.dump(context, outfile, indent=2)


def load(replay_dir, template_name) -> Mapping[str, Any]:
    """Read json data from file."""
    if not isinstance(template_name, str):
        raise TypeError("Template name is required to be of type str")

    replay_file = get_file_name(replay_dir, template_name)

    with open(replay_file) as infile:
        context = json.load(infile)

    if "cookiecutter" not in context:
        raise ValueError("Context is required to contain a cookiecutter key")

    return context
