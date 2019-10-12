#!/usr/bin/env bash

rm -rf --verbose dist build *.egg-info && python setup.py sdist  && twine check dist/* && twine upload dist/*