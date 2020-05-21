# **AutoNmap Scans**
This script will perform the nmap scans, convert the result into CSV file and compare if any changes are there in open ports. If any changes are found a mail will be triggered along with the changes.

## **Steps**

**Step 1:** Type the following commands in Kali Linux Terminal-

```
$ git clone https://github.com/RihaMaheshwari/AutoNmap-Scans
$ cd AutoNmap-scans
$ mkdir Reports
```
**Step 2:** Enter the IP Addresses you want to scan in IP-Address file.

**Step 3:** Navigate to Recon.sh and change the <Path> to actual Path in Line no. 40,41,42 and 51.

**Step 4:** Navigate to CSVComp-Final.py file and add the sender email-id in line 20 and receiver email-id in line 21 and password in Line 22. Also, change the <Path> to actual Path in Line 60,85 and 86.

**Step 5:** Add the following lines in Cronjob to schedule the task.

```
$ crontab -e
# Add the following line-
0 1 * * * <Path>/Recon.sh <Path>/IP-Address IP-Address >> <Path>/Recon.log 2>&1 &
```
**Note:** If you have large number of subnets to scan you can create multiple IP-Address files. Just Rename the files as IP-Address1, IP-Address2, etc., and replace the same in Cronjob.
