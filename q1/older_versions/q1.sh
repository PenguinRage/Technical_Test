#!/bin/bash

# Argument is a sub-directory name

# finds -name : the directory name at any subdirectory level
# find -type f : recursively finds all the files, excluding directories
# wc -w  : counts all the words

find . -name $1 | xargs -I dir find dir -type f | xargs wc -w

