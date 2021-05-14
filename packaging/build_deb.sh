#!/bin/bash
VERSION=0.1.0

mkdir -p dist
mkdir deb.tmp
pushd deb.tmp

mkdir -p debian
mkdir -p debian/DEBIAN

# Write control files
cat <<END > debian/DEBIAN/control
Package: cups-peripage-printers
Version: $VERSION
Section: web
Priority: optional
Architecture: any
Maintainer: Francesco Fantoni
License: GPL-3
Depends: python3, python3-pillow, python3-numpy
Description: CUPS driver for Peripage printers
 .
 CUPS driver for Peripage printers
 .
END

mkdir -p debian/usr/lib/cups/filter
mkdir -p debian/usr/share/cups/model/custom

cd ..
make ppds
cd deb.tmp

cp -r ../ppd debian/usr/share/cups/model/custom/peripage
install -Dm 755 ../rastertoperipage.py debian/usr/lib/cups/filter/rastertoperipage

DPKG=dpkg
DEBDIR=$(pwd)
if ! hash $DPKG 2>/dev/null
then
    DPKG="docker run --rm --entrypoint /usr/bin/dpkg -v $(pwd):/tmp/deb -it raphaelm/ci-pretixdesk-apt"
    DEBDIR=/tmp/deb
fi

mkdir -p ../dist
$DPKG --build $DEBDIR/debian

mv -f debian.deb ../dist/cups-peripage-printers.deb

popd
#rm -rf deb.tmp
