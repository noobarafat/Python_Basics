phone = input("Phone: ")

digitMapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}

output = ''
for ch in phone:
    output += digitMapping.get(ch, '!') + " "

print(output,"!")