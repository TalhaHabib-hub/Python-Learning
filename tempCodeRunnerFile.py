
import win32com.client
import time

l = ['Ali', 'Talha', 'Shibli']

# Create SAPI voice object
speaker = win32com.client.Dispatch("SAPI.SpVoice")

for name in l:
    print(f"Speaking: {name}")
    speaker.Speak(name)  # speak the name
    time.sleep(0.5)      # small pause between names