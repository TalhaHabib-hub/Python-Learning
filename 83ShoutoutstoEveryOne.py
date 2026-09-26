'''Write a program to pronounce list of names using win32 API.
if you are given a list l as follows:
l = ['Ali', 'Talha', 'Shibli']'''
# my program should pronounce 
'''
you are amazing Ali
you are amazing Talha
you are amazing Shibli
'''
# Source - https://stackoverflow.com/a/61388230
# Posted by Charlie
# Retrieved 2026-06-27, License - CC BY-SA 4.0

# import win32com.client as wincl

# speaker_number = 1
# spk = wincl.Dispatch("SAPI.SpVoice")
# vcs = spk.GetVoices()
# SVSFlag = 11
# print(vcs.Item (speaker_number) .GetAttribute ("Name")) # speaker namea
# spk.Voice
# spk.SetVoice(vcs.Item(speaker_number)) # set voice (see Windows Text-to-Speech settings)
# spk.Speak("Hello, it works!")

import win32com.client
import time

l = ['Ali', 'Talha', 'Shibli']

# Create SAPI voice object
speaker = win32com.client.Dispatch("SAPI.SpVoice")

while True:
    # print(f"Speaking: {name}")
    speaker.speak('What is your name?')
    name = input('What is your name?')
    speaker.Speak(name)
    print(f" {name} beautiful name though ")
    speaker.Speak('beautiful name though')  # speak the name
    exit = input('exit or no')
    if exit == 'exit':
        break
    time.sleep(0)      # small pause between names