#! /bin/bash

gnome-terminal --window-with-profile=Bash -e 'python3 interfaceInfo.py'
sleep 2
gnome-terminal --window-with-profile=Bash -e 'python3 sqliteInsertionData.py'