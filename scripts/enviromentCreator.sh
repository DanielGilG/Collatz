#!/bin/bash

# Needs virtualenv installed
# Create new enviroment
# Enter the enviroment
# Install dependencies

virtualenv env1 
source env1/bin/activate
pip install -r ../requirements.txt

echo 
echo 
echo ----------VIRTUAL ENVIROMENT DONE----------
echo 
echo 
