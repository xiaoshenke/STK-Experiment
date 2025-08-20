#!/bin/bash

echo 版块模版列表
ls engine/observe/buyer/template/|grep xx_|grep [.]properties|sort

echo ""
echo 行情列表
ls engine/observe/buyer/template/|grep -v xx_|grep [.]properties|sort
