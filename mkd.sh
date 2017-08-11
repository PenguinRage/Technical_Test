#!/bin/bash
# Non-accessible
# Just a quick script to create directories and READMEs

for i in {2..9}; do
  mkdir q"$i"  
  touch "q$i/README.md"
done
