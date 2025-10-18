#!/bin/bash
# Create a new distribution. Runs twine to upload the file.
if [ -d dist ] 
then
    rm -rf dist
fi
python -m build
twine upload dist/*.*
