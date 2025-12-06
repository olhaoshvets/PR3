# Task 1
from os.path import split

word = 'PyTHon'

firstLastLetter = word[0] + word[-1]
print(firstLastLetter)

upperCase = word.upper()
print(upperCase)

lowerCase = word.lower()
print(lowerCase)

capitalize = word.capitalize()
print(capitalize)

twoLetters = word[2:4]
print(twoLetters)

# Task 2
text = 'Hello World'

length = len(text)
print('The text length is:', length)

# Task 3
text = '''
Never gonna give you up, never gonna let you down
Never gonna run around and desert you
Never gonna make you cry, never gonna say goodbye
Never gonna tell a lie and hurt you
'''

specificWordCount = text.lower().count('never')
print('The word "never" meets in the text', specificWordCount, 'times.')

# Task 4
text = 'Text'
number = '1320'

isString = text.isalpha()
isNumber = number.isdigit()

print(isString, isNumber)

# Task 5
text = 'I love cats'

replaceWord = text.replace('cats', 'dogs')
print(replaceWord)

# Task 6
textAnalyzer = input()

charCount = len(textAnalyzer) - textAnalyzer.count(' ')
if charCount == 1:
    print('The text contains',charCount, 'character.')
else:
    print('The text contains',charCount, 'characters.')

wordCount = textAnalyzer.count(' ') + 1
if wordCount == 1:
    print('The text contains', wordCount, 'word.')
else:
    print('The text contains', wordCount, 'words.')

upperLowerCases = textAnalyzer.lower(), textAnalyzer.upper()
print(upperLowerCases)

replaceChar = textAnalyzer.replace(' ', '_')

# Task 7
row = '123-456-789'

findPlacement = row.find('-')
print('The index of the first - is', findPlacement)

# Task 8
email = 'email: user@example.com'

emailSplit = email.split()
emailSplit = (emailSplit[1])
print('Extracted with split:', emailSplit)

emailStrip = email.lstrip('email: ')
print('Extracted with strip:', emailStrip)

# Task 9
textInput = 'Hello, your id number is 32'

isNumberPresent = any(textInput.isdigit() for textInput in textInput)
if isNumberPresent:
    print('The text contains a number.')
else:
    print('The text does not contain a number.')

# Task 10 replaced agent with James to make it more fun :)
agent = 'qwertyjamesbondqazwsx'

findNameIndexStart = agent.find('j')
findNameIndexEnd = agent.rfind('b')
name = agent[findNameIndexStart:findNameIndexEnd].capitalize()

findSurnameIndexStart = agent.find('b')
findSurnameIndexEnd = agent.rfind('q')
surname = agent[findSurnameIndexStart:findSurnameIndexEnd].capitalize()
print('My name is', surname + ',', name, surname)