#!/bin/bash

for csv in `ls | grep [.]csv`
do
	echo python cmd.py encypt_df_file $csv
	python cmd.py encypt_df_file $csv
done


path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

python util/crypt/crypt_all.py

rm secret

