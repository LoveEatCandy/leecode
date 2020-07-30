#!/bin/bash
git pull origin master
git add -A && git commit -m '+' && git push origin master
echo "--- DONE SCRIPT PUSH ---"