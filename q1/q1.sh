#!/bin/bash
# finds the directory name at any level
# grep -r recursively finds all the files, excluding directories
# wc -w counts all the words
find . -name $1 | xargs -I subdir grep -r '' subdir | wc -w
