from ast import Try
from email.mime import audio
import importlib
from googletrans import Translator
from gtts import gTTS
from time import struct_time
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
from flask import Flask
import webbrowser
import os
import pywhatkit as kit
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import seaborn as sns
import subprocess
import random
import array
import imageio
import scipy.ndimage
import cv2






engine=pyttsx3.init("sapi5")
voice=engine.getProperty("voices")
#print(voice[0].id)
engine.setProperty("voice",voice[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning shyam sir")
    elif hour>=12 and hour<16:
        speak("Good afternoon shyam sir")
    else:
        speak("Good Evening shyam sir")
    
    speak(" how can i help you?")
    

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        audio=r.listen(source)    
   
    try:
        print("Recognizing...")
        querry=r.recognize_google(audio)
        print(f"user said: {querry}\n")

    except Exception as e:
        #print(e)
        print("Say that Again please..") 
        return  "None"   
    return querry 

def wifi():
    # now we will store the profiles data in "data" variable by 
          # running the 1st cmd command using subprocess.check_output
          data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')

          # now we will store the profile by converting them to list 
          profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]

           # using for loop in python we are checking and printing the wifi 
          # passwords if they are available using the 2nd cmd command
          for i in profiles:
            # running the 2nd cmd command to check passwords
             results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
            # storing passwords after converting them to list
             results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
               # printing the profiles(wifi name) with their passwords using 
             # try and except method 
             try:
                  print ("{:<30}|  {:<}".format(i, results[0]))
             except IndexError:
                print ("{:<30}|  {:<}".format(i, ""));
          return print

def password():
    # maximum length of password needed
    # this can be changed to suit your password length
    MAX_LEN = 12
    # declare arrays of the character that we need in out password
    # Represented as chars to enable easy string concatenation
    DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']
    UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']
    SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>','*', '(', ')', '<']
    # combines all the character arrays above to form one array
    COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS
    # randomly select at least one character from each character set above
    rand_digit = random.choice(DIGITS)
    rand_upper = random.choice(UPCASE_CHARACTERS)
    rand_lower = random.choice(LOCASE_CHARACTERS)
    rand_symbol = random.choice(SYMBOLS)

    # combine the character randomly selected above
    # at this stage, the password contains only 4 characters but
    # we want a 12-character password
    temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol


    # now that we are sure we have at least one character from each
    # set of characters, we fill the rest of
    # the password length by selecting randomly from the combined
    # list of character above.
    for x in range(MAX_LEN - 4):
            temp_pass = temp_pass + random.choice(COMBINED_LIST)# convert temporary password into array and shuffle to
	    # prevent it from having a consistent pattern
	    # where the beginning of the password is predictable
    temp_pass_list = array.array('u', temp_pass)
    random.shuffle(temp_pass_list)

    # traverse the temporary password array and append the chars
    # to form the password
    
    password =""
    
    for x in temp_pass_list:
           password=password + x;
    print("The password is :",password)
    return print



if __name__ == "__main__":
    wishme()
    while True:
      querry = takecommand().lower()
    #concept for taking task
      if "wikipedia" in querry:
        speak("searching wikipedia...")
        querry = querry.replace("wikipedia","")
        results=wikipedia.summary(querry, sentences=2)
        speak("according to wikipedia")
        print(results)
        speak(results)
      #elif "meaning" in querry:
       #   speak("Searching meaning...")
        #  querry=querry.replace("meaning","")
         # result=PyDictionary
          #word=result.meaning(querry)
          #speak("The meaning is...")
          #print(word)
          #speak(word)
      elif "open youtube" in querry:
          path="https://www.youtube.com/"
          os.startfile(path)
      elif "open animixplay" in querry:
          path1="https://animixplay.to/"
          os.startfile(path1)
      elif "open gmail" in querry:
          path3="https://mail.google.com/mail/u/0/#inbox"
          os.startfile(path3)
      elif "open chrome" in querry:
          path2="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
          os.startfile(path2)
      elif "current time" in querry:
          strTime=datetime.datetime.now().strftime("%H:%M:%S")
          speak(f"the time is: {strTime}")
      elif "open vs code" in querry:
          codepath="C:\\Microsoft VS Code\\Code.exe"
          os.startfile(codepath)
      elif "python libraries" in querry:
          path4="https://www.lfd.uci.edu/~gohlke/pythonlibs/"
          os.startfile(path4)
      elif "open whatsapp" in querry:
          path5="https://web.whatsapp.com/"
          os.startfile(path5)
      elif "open piano" in querry:
          path6="file:///C:/Users/admin/Desktop/piano.html"
          os.startfile(path6)
      elif "send a whatsapp message" in querry:
          kit.sendwhatmsg("+919619991167","hii mummy",16,44)
      elif "play songs" in querry:
          kit.playonyt("fur elise")
      elif "tell me about yourself" in querry:
          speak("Hello! i am Desktop assistant made by master shyam thakur for desktop activities, my name is Albert ")
      elif "how are you albert" in querry:
          speak("I am fine sir, what about yourself hope your day is going beautiful")
      elif "who is shweta" in querry:
          speak("Shweta is your older sister, she is extremly pissed of your behaviour and she like sleeping")
      elif "yep its going absolutely great" in querry:
          speak("Great sir! how can i help you?")
      elif "nope its not going so great" in querry:
          speak("How can i help you to make you feel better?")
      elif "show wi-fi password" in querry:
          speak("Here is the wifi passwords")
          wifi()
      elif "generate a password" in querry:
          speak("Here is the generated password")
          password()              
      elif "exit" in querry:
          speak("if you need help dont come here i wont help you. bye bye")
          sys.exit()