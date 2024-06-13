# 1. Mine:
# file = open("data.txt", 'w')
# file.write("100.12" + "\n")
# file.write("111.23" + "\n")
# file.close()
# file = open("data.txt", 'r')
# read = file.read()
# print(read)
# file.close()

# Theirs:
# file = open("data.txt", 'w')
#
# file.write("100.12\n")
# file.write("111.23\n")
#
# file.close()

# 2. Mine identical to theirs:
file = open("data.txt", 'w')
file.write("100.12")
file.close()
