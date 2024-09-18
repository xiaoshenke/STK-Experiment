#!/bin/bash

echo 起指数监控器... sh/start_change_observe.sh
sh/start_change_observe.sh

#echo 起风偏组件... sh/start_fengpian_observe.sh
#sh/start_fengpian_observe.sh 

echo 起new-upstp... sh/start_new_upstp.sh 
sh/start_new_upstp.sh

echo 起flush-code-types... sh/start_code_types_observe.sh --mode pan
sh/start_code_types_observe.sh --mode pan

echo 起buyer scheduler... sh/start_buyer_scheduler.sh --mode pan
sh/start_buyer_scheduler.sh --mode pan

