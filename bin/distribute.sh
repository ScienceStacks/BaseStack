# Builds source and updates PyPI
# A common problem is having out of date packages.
# Do pip install --upgrade for: twine, setuptools, wheel
echo "Have you updated the version number? Press enter to continue."
read -p "$*"
rm -rf dist
python setup.py sdist
twine upload dist/*
