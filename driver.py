#Use command "pythonw driver.py" in this directory to run 24/7

#Ryan Kim
#https://github.com/kimry02

#imports
from plyer import notification
from bs4 import BeautifulSoup
import requests
import datetime
import time
import imaplib
import email
from email.header import decode_header
from collections import deque



if __name__ == "__main__":

    subjectDeq = deque()
    senderDeq = deque()
    dateDeq = deque()

    while True:    
        
        #Email Info
        user = 'ryan02.kim' #for use, change to personal email

        #Use Google App Password for Security
        pw = '' #PW removed for security purposes...
        
        #Desired Tags: Input key strings to search for
        keyTags = ["urgent", "response"]
        
        #IMAP Login and Search Specifications
        imap = imaplib.IMAP4_SSL("imap.gmail.com")
        imap.login(user, pw)
        imap.select("inbox")
        _, mailData = imap.search(None, 'UNSEEN')

        #Gathering Mail
        for entries in mailData[0].split():
            _, data = imap.fetch(entries, '(RFC822)')
            _, bData = data[0]
            mailMsg = email.message_from_bytes(bData)
            for st in keyTags:
                if mailMsg['subject'].lower().find(st.lower()) > -1 or mailMsg['from'].lower().find(st.lower()) > -1:
                    subjectDeq.append(mailMsg['subject'])
                    senderDeq.append(mailMsg['from'].rpartition('<')[0])
                    dateDeq.append(mailMsg['date'])
                    break
            
            #Print Test 
            #for header in ['subject', 'to', 'from', 'date']:
            #    print("{}: {}".format(header, mailMsg[header]))
            

        #Notification System
        while(senderDeq):
            notification.notify(title = senderDeq[0] + ": " + dateDeq[0][0:11], 
                        message = subjectDeq[0], 
                        app_icon = "uofm.ico", 
                        timeout = 999999, 
                        ticker = '',
                        toast = False
                        )
            senderDeq.popleft()
            dateDeq.popleft()
            subjectDeq.popleft()

