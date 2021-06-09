#This will convert numbers to numbers in words
number = input('Please Enter your number: ')
digit = {
"1": "one",
"2": "two",
"3": "three",
"4": "four"
}
output = ""
for ch in number:
    output += digit.get(ch, "!") + " "
print(output)
