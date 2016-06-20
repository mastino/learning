#!/bin/bash

#this script requests a message then adds commits and pushes

echo
echo -n "Enter message -> "
read message
git add -A
git commit -m "$message"
git pull origin master
git push origin master
echo

