#!/usr/bin/env bash
# OxyX-UB - UserBot
# Copyright (C) 2020 OxyNotOp
#
# This file is a part of < https://github.com/OxyNotOp/OxyX-UB/ >
# PLease read the GNU Affero General Public License in <https://www.github.com/OxyNotOp/OxyX-UB/blob/main/LICENSE/>.

clear
echo -e "\e[1m"
echo "  _    _ _ _             _     _ "
echo " | |  | | | |           (_)   | |"
echo " | |  | | | |_ _ __ ___  _  __| |"
echo " | |  | | | __| '__/ _ \| |/ _  |"
echo " | |__| | | |_| | | (_) | | (_| |"
echo "  \____/|_|\__|_|  \___/|_|\__,_|"
echo -e "\e[0m"
sec=5
spinner=(⣻ ⢿ ⡿ ⣟ ⣯ ⣷)
while [ $sec -gt 0 ]; do
    echo -ne "\e[33m ${spinner[sec]} Starting dependency installation in $sec seconds...\r"
    sleep 1
    sec=$(($sec - 1))
done
echo -e "\e[1;32mInstalling Dependencies ---------------------------\e[0m\n" # Don't Remove Dashes / Fix it
apt-get update
apt-get upgrade -y
pkg upgrade -y
pkg install python wget -y
wget https://raw.githubusercontent.com/OxyNotOp/OxyX-UB/main/resources/session/ssgen.py
pip install telethon
clear
python3 ssgen.py