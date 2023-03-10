.. _directories:

Organizing cookieninjas in directories
---------------------------------------

Cookieninja introduces the ability to organize several templates in one repository or zip file, separating them by directories.
This allows using symlinks for general files.
Here's an example repository demonstrating this feature::

    https://github.com/user/repo-name.git
        ├── directory1-name/
        |   ├── {{cookiecutter.project_slug}}/
        |   └── cookiecutter.json
        └── directory2-name/
            ├── {{cookiecutter.project_slug}}/
            └── cookiecutter.json

To activate one of templates within a subdirectory, use the ``--directory`` option:

.. code-block:: bash

    cookieninja https://github.com/user/repo-name.git --directory="directory1-name"
