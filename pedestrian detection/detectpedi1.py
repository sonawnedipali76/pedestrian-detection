#import numpy as np
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import cv2 as cv
import os
body_cascade = cv.CascadeClassifier('haarcascade_fullbody.xml')
from email.mime.base import MIMEBase
from email import encoders
#cap = cv.VideoCapture(0)
cap = cv.VideoCapture('i2.jpg')
#cap = cv.VideoCapture('v1.mp4')
#cap = cv.imread('i.jpg')
capacity=10
def SendMail():
    mail_content = 'Hello,This is a simple mail. There is only text, no attachments are there The mail is sent using Python SMTP library.Thank You'
#The mail addresses and password

    sender_address = 'detectpedestrian926@gmail.com'
    sender_pass = 'Detectaion@123'
    receiver_address = 'sonawnedipali76@gmail.com'
    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'A test mail sent by Python. It has an attachment.'   #The subject line
    #The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'plain'))
   # attach_file.add_header
    attach_file_name = 'abh.jpg'
    attach_file = open(attach_file_name, 'rb') # Open the file as binary mode
    payload = MIMEBase('application', 'octate-stream')
    payload.set_payload((attach_file).read())
    encoders.encode_base64(payload) #encode the attachment
    #add payload header with filename
    payload.add_header('Content-Decomposition', 'attachment', filename=attach_file_name)
    message.attach(payload)
    
    #Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    session.starttls() #enable security
    session.login(sender_address, sender_pass) #login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print('Mail Sent')
   
#open("vid1.mp4")
while 1:
    #read frame from video
    ret, img = cap.read()
    #convert to gray scale of each frame
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    #detects pedestrians of different sizes in the input imge
    bodies = body_cascade.detectMultiScale(gray, 1.1, 5)
#  
    #to draw a rectangle in each pedestrians
    
    for (x,y,w,h) in bodies:
        cv.rectangle(img,(x-20,y-1),(x+w+20,y+h*8),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        
      #  SendMail()
    cv.putText(img, str(len(bodies)), (25,25) , cv.FONT_HERSHEY_SIMPLEX,1, (255, 25, 155) , 2, cv.LINE_AA)
    if(len(bodies)>=capacity):
         os.startfile("aud.mp3")
         cv.imwrite('abh.jpg', img)
         SendMail()
       # SendMail()
    
    #display frames in a window
    cv.imshow('img',img)
    #wait for enter key to stop
    if cv.waitKey(1) & 0xff == ord('q'):
        break
    #all captured videos must be released
cv.destroyAllWindows()