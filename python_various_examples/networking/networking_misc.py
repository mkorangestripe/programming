# snmp
import netsnmp
oid = netsnmp.Varbind('sysDescr')
netsnmp.snmpwalk(oid, Version = 2, DestHost = "192.168.1.112", Community = "public")


# Email
import smtplib
from email.mime.text import MIMEText

COMMASPACE = ', '

me = os.environ['USER'] + '@domain.com'
recipients = ['addr1@domain.com', 'addr2@domain.com']

body = 'This is a test from Python smtplib.'
msg = MIMEText(body)

msg['Subject'] = 'Test from Python smtplib'
msg['From'] = me
msg['To'] = COMMASPACE.join(recipients)

s = smtplib.SMTP('localhost')
s.sendmail(me, recipients, msg.as_string())
s.quit()
