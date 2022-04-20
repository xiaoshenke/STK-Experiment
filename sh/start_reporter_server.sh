#!/bin/bash

echo nohup python engine/report/plan/cli.py start_plan_reporter_engine_mode --mimic_open_code 0

nohup python engine/report/plan/cli.py start_plan_reporter_engine_mode --mimic_open_code 0 >>reporter.log 2>&1 &
