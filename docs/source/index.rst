.. md2remark documentation master file, created by
   sphinx-quickstart on Sat Aug 30 00:07:06 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to md2remark's documentation!
=====================================

md2remark is a tool to compile markdown files to remark.js presentations. The main aim of this package is to decouple the content from the html boilerplate around it.

Usage:

.. code-block:: bash

  md2remark {source}

When source is a file, only that file is compiled. When it is a directory, all markdown files within it are compiled. All output is saved in a subdirectory of the current working directory called ``md2remark_build``.
