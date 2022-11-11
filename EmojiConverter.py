message = input("> ")
words = message.split(" ") #sets boundaries between strings. this splits them into separate pieces when it finds a space.
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
print(output)