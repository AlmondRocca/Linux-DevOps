#!/bin/sh

INSTALL_DIR=/usr/bin/
MAIN_PROGRAM_FILE=primes
CONFIGURATION_INSTALL_DIR=/etc/
MAIN_CONFIG_FILE=primes.conf

echo "Installing primes"

cp src/$MAIN_PROGRAM_FILE $INSTALL_DIR/
cp src/$MAIN_CONFIG_FILE $CONFIGURATION_INSTALL_DIR/

echo "Primes installed"
