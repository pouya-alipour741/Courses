command = input("> ")
words = command.split(" ")
emoji= {
    ":)": "\U0001F642",
    ":(": "\U0001F625"
}
output = ""
for word in words:
    output += emoji.get(word, word) + " "
print(output)


