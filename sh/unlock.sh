#!/bin/bash

if [ $# -ne 1 ]
then
        echo Usage:./unlock.sh your-secret
        exit 2
fi

sec=$1

echo $sec > secret

sh sh/uncrpyt.sh

