#!/bin/bash
# Tests a distribution for a package (argument #1)
# $1 - package name (also name of the repo directory)
PACKAGE=$1
#
if [ -z "${PACKAGE}" ]
then
    echo "*** Must specify the package name."
    exit
fi
#
echo "* Verifying the package name."
pushd ..
if [ -d ${PACKAGE} ]
then
    echo "* Found package."
else
    echo "*** Package not found!"
    exit
fi
#
# Create the test directory in the parent
TESTDIR=testing_${PACKAGE}
if [ -d ${TESTDIR} ]
then
    rm -rf $TESTDIR
    echo "* Deleting existing $TESTDIR."
fi
#
echo "* Creating the virtual environment."
python3 -m venv ${TESTDIR}
source ${TESTDIR}/bin/activate
pip install --upgrade pip
echo "* Doing installs."
pip install ${PACKAGE}
pip install nose
#
echo "* Testing the install."
nosetests ${PACKAGE}/tests
