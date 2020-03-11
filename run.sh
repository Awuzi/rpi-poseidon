#! /bin/bash

gnome-terminal --window-with-profile=Bash -e 'python3 interfaceInfo.py'
gnome-terminal --window-with-profile=Bash -e 'python3 sqliteInsertionData.py'