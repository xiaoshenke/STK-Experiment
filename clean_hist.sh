#!/bin/bash


export HISTTIMEFORMAT="%F %T "
history |gawk '{$1="";print $0}'|tail -n 20
