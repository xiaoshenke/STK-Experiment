#!/bin/bash

if [ $# -ne 1 ]
then
        echo Usage:./tmp_scp.sh your-code
        exit 2
fi

scp wuxian@192.168.1.103://Users/wuxian/Desktop/STK-Experiment/csv_data/hist/$1.csv csv_data/hist/$1.csv

