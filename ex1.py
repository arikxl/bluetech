fileName = input('What is the file name? ')
content = input('What is the file content? ')


with open(fileName, 'w') as file:
    file.write(content)