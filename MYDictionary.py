import requests

try:
    import win32com.client as wincl
except ImportError:
    wincl = None


def get_meaning(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    try:
        res = requests.get(url, timeout=5).json()
        meaning = res[0]['meanings'][0]['definitions'][0]['definition']
        return meaning
    except Exception:
        return "Sorry, I couldn't find a meaning for that word."


def speak_meaning(word, meaning):
    if wincl is None:
        return

    spk = wincl.Dispatch("SAPI.SpVoice")
    spk.Rate = 0
    spk.Volume = 100
    spk.Speak(f"{word}. Meaning: {meaning}")


def main():
    while True:
        word = input("\nEnter a word [or 'exit']: ").strip().lower()

        if word == 'exit':
            break

        meaning = get_meaning(word)
        print(f"\n{word}: {meaning}")
        speak_meaning(word, meaning)


if __name__ == "__main__":
    main()