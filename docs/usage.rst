=====
Usage
=====

Grab a Cookieninja template
----------------------------

First, clone a Cookieninja project template::

    $ git clone https://github.com/audreyfeldroy/cookiecutter-pypackage.git

Make your changes
-----------------

Modify the variables defined in `cookiecutter.json`.

Open up the skeleton project. If you need to change it around a bit, do so.

You probably also want to create a repo, name it differently, and push it as
your own new Cookieninja project template, for handy future use.

Generate your project
---------------------

Then generate your project from the project template::

    $ cookieninja cookieninja-pypackage/

The only argument is the input directory. (The output directory is generated
by rendering that, and it can't be the same as the input directory.)

.. note:: see :ref:`command_line_options` for extra command line arguments

Try it out!



Works directly with git and hg (mercurial) repos too
------------------------------------------------------

To create a project from the cookieninja-pypackage.git repo template::

    $ cookieninja gh:audreyfeldroy/cookiecutter-pypackage

Cookieninja knows abbreviations for Github (``gh``), Bitbucket (``bb``), and
GitLab (``gl``) projects, but you can also give it the full URL to any
repository::

    $ cookieninja https://github.com/audreyfeldroy/cookiecutter-pypackage.git
    $ cookieninja git+ssh://git@github.com/audreyfeldroy/cookiecutter-pypackage.git
    $ cookieninja hg+ssh://hg@bitbucket.org/audreyr/cookiecutter-pypackage

You will be prompted to enter a bunch of project config values. (These are
defined in the project's `cookiecutter.json`.)

Then, Cookieninja will generate a project from the template, using the values
that you entered. It will be placed in your current directory.

And if you want to specify a branch you can do that with::

    $ cookieninja https://github.com/audreyfeldroy/cookiecutter-pypackage.git --checkout develop

Works with private repos
------------------------

If you want to work with repos that are not hosted in github or bitbucket you can indicate explicitly the
type of repo that you want to use prepending `hg+` or `git+` to repo url::

    $ cookieninja hg+https://example.com/repo

In addition, one can provide a path to the cookieninja stored
on a local server::

    $ cookieninja file://server/folder/project.git

Works with git submodules
-------------------------

If you have complex structures where different templates need to be
combined, you could use git submodules in your template. Then, by passing
the parameter '--recurse-submodules' all submodules from your project will
be also downloaded allowing you to used them in your project.

    $ cookiecutter hg+https://example.com/repo --recurse-submodules

In addition, one can combine it with post processing functions in order to
have even more flexibility.

Works with Zip files
--------------------

You can also distribute cookieninja templates as Zip files. To use a Zip file
template, point cookieninja at a Zip file on your local machine::

    $ cookieninja /path/to/template.zip

Or, if the Zip file is online::

    $ cookieninja https://example.com/path/to/template.zip

If the template has already been downloaded, or a template with the same name
has already been downloaded, you will be prompted to delete the existing
template before proceeding.

The Zip file contents should be the same as a git/hg repository for a template -
that is, the zipfile should unpack into a top level directory that contains the
name of the template. The name of the zipfile doesn't have to match the name of
the template - for example, you can label a zipfile with a version number, but
omit the version number from the directory inside the Zip file.

If you want to see an example Zipfile, find any Cookieninja repository on Github
and download that repository as a zip file - Github repository downloads are in
a valid format for Cookieninja.

Password-protected Zip files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If your repository Zip file is password protected, Cookieninja will prompt you
for that password whenever the template is used.

Alternatively, if you want to use a password-protected Zip file in an
automated environment, you can export the `COOKIECUTTER_REPO_PASSWORD`
environment variable; the value of that environment variable will be used
whenever a password is required.

Keeping your cookieninjas organized
------------------------------------

* Whenever you generate a project with a cookieninja, the resulting project
  is output to your current directory.

* Your cloned cookieninjas are stored by default in your `~/.cookiecutters/`
  directory (or Windows equivalent). The location is configurable: see
  :doc:`advanced/user_config` for details.

