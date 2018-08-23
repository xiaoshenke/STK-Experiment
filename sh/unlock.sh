#!/bin/bash

if [ $# -ne 1 ]
then
        echo Usage:./unlock.sh your-secret
        exit 2
fi

sec=$1

echo $sec > secret

sh sh/uncrpyt.sh

for csv in `ls | grep [.]csv`
do
        echo python cmd.py decrypt_df_file $csv
        python cmd.py decrypt_df_file $csv
done

