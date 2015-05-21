import smtplib
import base64
from os.path import basename

from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.utils import COMMASPACE, formatdate
from email import encoders


""" Mail an attachment """
# http://www.tutorialspoint.com/python/python_sending_email.htm
def sendFromManager():
    host_from_manager = "localhost"
    port_from_manager = "25"

    sender = "do-not-reply@adara.com" # doesn't matter
    receivers = ["bartev.vartanian@adara.com"]
    message = """From: Doctor Who <do-not-reply@adara.com>
    To: Thor Dude <bartev.vartanian@adara.com>
    Subject: IGNORE THIS - ext email 1

    This is a test email
    """
    smtpObj = smtplib.SMTP(host_from_manager, port_from_manager)
    smtpObj.sendmail(sender, receivers, message)

    try:
        smtpObj = smtplib.SMTP(host_from_manager, port_from_manager)
        smtpObj.sendmail(sender, receivers, message)
        print("Successfully sent email")
    except smtplib.SMTPException:
        print("Error: unable to send email")

def sendFromInternal():
    host_adara_internal = "10.101.0.24"
    port_adara_internal = "25"

    sender = "do-not-reply@adara.com" # doesn't matter
    receivers = ["bartev.vartanian@adara.com"]
    message = """From: Doctor Who <do-not-reply@adara.com>
    To: Thor Dude <bartev.vartanian@adara.com>
    Subject: IGNORE THIS - SMTP email test 8

    This is a test email to bartev only
    tabbed text
    """
    try:
        smtpObj = smtplib.SMTP(host_adara_internal, port_adara_internal)
        smtpObj.sendmail(sender, receivers, message)
        print("Successfully sent email")
    except smtplib.SMTPException:
        print("Error: unable to send email")


def sendAttachmentDoesNotWork():
    filename = "dac.xlsm"
    fo = open(filename, "rb")
    fileContent = fo.read()
    encodedContent = base64.b64encode(fileContent)
    host_adara_internal = "10.101.0.24"
    port_adara_internal = "25"

    sender = "do-not-reply@adara.com" # doesn't matter
    receivers = ["bartev.vartanian@adara.com"]

    marker = "AUNIQUEMARKER"

    body = """
This is a test email to bartev only
include dac.xlsm
    """

    # main header
    part1 = """From: Whovian <do-not-reply@adara.com>
To: Rolling Stones <bartev.vartanian@adara.com>
Subject: IGNORE - SMTP attachment 1
MIME-Version: 1.0
Content-type: multipart/mixed; boundary=%s
--%s
    """ % (marker, marker)

    # define message action
    part2 = """Content-Type: text/plain
Content-Transfer-Encoding:8bit

%s
--%s
    """ % (body, marker)

    # define the attachment section
    part3 = """Content-Type: multipart/mixed; name=\"%s\"
Content-Transfer-Encoding:base64
Content-Disposition: attachment; filename=%s

%s
--%s--
    """ % (filename, filename, encodedContent, marker)

    message = part1 + part2 + part3

    smtpObj = smtplib.SMTP(host_adara_internal, port_adara_internal)
    smtpObj.sendmail(sender, receivers, message)

def sendAttachmentDoesNotWork2():
    # http://stackoverflow.com/questions/25346001/add-excel-file-attachment-when-sending-python-email
    msg = MIMEMultipart()
    msg['From'] = "do-not-reply@adara.com"
    msg['To'] = "bartev.vartanian@adara.com"
    msg['Subject'] = "TEST email using MIME-multipart"
    msg.attach (MIMEText("here is the message text"))

    filename = "dac.xlsm"
    fo = open(filename, "rb")
    fileContent = fo.read()
    encodedContent = base64.b64encode(fileContent)

    part = MIMEBase('application', "octet-stream")
    part.set_payload(fileContent)
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename=%s' % filename)
    msg.attach(part)

    host_adara_internal = "10.101.0.24"
    port_adara_internal = "25"

    sender = "do-not-reply@adara.com" # doesn't matter
    receivers = ["bartev.vartanian@adara.com"]

    smtp = smtplib.SMTP(host_adara_internal, port_adara_internal)
    smtp.sendmail(sender, receivers, msg.as_string)


    # prev example didn't work
    from email.mime.multipart import MIMEMultipart
    from email.mime.application import MIMEApplication

    msg = MIMEMultipart()

    msg['Subject'] = "SOME ATTACHMENT"
    me = 'do-not-reply@adara.com'
    to = ['bartev.vartanian@adara.com', me]
    msg['From'] = me
    msg['To'] = COMMASPACE.join(to)
    msg.preamble = "The preamble"

    filename = "dac.xlsm"
    fo = open(filename, "rb")
    # fileContent = fo.read()
    # encodedContent = base64.b64encode(fileContent)
    encodedContent = MIMEApplication(fo.read)
    fo.close()
    msg.attach(encodedContent)

    s = smtplib.SMTP(host_adara_internal, port_adara_internal)
    s.sendmail(me, to, msg.as_string)
    s.quit()

host_adara_internal = "10.101.0.24"
port_adara_internal = "25"

send_from = "do-not-reply@adara.com"
send_to = ["bartev.vartanian@adara.com"]
subject = "sendAttachWip"
text = "here is some text for the body"
files = None
server = host_adara_internal
port = port_adara_internal

def sendAttachWorks(send_from, send_to, server, port, subject, text, files=None):
    # http://stackoverflow.com/questions/3362600/how-to-send-email-attachments-with-python

    # send_from
    # send_to   a LIST of email addresses
    # server    ip address of smtp server ("10.101.0.24" for ADARA internal, "localhost" for manager)
    # port      port for mailserver (25 for ADARA internal and manager)
    # subject   subject line
    # text      body text
    # files     a LIST of file names e.g. ['abc.txt', 'def.csv', 'ghi.xlsm'] or ['abc.txt']

    assert isinstance(send_to, list)

    msg = MIMEMultipart(
        From = send_from,
        To = COMMASPACE.join(send_to),
        Date = formatdate(localtime=True),
        Subject = subject
    )
    msg.attach(MIMEText(text))

    for f in files or []:
        part = MIMEBase('application', 'base64')
        part.set_payload(open(f, 'rb').read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="%s"' % basename(f))
        msg.attach(part)

    try:
        s = smtplib.SMTP(server, port)
        s.sendmail(send_from, send_to, msg.as_string())
        s.close()
        print("Successfully sent email")
    except smtplib.SMTPException:
        print("Error: unable to send email")



sendAttachWorks(send_from= send_from,
              send_to= send_to,
              server= server,
              port= port,
              subject= subject,
              text= text,
              files= ['dac.xlsm'])

__author__ = 'bvartanian'

