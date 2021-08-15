===============================
Buildroot utils with pre-commit
===============================

This is a Python package that installs `Buildroot utils
<https://git.buildroot.net/buildroot/tree/utils>`_. Currently only ``check-package`` utility
(for linting Buildroot `code style
<https://buildroot.org/downloads/manual/manual.html#_coding_style>`_) is packaged.

This repo doesn't contain Buildroot utils — utilities are fetched from Buildroot Git
repo while Python package is installed.

There is an extra ``lint-buildroot`` script which detects whether linted directory contains
``external.desc`` file (which is a marker for br2 external tree) and calls
``check-package`` with or without ``--br2-external`` option.

Using with pre-commit
=====================

``check-package`` can be used as `pre-commit <https://pre-commit.com>`_ hook (add following
snippets to ``.pre-commit-config.yaml``).

Use *lint-buildroot* hook to autodetect Buildroot top tree vs br2 external tree and run
``check-package``:

.. code:: yaml

   - repo: https://github.com/vlotorev/buildroot-utils
     rev: main  # replace with latest SHA of this repo
     hooks:
       - id: lint-buildroot

Use *check-package* hook to run ``check-package`` directly:

.. code:: yaml

   - repo: https://github.com/vlotorev/buildroot-utils
     rev: main  # replace with latest SHA of this repo
     hooks:
       - id: check-package
         args: [--br2-external, --exclude, Sob, <whatever>]

To give it a try with pre-commit without creating ``.pre-commit-config.yaml``::

  pre-commit try-repo https://github.com/vlotorev/buildroot-utils lint-buildroot --all-files --verbose
