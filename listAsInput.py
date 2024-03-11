# n = input("Enter a text of number: ")

# list = n. split()
# sum = 0

# for num in list:
#     sum = sum + int(num)
    
# print(sum)

numOfWords = 0
numOfLetters = 0
numOfDigits = 0


text  = input("Enter a text of Numbers: ") #My name is Arafat 

for x in text:
    x = x.lower()
    if x >= 'a' and x<='z':
        numOfLetters = numOfLetters + 1
        
    elif x >= '0' and x<='9':
        numOfDigits = numOfDigits + 1
        
    elif x == ' ':
        numOfWords = numOfWords + 1
        
print("Number of letter: ",numOfLetters)
print("Number of digits",numOfDigits)
print("Number of words",numOfWords)