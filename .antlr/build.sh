#!/bin/bash

# install antlr4 in mac ref:https://github.com/antlr/antlr4/blob/master/doc/getting-started.md

#export CLASSPATH=".:/usr/local/lib/antlr-4.7.1-complete.jar:$CLASSPATH"
#alias antlr4='java -Xmx500M -cp "/usr/local/lib/antlr-4.7.1-complete.jar:$CLASSPATH" org.antlr.v4.Tool'

antlr4 -visitor -Dlanguage=Python2 Source.g4
