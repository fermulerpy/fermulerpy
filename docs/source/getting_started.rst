Getting started
===============

Overview
--------

FermulerPy is a python package designed specifically for computation of Number Theory in order to bridge the gap between mathematicians
and programmers. This package covers almost every useful function needed to carry out research related to computational proofs, and 
visualizing function plots.


Target Users
------------

This package is extremely easy to use and can be used by student community and researchers across the world. People having very less experience
in python can also use it and visualize number theory functions with few lines of code. We have provided some jupyter notebooks to guide 
such people.

Installation Steps
------------------

Command for installaion (currently not available)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Using pip:

  .. code-block:: sh

       $ pip install fermulerpy

- Using conda:

  .. code-block:: sh

       $ conda install -c conda-forge fermulerpy

Current method for installation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Using package build

  * Fork the repository from github
  * Make a clone in your local system
  * Then follow these commands

  .. code-block:: sh
   
       $ python setup.py sdist bdist_wheel
       $ cd dist
       $ pip install 'package-build-name.whl'


Running fermulerpy programs
---------------------------

Various examples can be found in the `jupyter_notebooks`_ folder.

.. _`jupyter_notebooks` : https://fermulerpy.readthedocs.io/en/latest/jupyter.html
