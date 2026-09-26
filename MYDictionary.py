import requests
import win32com.client as wincl

# Setup TTS
spk = wincl.Dispatch("SAPI.SpVoice")
spk.Rate = 0 # speed
spk.Volume = 100

def get_meaning(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    try:
        res = requests.get(url, timeout=5).json()
        # Grab first definition
        meaning = res[0]['meanings'][0]['definitions'][0]['definition']
        return meaning
    except:
        return "Sorry, I couldn't find a meaning for that word."

while True:
    word = input("\nEnter a word [or 'exit']: ").strip().lower()

    if word == 'exit':
        break

    meaning = get_meaning(word)
    print(f"\n{word}: {meaning}")

    # Speak it out loud
    spk.Speak(f"{word}. Meaning: {meaning}")