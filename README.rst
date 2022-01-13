My pre-commit hooks collection
==============================

Usage
-----

Add using hooks into your ``.pre-commit-config.yaml``.

.. code-block::

   repos:

     - repo: https://github.com/attakei/pre-commit-hooks
       rev: v0.0.1
       hooks:
         - id: conventional-commits

.. note::

   This collection have hooks in ``commit-msg`` stage.
   Please run command ``pre-commit install -t commit-msg`` after edit ``.pre-commit-config.yaml``.

License
-------

`Apache License, Version 2.0 <./LICENSE>`_
