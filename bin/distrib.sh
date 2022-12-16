#!/bin/bash
# Create a new distribution. Runs twine to upload the file.
if [ -d dist ] 
then
    rm -rf $DIR
fi
#python setup.py sdist
python -m build
twine upload dist/*.*
