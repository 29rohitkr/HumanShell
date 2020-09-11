#!/usr/bin/python3
## HumanShell created by Rohit Kumar . This is Cross platform it will work on both Linux and Windows ##
import os
import platform
import smtplib, ssl
try :
    import twilio
    import pyttsx3
    #import pyaudio
    #import speech_recognition as sr
except:
    print("install required libraries, list in requirements.txt")

if platform.system() == "Windows":
    os.system("CLS")
elif platform.system() == "Linux":
    os.system("clear")
elif platform.system() == "Darwin":
    os.system("clear")
#####

print("             ####################################################################################")
print("             #      _   _ _   _ __  __    _    _   _   ____  _   _ _____ _     _                #")
print("             #     | | | | | | |  \/  |  / \  | \ | | / ___|| | | | ____| |   | |               #")
print("             #     | |_| | | | | |\/| | / _ \ |  \| | \___ \| |_| |  _| | |   | |               #")
print("             #     |  _  | |_| | |  | |/ ___ \| |\  |  ___) |  _  | |___| |___| |___            #")
print("             #     |_| |_|\___/|_|  |_/_/   \_\_| \_| |____/|_| |_|_____|_____|_____|           #")
print("             #                                                                                  #")
print("             #                    Turn Your Thoughts Into Command                               #")
print("             #            --------------------------------------------------                    #")
print("             #             Bash/Cmd commands/WhatsApp / SMS / E-Mail                            #")
print("             ####################################################################################")
pyttsx3.speak("Welcome to human shell")
pyttsx3.speak("Turn your thoughts into command")
if platform.system() == 'Linux':
    name = platform.uname()[1]
    mac = platform.uname()[4]
elif platform.system() == 'Windows':
    name = platform.uname().node
    mac = platform.uname().machine
name = str(name)
print("Welcome,", name,"."," You are using ","'",str(platform.system()),mac,"'")
print()
print()
print("       Text editor    network/communication        others              internal     ")
print("    -------------   --------------------------   ----------          ------------   ")
print("      Notepad (W)       chrome    (C)             explorer   (W)      credits  (C)  ")
print("      Vim     (L)       firefox   (C)             wmplayer   (W)      help     (C)  ")
print("      nano    (L)       ipaddress (C)             whoami     (C)      exit     (C)  ")
print("      gedit   (L)       email     (C)             cmd        (W)      clear    (C)  ")
print("      vscode  (C)       sms       (C)             bash       (L)                    ")
print("                        whatsapp  (C)             calculator (C)                    ")
print()
print("** notepad is default in Windows / nano is default in linux  // W = Windows / L = Linux / C = cross-platform ")
print()
print(' Recommended :  Type "help", "credits" for more information.')
pyttsx3.speak("first read help section to know more about humanshell")
print()
while True:
    print()
    print("                         Enter Your Thought and Human Shell will try to process it                           ")
    print(" ----------------------------------------------------------------------------------------------------------- ")
    print("Example : type help to see help, Now go try it below.")
    print()
    
    query = input(" Your thought goes here  $ ")
    ##############################  clear Screen ############
    if (("clear" in query) or ("cls" in query) or ("CLS" in query) or ("CLEAR" in query) or ("Clear" in query)):
        if platform.system() == "Windows":
            os.system("CLS")
        elif platform.system() == "Linux":
            os.system("clear")
        elif platform.system() == "Darwin":
            os.system("clear")

#############################  Exit ###################
    if(("quit" in query) or ("exit" in query ) or ("get out" in query) or ("out of here" in query )):
        exit()
###############################################

###############################  HELP SECTION ########################################
    if (("help" in query) or ("Help" in query) or ("how to use" in query)):
        if platform.system() == "Windows":
            os.system("CLS")
        elif platform.system() == "Linux":
            os.system("clear")
        elif platform.system() == "Darwin":
            os.system("clear")
        
        print("             ####################################################################################")
        print("             #      _   _ _   _ __  __    _    _   _   ____  _   _ _____ _     _                #")
        print("             #     | | | | | | |  \/  |  / \  | \ | | / ___|| | | | ____| |   | |               #")
        print("             #     | |_| | | | | |\/| | / _ \ |  \| | \___ \| |_| |  _| | |   | |               #")
        print("             #     |  _  | |_| | |  | |/ ___ \| |\  |  ___) |  _  | |___| |___| |___            #")
        print("             #     |_| |_|\___/|_|  |_/_/   \_\_| \_| |____/|_| |_|_____|_____|_____|           #")
        print("             #                                                                                  #")
        print("             #                    Turn Your Thoughts Into Command                               #")
        print("             #            --------------------------------------------------                    #")
        print("             #            Bash/Cmd commands // WhatsApp // SMS // E-Mail                        #")
        print("             ####################################################################################")
        pyttsx3.speak("this is help section.")
        print()
        print("  I am ROHIT KUMAR & I am new to Python.This is Human Shell my first project in python. This is Cross platform it will work on  both ")
        print("  Linux and Windows. ")
        print()
        print("You can directly use any common command prompt or bash shell commands in human shell ")
        print("OR you can use human type sentences/query to make your work easy (only for mentioned application on main screen)")
        print("For Example :")
        print()
        print(" >> chrome ")
        print(" >> Enter URL : https://github.com    # then press Enter")
        print()
        print(" >> i want to surf web")
        print(" >> I want to securely surf the web   # it will open duckduckgo search engine")
        print(" >> notepad ")
        print(" >> Enter file name :          # then press enter ")
        print()
        print(" >> i want to write something ")
        print(" >> i want to take notes via vim")
        print(" >> i want to take notes in texteditor")
        print(" >> explorer  # this command is for file explorer in windows only")
        print()
        print(" >> plz open browser for me ")
        print(" >> i want to write a note")
        print(" >> plz open vscode for me")
        print()
        print("Default texteditor in 'windows' is Notepad and in 'LINUX' is nano editor")
        print("Default web Browser in 'Windows' is chrome (must have installed in your pc) and in 'linux' is mozilla Firefox")
        print(" This is Still Incomplete and lacking Many thing. I will try to solve it.")
        print(" >> who the hell i am  | >> who the hell am i")
        

######################################################################################
############################ Web Browser ####################################
    if platform.system() == "Windows":
        if(("browser" in query) or (("run" in query) and ("browser" in query)) or (("run" in query) and ("chrome" in query)) or ("web" in query) or (("open" in query) and ("chrome" in query))):
            if(("secure" in query) or ("protect" in query) or ("privacy" in query) or ("securely" in query)):
                pyttsx3.speak("Launching chrome in secure mode")
                os.system("chrome www.duckduckgo.com/")
            else:
                pyttsx3.speak("Launching chrome")
                os.system("chrome")
    elif platform.system() == "Linux":
        if(("browser" in query) or (("run" in query) and ("browser" in query)) or (("run" in query) and ("firefox" in query)) or ("web" in query) or (("open" in query) and ("firefox" in query))):
            pyttsx3.speak("Launching firefox")
            os.system("firefox")

    if (query == "chrome"):
        x = input("Enter URL : ")
        url ="chrome " +  x
        os.system(url)
    if (query == "firefox"):
        x = input("Enter URL : ")
        url ="firefox " +  x
        os.system(url) 
      # > I want to securely surf the web 
##################################Who am i#############################################

    if (("whoami" in query) or ("i am" in query) or ("am i" in query)):
        os.system("whoami")

####################### Text Editor ###########################################
    if platform.system() == "Windows":
        if("texteditor" in query or (("run" in query) and ("notepad" in query)) or "write" in query or "notes" in query or (("open" in query) and ("notepad" in query))):
            pyttsx3.speak("Launching notepad")
            os.system("notepad")
            
        if( query == "notepad" ):
            x = input("Enter File Name : ")
            note = "notepad "+ x
            pyttsx3.speak("Launching notepad")
            os.system(note)

        if("codeeditor" in query or (("run" in query) and ("vscode" in query)) or(("execute" in query ) and ("code" in query))  or "program" in query or (("open" in query) and ("vscode" in query))):
            pyttsx3.speak("Launching VSCode")
            os.system("code")

        if( query == "vscode"):
            x  = input("Enter File Name (with extension) : ")
            code = "code "+ x
            pyttsx3.speak("Launching VSCode")
            os.system(code)
        
    if platform.system() == "Linux":
        if("texteditor" in query or (("run" in query) and ("nano" in query))  or "write" in query or "notes" in query or (("open" in query) and ("nano" in query))):
            pyttsx3.speak("Launching nano")
            os.system("nano")   
        
        if("codeeditor" in query or (("run" in query) and ("vscode" in query))  or "code" in query or "program" in query or (("open" in query) and ("vscode" in query))):
            pyttsx3.speak("Launching VSCode")
            os.system("code")

        if( query == "vscode"):
            x  = input("Enter File Name (with extension) : ")
            code = "code "+ x
            pyttsx3.speak("Launching VSCode")
            os.system(code)

        if("vimeditor" in query or (("run" in query) and ("vim" in query)) or  (("execute" in query) and ("vim" in query)) or(("open" in query) and ("vim" in query))):
            pyttsx3.speak("Launching vim")
            os.system("vim")

        if( query == "vim"):
            x  = input("Enter File Name (with extension) : ")
            code = "vim "+ x
            pyttsx3.speak("Launching vim")
            os.system(code)

        if("geditor" in query or (("run" in query) and ("gedit" in query)) or  (("execute" in query) and ("gedit" in query)) or(("open" in query) and ("gedit" in query))):
            pyttsx3.speak("Launching gedit")
            os.system("gedit")

        if( query == "gedit"):
            x  = input("Enter File Name (with extension) : ")
            code = "gedit "+ x
            pyttsx3.speak("Launching gedit")
            os.system(code)
#########################################################################################
########################## Calculator ################################
    if platform.system() == "Windows":
        if("calculator" in query or "calc" in query or "calculate" in query or "add" in query or "sum" in query or "subtract" in query or "product" in query):
            pyttsx3.speak("Launching calculator")
            os.system("calc")
    if platform.system() == "Linux":
        if("calculator" in query or "calc" in query or "calculate" in query or "add" in query or "sum" in query or "subtract" in query or "product" in query):
            pyttsx3.speak("launching bc calculator")
            print("Type 'quit' to exit")
            os.systeproduct

######################### Network ########################################
    if platform.system() == "Windows":
        if("ipconfig" in query or "ipaddress" in query or "netstatus" in query or "ip" in query or "mac address" in query or "ip address" in query):
            os.system("ipconfig /all")
    if platform.system() == "Linux":
        if("ipconfig" in query or "ipaddress" in query or "netstatus" in query or "ifconfig" in query):
            os.system("ifconfig") 
    # > what is my ipaddress
########################  Media Player / vlc ###################################
    if platform.system() == "Windows":
        if("media" in query or "music" in query or "wmplayer" in query or (("run" in query) and ("wmplayer" in query)) or (("open" in query) and ("wmplayer" in query))):
            os.system("wmplayer")

############################ File Explorer ########################
    if platform.system() == "Windows":
        if("file explorer" in query or "explorer" in query):
            pyttsx3.speak("Launching windows file explorer")
            os.system("explorer")


#################  Send SMS  #######  Twilio Reference #####################
    # Download the helper library from https://www.twilio.com/docs/python/install

    if("sms" in query or (("send" in query) and ("message" in query)) or "message" in query or (("send" in query) and ("sms" in query))):
        # Your Account Sid and Auth Token from twilio.com/console
        # DANGER! This is insecure. See http://twil.io/secure
        print("You must create an account on 'www.twilio.com' to get your own 'account_sid' , 'account_token' and Sandbox  number ")
        account_sid = input("Enter Account Sid : ")
        auth_token = input("Enter Auth Token : ")
        client = Client(account_sid, auth_token)

        message = client.messages \
                        .create(
                            body=input("Enter Your Message : "),
                            from_=input("Enter your Number(twilio with Country code) : "),
                            to=input("Enter receipent Number (verified Number): ")
                        )

        print(message.sid)
        print("for Reference and help in this section goto https://twilio.com/docs")
####################################################################################

############################## Send Email ##################
    if("mail" in query or "email" in query or (("send" in query) and ("email" in query)) or (("send" in query) and ("mail" in query))):
        print("         This section will work only if Senders Gmail Account's particular option is active :")
        print("             i.e, 'Allow Less Secure Apps'  must be on ")
        print()
        port = 587  # For starttls
        smtp_server = "smtp.gmail.com"
        sender_email = input("Enter your Email : ")
        password = input("Type your password and press enter:")
        receiver_email = input("enter Recepiant Email : ")
        subject = """\
        Subject: Hi there
            """
        message = subject + input("Enter your Message : ") 
        context = ssl.create_default_context()
        with smtplib.SMTP(smtp_server, port) as server:
            server.ehlo()  # Can be omitted
            server.starttls(context=context)
            server.ehlo()  # Can be omitted
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
#############################################################

#####################################  Whatsapp #######################
    if("whatsapp" in query or "chat" in query or(("instant" in query) and ("chat" in query))):

        # client credentials are read from TWILIO_ACCOUNT_SID and AUTH_TOKEN
        print("You must create an account on 'www.twilio.com' to get your own 'account_sid' , 'account_token' and 'Sandbox  number' ")
        account_sid = input("Enter Account_Sid : ")
        auth_token = input("Enter Auth_Token : ")
        client = Client(account_sid, auth_token)

        # this is the Twilio sandbox testing number
        from_whatsapp_number = 'whatsapp:'+input("Enter twilio sandbox number : ")
        # replace this number with your own WhatsApp Messaging number
        to_whatsapp_number = 'whatsapp:'+input("Enter receiver number : ")
        what_message = input(" Enter your message : ")
        client.messages.create(body=what_message,
                            from_=from_whatsapp_number,
                            to=to_whatsapp_number)

#############################################  CMD // Bash Commands ########################################
    if (platform.system() == "Windows") :
        if("cmd" in query or "command" in query or "dos" in query or ("run" in query and ("cmd" in query)) or "prompt" in query ):
            print("         to 'exit' type exit and press enter")
            os.system("cmd")
    if (platform.system() == "Linux"):
        if("bash" in query or "command" in query or "shell" in query or ("run" in query and ("bash" in query)) or "sh" in query):
            print("         to 'exit' type exit and press enter")
            os.system("bash")
############################################################################################################

##################################  Credits ##########################################
    if("credits" in query or "programmer" in query or "developer" in query or "owner" in query):

        if platform.system() == "Windows":
            os.system("CLS")
        elif platform.system() == "Linux":
            os.system("clear")
        elif platform.system() == "Darwin":
            os.system("clear")

        print("             ####################################################################################")
        print("             #      _   _ _   _ __  __    _    _   _   ____  _   _ _____ _     _                #")
        print("             #     | | | | | | |  \/  |  / \  | \ | | / ___|| | | | ____| |   | |               #")
        print("             #     | |_| | | | | |\/| | / _ \ |  \| | \___ \| |_| |  _| | |   | |               #")
        print("             #     |  _  | |_| | |  | |/ ___ \| |\  |  ___) |  _  | |___| |___| |___            #")
        print("             #     |_| |_|\___/|_|  |_/_/   \_\_| \_| |____/|_| |_|_____|_____|_____|           #")
        print("             #                                                                                  #")
        print("             #                    Turn Your Thoughts Into Command                               #")
        print("             #            --------------------------------------------------                    #")
        print("             #             Bash/Cmd commands/WhatsApp / SMS / E-Mail                            #")
        print("             ####################################################################################")

        print("                           My Name is Rohit Kumar. I am a Second Year college Student.")
        print()
        print("                           My Email : 29rkwhitelist@gmail.com / 29rohit.code@gmail.com")
        print()
        print("                           My github : https://github.com/29rohitkr/")
        print()
        print("                           My Linkedin profile : https://www.linkedin.com/in/29rohitkr/")
        print()
        print()
    
