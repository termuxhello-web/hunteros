#!/bin/bash
APP=$1
# Run app in Firejail / Proot sandbox
firejail --quiet --noprofile $APP &
echo "App $APP is running sandboxed"
