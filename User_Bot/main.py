from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from time import sleep
from random import randint

app = Client("my_account")
REPLACEMENT_MAP = {"a": "ɐ", "b": "q", "c": "ɔ", "d": "p", "e": "ǝ", "f": "ɟ", "g": "ƃ", "h": "ɥ", "i": "ᴉ", "j": "ɾ",
                   "k": "ʞ", "l": "l", "m": "ɯ", "n": "u", "o": "o", "p": "d", "q": "b", "r": "ɹ", "s": "s", "t": "ʇ",
                   "u": "n", "v": "ʌ", "w": "ʍ", "x": "x", "y": "ʎ", "z": "z", "A": "∀", "B": "B", "C": "Ɔ", "D": "D",
                   "E": "Ǝ", "F": "Ⅎ", "G": "פ", "H": "H", "I": "I", "J": "ſ", "K": "K", "L": "˥", "M": "W", "N": "N",
                   "O": "O", "P": "Ԁ", "Q": "Q", "R": "R", "S": "S", "T": "┴", "U": "∩", "V": "Λ", "W": "M", "X": "X",
                   "Y": "⅄", "Z": "Z", "0": "0", "1": "Ɩ", "2": "ᄅ", "3": "Ɛ", "4": "ㄣ", "5": "ϛ", "6": "9", "7": "ㄥ",
                   "8": "8", "9": "6", ",": "'", ".": "˙", "?": "¿", "!": "¡", '"': ",,", "'": ",", "(": ")", ")": "(",
                   "[": "]", "]": "[", "{": "}", "}": "{", "<": ">", ">": "<", "&": "⅋", "_": "‾",
                   }


# Typing message
@app.on_message(filters.command("type", prefixes=".") & filters.me)
def typing(_, msg):
    i = 0
    while i < 2:
        orig_text = msg.text.split(".type ", maxsplit=1)[1]
        text = orig_text
        tbp = ""  # to be printed
        typing_symbol = "▓"
        i += 1

        while tbp != orig_text:
            try:
                msg.edit(tbp + typing_symbol)
                sleep(0.02)  # 50 ms

                tbp = tbp + text[0]
                text = text[1:]

                msg.edit(tbp)
                sleep(0.05)

            except FloodWait as e:
                sleep(e.x)


# Hack of Pentagon
@app.on_message(filters.command("hack_pentagon", prefixes=".") & filters.me)
def hack_pentagon(_, msg):
    percentage = 0

    while percentage < 100:
        try:
            text = "🙃‍ Hacking Pentagon..." + str(percentage) + "%"
            msg.edit(text)

            percentage += randint(1, 4)
        except FloodWait as e:
            sleep(e.x)
    msg.edit("Пентагон успешно взломан!")


# Hack Area 51
@app.on_message(filters.command("top_secret", prefixes=".") & filters.me)
def hack_UFo(_, msg):
    percentage = 0

    while percentage < 100:
        try:
            text = "👽 Hacking Area 51 in process..." + str(percentage) + "%"
            msg.edit(text)

            percentage += randint(1, 3)
            sleep(0.15)
        except FloodWait as e:
            sleep(e.x)
    msg.edit("🛸 Found secret data about UFO!")


# Hack of ass
@app.on_message(filters.command("hack_ass", prefixes=".") & filters.me)
def hacking_ass(_, msg):
    percentage = 0

    while percentage < 100:
        try:
            text = "🍑 Hacking your ass in process..." + str(percentage) + "%"
            msg.edit(text)

            percentage += randint(1, 3)
            sleep(0.15)
        except FloodWait as e:
            sleep(e.x)
    msg.edit("🔥 Call the firemen, his ass is burnt!")


# Flip words
@app.on_message(filters.command("flip", prefixes=".") & filters.me)
def flip(_, msg):
    text = msg.text.split(".flip", maxsplit=1)[1]
    final_str = ""
    for char in text:
        if char in REPLACEMENT_MAP.keys():
            new_char = REPLACEMENT_MAP[char]
        else:
            new_char = char
        final_str += new_char
    if text != final_str:
        msg.edit(final_str)
    else:
        msg.edit(text)


# Who reads he will die
app.run()
