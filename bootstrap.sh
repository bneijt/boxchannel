#!/bin/bash
set -e #Exit on any sub-process failure
cd "`dirname "$0"`"

if ! test -d bin; then
    echo "Creating virtual env"
    virtualenv  --no-site-packages .
fi
. bin/activate
echo "Installing in virtual env"
python setup.py install

echo "Done"
echo "Start development by running"
echo "  . bin/activate"
echo "  python _name_of_script_.py"


