CUPS drivers for Peripage printers
===================================

This project tries to provide a CUPS driver for Peripage A6+ printers.
Seems to be more or less working, but be prepared to face a good amount of issues. 

Supported models
----------------

* Peripage A6 - 203dpi (NOT YET, PPD TODO)
* Peripage A6+ - 304dpi

Tested models
^^^^^^^^^^^^^

* Peripage A6+





Development
-----------

You can compile the ``.drv`` files to ``.ppd`` files by executing::

    make ppds

in the project's main directory.


Installation
------------

In order to install manually on linux do more or less the following::

	sudo cp peribakend.py /usr/lib/cups/backend/peri
	sudo chmod 0700 /usr/lib/cups/backend/peri
	sudo cp rastertoperipage.py /usr/lib/cups/filter/rastertoperipage
	sudo chmod 0755 /usr/lib/cups/filter/rastertoperipage

	copy ppd.gz file to /usr/share/cups/model/

	sudo service restart cups
	
create a 'peripage' printer choosing 'peripage therma printer' using gui or lpadmin and set 'peri://' as protocol.

choose 'peripage' driver. At present the ppd file only exists for A6p (304dpi) model.

mac number for the moment is hardcoded in peribakend.py file, make sure to change it according to your printer before installing.

Contrast level (light, medium, dark) is selectable as printer option.

P.S. I made a typo when naming backend file, it still sticks

P.P.S. Be aware that peripage cups backend must run as root, set the correct permissions.



Ubuntu/Debian package
^^^^^^^^^^^^^^^^^^^^^
PACKAGING IS NOT WORKING YET. INSTALL MANUALLY


To build the Ubuntu/Debian package, execute::

    ./packaging/build_deb.sh

If you are on linux, but not on a debian-based distribution that lacks the ``dpkg`` command,
a docker image will be downloaded and executed to get the debian toolchain. There is a similar
command ``build_deb_repo.sh`` that you probably won't need, except if you are myself reading
this in a couple of years.

Contributing
------------

If you like to contribute to this project, you are very welcome to do so. If you have any
questions in the process, please do not hesitate to ask.


License
-------

The code in this repository is published under the terms of the GPLv3 License.
See the LICENSE file for the complete license text.

This project is based on work by Bitrate16 for Peripage python module and Raphael Michel of pretix.eu <mail@raphaelmichel.de> for a piece of cups filter. See the
AUTHORS file for a list of all the awesome folks who contributed to this project.

