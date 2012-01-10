#!/bin/bash
cd "`dirname "$0"`"

if ! test -d bin; then
    echo "Creating virtual env"
    virtualenv  --no-site-packages .
fi
. bin/activate
echo "Installing mmh3"
bin/pip install mmh3


echo "Done"
echo "Start development by running"
echo "  . bin/activate"
echo "  python _name_of_script_.py"


