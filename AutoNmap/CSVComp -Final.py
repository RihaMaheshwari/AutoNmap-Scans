#!/usr/bin/python

from csv_diff import load_csv, compare
import difflib
from datetime import date
from datetime import timedelta
import sys

arg = str(sys.argv[1])
print(arg)
#========================================================================================================
def SendMail(diffr, arg):
        import smtplib, ssl
        from email.mime.text import MIMEText
        from email.mime.multipart import MIMEMultipart
        from email.mime.base import MIMEBase
        from email.mime.text import MIMEText
        #from email import Encoders

        sender_email = "<sender_email>"
        receiver_email = "<receiver_email"
        password = "<password>"

        message = MIMEMultipart("alternative")
        message["Subject"] = "Nmap Scan Alert"
        message["From"] = sender_email
        message["To"] = receiver_email
        diffstr = ''
        nochange = "No Change In The Scans."
        if diffr != nochange:
            for i in diffr:
                for j in i:
                    diffstr = diffstr+"       |       "+j
                diffstr = diffstr+"<br>"
        else:
            diffstr=diffr
        # Create the plain-text and HTML version of your message
        text = """\
        -------------------------------------------------------------------------------------------------------"""
        html = """\
        <html>
          <body>
            <p><h4>Hi Team,</h4>
               Please find attached the Recent Nmap Scan.
               Following is the summary of changes:- <br><br>
                """+str(diffstr)+"""
            </p>
          </body>
        </html>
        """

        print(html)

        # Turn these into plain/html MIMEText objects
        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")
        print(arg)
        #Attach File
        today = date.today()
        report = '<Path>/Reports/'+arg+'+Report'+str(today)+'.csv'
        print(report)
        part = MIMEBase('application', 'csv')
        part.set_payload(open(report, 'rb').read())
        #encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment', filename='DailyReport.csv')

        #End Attach File
        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        message.attach(part1)
        message.attach(part2)
        message.attach(part)

        # Create secure connection with server and send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(
                sender_email, receiver_email, message.as_string()
           )

#========================================================================================================
today = date.today()
Previous_Date = today - timedelta(days = 1)
fn = '<Path>/Reports/'+arg+'+ReportAllports'+str(today)+'.csv'
fn1 = '<Path>/Reports/'+arg+'+ReportAllports'+str(Previous_Date)+'.csv'
print(fn)
print(fn1)

lines1 = open(fn1).readlines()
lines2 = open(fn).readlines()
added = [['IP Address', 'Port']]
for line in difflib.unified_diff(lines1, lines2, fromfile=fn, tofile=fn1, lineterm=''):
   try:
    #Lines Added In File two
    if line.startswith('+')== True and line.startswith('@')!= True and line.startswith('++')!= True:
        line=line.strip('+')
        line=line.strip('\n')
        #print("Added:"+line+"")
        #added.append("<br>")
        added.append(line.split(","))


   except:
        print(" ")

print(added)

#Trigger mail even if no difference found
if added!=[['IP Address', 'Port']]:
    print("Triggering Mail:")
    SendMail(added, arg)
else:
    nochange = "No Change In The Scans."
    print("Daily Scan Completed - No Changes")
    SendMail(nochange, arg)
