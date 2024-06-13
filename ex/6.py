#Reading absolute paths from from external sources/files are done like this:

#On windows (the r in the front makes it a raw path which ignores characters like \n(newLine) or \t(tab):
#file = open(r'C:\Users\FrederickBredenkamp\downloads\todos.txt', 'r')

#on mac/linux:
#file = open('/Users/FrederickBredenkamp/downloads/todos.txt', 'r')

# ex1:
# file = open("bear.txt",'r')
# content = file.read()
# print(content)

# ex 2:
# file = open("essay.txt", 'r')
# content = file.read().title()
# print(content)

# ex 3:
# file = open("essay.txt", 'r')
# content = len(file.read())
# print(content)

# ex4:
# file = open("file.txt", 'w')
# file.writelines("snail")
# file.close()

# ex5:
# Please code this exercise in your computer IDE. For this exercise, download the members.txt file attached to the resources. Then, create a program that:
# 1. prompts the user to enter a new member.
# 2. adds that member to members.txt at the end of the existing members. For example, the user here has entered the member Solomon Right.
# In the above example, Solomon Right will be added to members.txt updating the content of the file to:
# John Smith
# Sen Lakmi
# Sono Octonot
# Solomon Right

# prompt = input("Please write your name: ")
# file = open("members.txt", 'r')
# names = file.readlines()
# file.close()
# names.append(f"{prompt.title()}\n")
# file = open('members.txt', 'w')
# file.writelines(names)
# file.close()
# print(names)

# ex6:
# Open your computer IDE and place the following in a Python file:
# filenames = ['doc.txt', 'report.txt', 'presentation.txt']
# Then, create a program that:
# 1. generates multiple text files by iterating over the filenames list,
# 2. and writes the text Hello  inside each generated text file.

# filenames = ['doc.txt', 'report.txt', 'presentation.txt']
# for filename in filenames:
#     file = open(filename, 'w')
#     file.writelines("Hello")
#     file.close()

# ex7:
filenames = ['a.txt', 'b.txt', 'c.txt']
for filename in filenames:
    file = open(filename, 'r')
    content = file.read()
    print(content)
    file.close()
