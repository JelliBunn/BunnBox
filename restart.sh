#!/bin/bash
cd /path/to/app || exit 1
git pull origin main
pkill -f app.py  # or use systemctl restart yourservice
nohup python3 app.py &> app.log &
sftp://admin@srv734163.hstgr.cloud:2223/__VDS__BunnBox01/

AvaIObdRui2yK1PE8nVjoJLwtrgNjt6khtKNvdZ8c5d56583