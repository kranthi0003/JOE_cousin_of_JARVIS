from gtts import gTTS
import speech_recognition as sr
import os
import re
import webbrowser as wr
import smtplib
import requests
import pyttsx3
from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager 
import psutil
import playsound 
import datetime

os.system("C:\\Users\\KK\\Documents\\jarvis\\login.vbs")
playsound.playsound("C:\\Users\\KK\\Downloads\\robot.mp3")
playsound.playsound("C:\\Users\\KK\\Downloads\\jarvis.mp3")
cnt=0

def date():
	now = datetime.datetime.now()
	if(now.hour<12):
		talkToMe("Good morning Sir")
	elif(now.hour>=12 and now.hour<17):
		talkToMe("Good Afternoon Sir")
	elif(now.hour>=17):
		talkToMe("Good evening Sir")


def whatsapp():
	driver = webdriver.Chrome(ChromeDriverManager().install())
	driver.get('http://web.whatsapp.com')
	while(True):
		os.system("C:\\Users\\KK\\Documents\\jarvis\\whatsapp.vbs")
		name=myCommand()
		name=name[0].upper()+(name[1:len(name)]).lower()
		print(name)
		if 'Exit' in name:
			break

		while(True):
			try:
				os.system("C:\\Users\\KK\\Documents\\jarvis\\message.vbs")
				message=myCommand()
				if 'exit' in message:
					break
				os.system("C:\\Users\\KK\\Documents\\jarvis\\count.vbs")
				count=myCommand()

				user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
				user.click()

				msg_box = driver.find_element_by_class_name('_2S1VP')

				for i in range(int(count)):
					msg_box.send_keys(message)
					driver.find_element_by_class_name('_35EW6').click()

			except:
				print('Something Went Wrong :(')
				continue


def talkToMe(audio):
    "speaks audio passed as argument"

    print(audio)
    engine=pyttsx3.init()
    rate=engine.getProperty('rate')
    engine.setProperty('rate',rate-10)
    engine.say('{}'.format(audio))
    engine.runAndWait()
    #  use the system's inbuilt say command instead of mpg123
    #  text_to_speech = gTTS(text=audio, lang='en')
    #  text_to_speech.save('audio.mp3')
    #  os.system('mpg123 audio.mp3')


def myCommand():
    "listens for commands"

    r = sr.Recognizer()

    with sr.Microphone() as source:
        talkToMe('Ready.....')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio).lower()
        print('You said: ' + command + '\n')
        cnt=0
    #loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:

    	talkToMe('Your last command couldn\'t be heard')
    	command = myCommand();

    return command


def assistant(command):
    "if statements for executing commands"
    command=command.lower()
    if('open' in command):
        if('google' in command):
            wr.open_new("https://www.google.com/")
        if('whatsapp' in command):
        	whatsapp()
        if('youtube' in command):
            wr.open_new("https://www.youtube.com/")
    elif('search' in command):
        split1=command.split(" ")    
        del split1[0]
        wr.open_new("https://www.google.com/search?q="+(" ".join(split1)))

    elif 'what\'s up' in command:
        talkToMe('Just doing my thing')
    elif 'joke' in command:
        res = requests.get(
                'https://icanhazdadjoke.com/',
                headers={"Accept":"application/json"}
                )
        if res.status_code == requests.codes.ok:
            talkToMe(str(res.json()['joke']))
        else:
            talkToMe('oops!I ran out of jokes')

    elif 'email' in command:
        talkToMe('Who is the recipient?')
        recipient = myCommand()

        if 'kamesh' in recipient:# one of my friend's email
            talkToMe('What should I say?')
            content = myCommand()

            #init gmail SMTP
            mail = smtplib.SMTP('smtp.gmail.com', 587)

            #identify to server
            mail.ehlo()

            #encrypt session
            mail.starttls()

            #login
            mail.login('sender_email','sender_password')

            #send message
            mail.sendmail('sender_email', 'akasapu.kamesh11@gmail.com', content)

            #end mail connection
            mail.close()

            talkToMe('Email sent.')

        elif 'myself' in recipient:
            talkToMe('What should I say?')
            content = myCommand()

            #init gmail SMTP
            mail = smtplib.SMTP('smtp.gmail.com', 587)

            #identify to server
            mail.ehlo()

            #encrypt session
            mail.starttls()

            #login
            mail.login('sender_email','sender_password')

            #send message
            mail.sendmail('sender_email', 'recievers email', content)

            #end mail connection
            mail.close()

            talkToMe('Email sent.')

       	elif 'aditya' in recipient: #one of my friend's email
            talkToMe('What should I say?')
            content = myCommand()

            #init gmail SMTP
            mail = smtplib.SMTP('smtp.gmail.com', 587)

            #identify to server
            mail.ehlo()

            #encrypt session
            mail.starttls()

            #login
            mail.login('sender email','sender_password')

            #send message
            mail.sendmail('sender_email', 'atiaditya3@gmail.com', content)

            #end mail connection
            mail.close()

            talkToMe('Email sent.')

        else:
            talkToMe('Email Not sent')

    else:
    	if 'hi' in command or 'hello' in command:
    		os.system("C:\\Users\\KK\\Documents\\jarvis\\hi.vbs")      
    	elif 'good' in command or 'great' in command or 'fine' in command:
    		  os.system("C:\\Users\\KK\\Documents\\jarvis\\great.vbs")
    	elif 'name' in command:
    		os.system("C:\\Users\\KK\\Documents\\jarvis\\name.vbs") 
    	elif command in ['who is jarvis','what is jarvis']:
    		os.system("C:\\Users\\KK\\Documents\\jarvis\\whojarvis.vbs")
    		wr.open_new("https://www.google.com/search?q="+command)



date()
talkToMe('I am ready for your command')
cnt=0
#loop to continue executing multiple commands
while True:
	
	battery = psutil.sensors_battery()
	percent = str(battery.percent)
	plugged = battery.power_plugged
	if int(percent)<20 and plugged==False:
		playsound.playsound("C:\\Users\\KK\\Downloads\\Battery.mp3")
	print(percent+'%')
	command=myCommand()
	if('shutdown' in command):
		playsound.playsound("C:\\Users\\KK\\Downloads\\disconnected.mp3")
		raise SystemExit
	assistant(command)
