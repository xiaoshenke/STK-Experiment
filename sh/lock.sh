#!/bin/bash

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

python util/crypt/crypt_all.py

rm secret

