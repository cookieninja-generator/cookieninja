"""Test cookiecutter invocation with nested configuration structure."""
from os import path

from cookieninja import main


def test_cookiecutter_nested_templates(mocker):
    """Verify cookiecutter nested configuration files mechanism."""
    mock_generate_files = mocker.patch("cookieninja.main.generate_files")
    main_dir = path.join("tests", "fake-nested-templates")
    main.cookiecutter(main_dir, no_input=True)
    assert mock_generate_files.call_args[1]["repo_dir"] == path.join(
        main_dir, "fake-project"
    )
