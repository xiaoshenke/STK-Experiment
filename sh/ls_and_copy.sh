#!/bin/bash
# Usage ./ls_and_copy.sh your-code

if [ $# -ne 1 ]
then
        echo Usage: ./ls_and_copy.sh your-code
        exit 2
fi

ls |grep $1 |xargs ./copy_to.sh


