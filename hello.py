import smtplib

# Start SMTP server with gmail
server = smtplib.SMTP('smtp.gmail.com', 587)

# secure server connection
server.starttls()

# login with my google Account
server.login('astic1764@gmail.com', 'hgrb1764@@')

#  sending mail
sender = "astic1764@gmail.com"
reciver = "astic1764@gmail.com"
content = "Hello World!"

server.sendmail(sender, reciver, content)

# closing server
server.close()