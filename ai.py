
from multiprocessing.connection import wait
from flask import after_this_request
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
from webbrowser import get
import pywhatkit
import sys
import os
import cv2
import numpy as np
import pyautogui as p
import time
from keyboard import press
from keyboard import press_and_release
from pynput.keyboard import Key, Controller
from twilio.rest import Client
#from client.textui import progress
#from ecapture import ecapture as ec
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine. setProperty("rate", 150)
r = sr.Recognizer()
r.energy_threshold = 80

keyboard = Controller()



def speak(audio):
	engine.say(audio)
	print(audio)
	engine.runAndWait()


def takecommand():
	
	r = sr.Recognizer()
    
    
	
	with sr.Microphone() as source:
        
		
		print("Listening...")
		r.pause_threshold = 0.6
		audio = r.listen(source)
           

	try:
		print("Recognizing...")
		command = r.recognize_google(audio, language ='en-in')
		print(f"User said: {command}\n")

	except Exception as e:
		print(e)
		print("Unable to Recognize your voice.")

		return "None"
	
	return command
def wish():
    hour = int(datetime.datetime.now().hour)
    name = "Aaditya"

    if hour>=0 and hour<=11:
        speak("good MORNING" + name )

    if hour>=12 and hour<=18:
        speak("good afternoon" + name )

    elif hour>=19 and hour<=24:
        speak("good evening" +  name)

    speak("What's going on sir! How may I help you")


def hacker():
    query = takecommand().lower()
    if "I am Aditya" in query:
        speak("Ok you cheater you are using my sir's name and trying to hack this computer using command prompt")

def passcheck():
    speak("Ok you cheater you are using my sir's name and tring to hack this computer using command prompt")
    speak("if you really are my Sir then tell the password")
    query = takecommand().lower()
    
    if "775" in query:
        speak("sorry Sir I thought someone is using your name to hack this pc I am happy you are there")
        speak("opening command prompt")
        os.system("start cmd")
    else:
        speak("you cheater this is the wrong password")

def te():
        keyboard = Controller()
        keyboard.press(Key.esc)
        keyboard.release(Key.esc)
        cv2.destroyAllWindows()
        p.press ("esc")
        speak("face recognition sucessfull")
        keyboard.press(Key.esc)
        wish()

        query = takecommand().lower()
        
        while True:
            

                if "+" in query:
                    query = query.replace("what's", "")
                    query = query.replace("plus", "")
                    query = query.replace("what is", "")
                    query = query.replace("+", "")
                    a=int(input("Number of elements in the array:-"))
                    n=list(map(int, input(query).strip().split()))
                    print(n)

                    print(query)

                if "open notepad" in query:

                    query = query.replace("open", "")
                    speak("opening "+query+" sir")
                    npath = "C:\\Windows\\system32\\notepad.exe"
                    os.startfile (npath)

                elif "open command prompt" in query:

                    speak("Sir are you realy there or someone else is trying to open command prompt")

                    hacker()
                    
                    passcheck()

                #elif "open camera" in query:
                    #cap = cv2.VideoCapture(0)
                    #while True:
                        #ret, img = cap.read()
                        #cv2.imshow('webcam', img)
                        #k = cv2.waitKey(10)
                        #if k==9:
                            #break;
                    #cap.release()
                    #cv2.destroyAllWindows()

                elif "play" and "music" in query:
                    speak("Sir you have not added this function yet")

                elif "ip address" in query:
                    ip = get('https://api.ipify.org').text
                    speak(f"Sir your ip address is {ip}")

                elif "wikipedia" in query:
                    speak("searching wikipedia...")
                    query = query.replace("wikipedia", "")
                    results = wikipedia.summary(query, sentences=2)
                    speak("according to wikipedia")
                    speak(results)
                    print(results)

                elif "open" in query:
                    #speak("what do you want to open")
                    #query=takecommand()-

                    if ".com" in query:

                        query = query.replace("open ", "")
                        query = query.replace(" ", "")
                        speak("opening  "+ query + " sir")
                        #query = query.replace("on web", "")
                        print(query)
                        webbrowser.open("www."+ query)
                    
                    elif ".in" in query:
                        query = query.replace("open ", "")
                        query = query.replace(" ", "")
                        speak("opening  "+ query + " sir")
                        print(query)
                        webbrowser.open("www."+query)

                elif "what is" in query or "search for" in query:
                    #speak("sir, what do you want to search for")
                    #query = takecommand().lower()
                    #query = query.replace("what is", "")
                    query = query.replace("search for ", "")
                    speak("searching for" + query)
                    
                    webbrowser.open("https://www.google.com/search?q="+ query)
                    #speak(webbrowser.open)

                #elif "search for" in query:
                    #speak("sir, what do you want to search for")
                    #query = takecommand().lower()
                    #
                    ##speak("searching for" + query)
                    
                    #webbrowser.open("https://www.google.com/search?q="+ query)
                    #speak(webbrowser.open

                #elif "how are you" in query:
                    #response()

                elif "tell me the time" in query:
                    tm = datetime.datetime.now().strftime("%H:%M:%S")   
                    speak(f"Sir, the time is " + tm)


                elif "ok thanks" in query or "no thanks" in query or "jarvis exit" in query or "exit" in query or "close your self" in query:
                    speak("thank you for using me sir")
                    sys.exit()

                elif "don't listen" in query or "stop listening" in query:
                    speak("for how much time you want to stop jarvis from listening commands")
                    a = (takecommand())
                    a = a.replace("a","")
                    a = a.replace("b","")
                    a = a.replace("c","")
                    a = a.replace("d","")
                    a = a.replace("e","")
                    a = a.replace("f","")
                    a = a.replace("g","")
                    a = a.replace("h","")
                    a = a.replace("i","")
                    a = a.replace("j","")
                    a = a.replace("k","")
                    a = a.replace("l","")
                    a = a.replace("m","")
                    a = a.replace("n","")
                    a = a.replace("o","")
                    a = a.replace("p","")
                    a = a.replace("q","")
                    a = a.replace("r","")
                    a = a.replace("s","")
                    a = a.replace("t","")
                    a = a.replace("v","")
                    a = a.replace("w","")
                    a = a.replace("x","")
                    a = a.replace("y","")
                    a = a.replace("z","")
                    am = int(float(a))
                    
                    time.sleep(am)
                    print(takecommand())
                    print(am)
                    speak("sir i am back")

                elif "play" in query:
                    query=query.replace("play","")
                    speak("playing" + query)
                    pywhatkit.playonyt(query)
            
                elif "open blender" in query:
                    speak("opening blender Sir")

            
                elif "tum kaise ho"  in query:
                    speak("main theek hun Sir")

                elif "chrome" in query:

                    query = query.replace("Chrome" , "")
                    webbrowser.open("chrome://" + query)

                

                elif "restart" in query:
                    facerec()

                elif "skip ad" in query:
                    press_and_release(".")

                elif "pause" in query:
                    press_and_release("spacebar")

                elif "add a else if line" in query:
                    press_and_release("e")
                    press_and_release("l")
                    press_and_release("i")
                    press_and_release("f")
                    press_and_release(" ")
                    press_and_release("i")
                    press_and_release("n")
                    press_and_release(" ")
                    press_and_release("q")
                    press_and_release("u")
                    press_and_release("e")
                    press_and_release("r")
                    press_and_release("y")
                    press_and_release("shift + :")
                
                

                elif "blender" in query:

                    if "delete all object" in query:
                        speak("deleted")
                        press_and_release("a")
                        press_and_release("a")
                        press_and_release("a")
                        press_and_release("a")
                        print("wait")
                        press_and_release("delete")

                    elif "add a" in query:
                        query = query.replace("add a" , "")
                        speak("added sir" + query)

                        if "cube" in query:
                            press_and_release("shift+aa")
                            

                query = takecommand().lower()

def facerec():
    recognizer = cv2.face.LBPHFaceRecognizer_create() # Local Binary Patterns Histograms
    recognizer.read('trainer/trainer.yml')   #load trained model
    cascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath) #initializing haar cascade for object detection approach

    font = cv2.FONT_HERSHEY_SIMPLEX #denotes the font type


    id = 1 #number of persons you want to Recognize


    names = ['aaryan']  #names, leave first empty bcz counter starts from 0


    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW) #cv2.CAP_DSHOW to remove warning
    cam.set(3, 640) # set video FrameWidht
    cam.set(4, 480) # set video FrameHeight

    # Define min window size to be recognized as a face
    minW = 0.1*cam.get(3)
    minH = 0.1*cam.get(4)

    # flag = True

    while True:

        ret, img =cam.read() #read the frames using the above created object

        converted_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  #The function converts an input image from one color space to another

        faces = faceCascade.detectMultiScale( 
            converted_image,
            scaleFactor = 1.2,
            minNeighbors = 5,
            minSize = (int(minW), int(minH)),
        )

        for(x,y,w,h) in faces:

            cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2) #used to draw a rectangle on any image

            id, accuracy = recognizer.predict(converted_image[y:y+h,x:x+w]) #to predict on every single image

            # Check if accuracy is less them 100 ==> "0" is perfect match 
            if (accuracy >70):
                id = names[id]
                accuracy = "  {0}%".format(round(100 - accuracy))
                te()

            elif(accuracy <50):
                id = "unknown"
                accuracy = "  {0}%".format(round(100 - accuracy))
                speak("You are not my Sir!")
        
            cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
            cv2.putText(img, str(accuracy), (x+5,y+h-5), font, 1, (255,255,0), 1)  
    
        cv2.imshow('camera',img) 

        k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
        if k == 27:
            break

    # Do a bit of cleanup
    print("Thanks for using this program, have a good day.")
    cam.release()
    cv2.destroyAllWindows()



            #elif "send message" in query:
                #skmgsdkjgks
if __name__ =="__main__":
    facerec()
