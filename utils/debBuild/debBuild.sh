#!/bin/sh

TEMP_DIR=temp

echo "Starting deb package build"

echo "Making temporary directory tree"
mkdir -p $TEMP_DIR
mkdir -p $TEMP_DIR/etc/
mkdir -p $TEMP_DIR/usr/bin/
mkdir -p $TEMP_DIR/DEBIAN

echo "Copy control file for DEBIAN/"
cp ./DEBIAN/control $TEMP_DIR/DEBIAN/

echo "conffiles setup for DEBIAN"
cp ./DEBIAN/conffiles $TEMP_DIR/DEBIAN/

echo "Copy binary into place"
cp ./bin/primes $TEMP_DIR/etc/

echo "Configuration file into place"
cp ./bin/primes.conf $TEMP_DIR/etc/

echo "Copy preinst, prerm, postrm files into place"
cp ./DEBIAN/postinst $TEMP_DIR/DEBIAN/
cp ./DEBIAN/prerm $TEMP_DIR/DEBIAN/
cp ./DEBIAN/postrm $TEMP_DIR/DEBIAN/

echo "Building deb file"
dpkg-deb --root-owner-group --build $TEMP_DIR
mv $TEMP_DIR.deb primes-v2.0.0.deb