CUPS drivers for Peripage printers
===================================

This project tries to provide a CUPS driver for Peripage A6+ printers. 

Supported models
----------------

* Peripage A6
* Peripage A6+

Tested models
^^^^^^^^^^^^^

* None




Development
-----------

You can compile the ``.drv`` files to ``.ppd`` files by executing::

    make ppds

in the project's main directory.

Ubuntu/Debian package
^^^^^^^^^^^^^^^^^^^^^

To build the Ubuntu/Debian package, execute::

    ./packaging/build_deb.sh

If you are on linux, but not on a debian-based distribution that lacks the ``dpkg`` command,
a docker image will be downloaded and executed to get the debian toolchain. There is a similar
command ``build_deb_repo.sh`` that you probably won't need, except if you are myself reading
this in a couple of years.

Contributing
------------

If you like to contribute to this project, you are very welcome to do so. If you have any
questions in the process, please do not hesitate to ask us.

Please note that we have a `Code of Conduct`_
in place that applies to all project contributions, including issues, pull requests, etc.

License
-------

The code in this repository is published under the terms of the GPLv3 License.
See the LICENSE file for the complete license text.

This project is based on a work by Raphael Michel o pretix.eu <mail@raphaelmichel.de>. See the
AUTHORS file for a list of all the awesome folks who contributed to this project.

