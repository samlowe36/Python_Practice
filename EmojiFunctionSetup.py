def emoji_converter(message):
    words = message.split(" ")
    emojis = {
        ":)": "😊",
        ":(": "☹",
        ";)": "😉",
        "B)": "😎",
        "surprise": "༼ つ ◕_◕ ༽つ"
    }
    output = ""
    for entry in words:
        output += emojis.get(entry, entry) + " "
    return output


message = input("> ")
print(emoji_converter(message))


#emoji converter program as a function