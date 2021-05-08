Contributing
============

FermulerPy is a open source project, hence all contributions are more than
welcome!

Bug reporting
-------------

Not only things break all the time, but also different people have different
use cases for the project. If you find anything that doesn't work as expected
or have suggestions, please refer to the `issue tracker`_ on GitHub.

.. _`issue tracker`: https://github.com/fermulerpy/fermulerpy/issues

Documentation
-------------

Documentation can always be improved and made easier to understand for
newcomers. The docs are stored in text files under the `docs/source`
directory, so if you think anything can be improved there please edit the
files.

To build the docs, you must first create a development environment (see
below) and then in the ``docs/`` directory run::

    $ cd docs
    $ make html

After this, the new docs will be inside ``build/html``. You can open
them by running an HTTP server::

    $ cd build/html
    $ python -m http.server
    Serving HTTP on 0.0.0.0 port 8000 ...

And point your browser to http://0.0.0.0:8000.

Development environment
-----------------------

These are some steps to set up a development environment:

1. Install git on your computer.
2. Register to GitHub.
3. Fork fermulerpy.
4. Clone your fork.
5. Create a new branch.
6. Make changes and commit.
7. Push to your fork.
8. Open a pull request!


