#!/bin/bash

#---------------------------------------------------------------------------------#
# Name       = Recon Script                                                       #
# Author     = Jagskap                                                                   #
#---------------------------------------------------------------------------------#


# check for File argument
date
for arg in "$@"
do
if [ -z "$arg" ]; then
  echo -e "\e[35m[*] Usage: \e[36m$0 <FileName-IP Address>"
  echo -e "\e[39m"
  $arg = 'IP1'
fi
echo $1
echo $2

DATE=`date +%F`
# check if packages are installed

if [ ! type nmap &> /dev/null ]; then
  echo "                                            "
  echo "Please install nmap and rerun the script."
  echo "                                            "
  exit 0
fi

# go ahead and start scanning

echo    "                                          "
echo -e "\e[35m#----------------------------------#"
echo -e "\e[35m#          \e[36m   Nmap Scan  \e[35m           #"
echo -e "\e[35m#----------------------------------#"
echo    "                                          "
echo -e "\e[39m"

nmap -Pn -sV -sC -iL $1 -oX <Path>/Reports/$2+_TCPAllports_$DATE
python3 <Path>/xml2csvallport.py -f <Path>/Reports/$2+_TCPAllports_$DATE -csv <Path>/Reports/$2+ReportAllports$DATE.csv
python3 <Path>/xml2csv.py -f <Path>/Reports/$2+_TCPAllports_$DATE -csv <Path>/Reports/$2+Report$DATE.csv

echo    "                                          "
echo -e "\e[35m#----------------------------------#"
echo -e "\e[35m#          \e[36m Difference & Mail \e[35m       #"
echo -e "\e[35m#----------------------------------#"
echo    "                                          "
echo -e "\e[39m"

python3 <Path>/CSVComp\ -Final.py $2

echo    "                                          "
echo -e "\e[35m#----------------------------------#"
echo -e "\e[35m#          \e[36m Done with Scans \e[35m       #"
echo -e "\e[35m#----------------------------------#"
echo    "                                          "
echo -e "\e[39m"
date
break
done
