filenames = ["1.Raw Data.txt", "2.Reports.txt", "3.Presentation.txt"]

for filename in filenames:
    filename = filename.replace('.', '-', 1) #this replaces the first ., for each string in the list, with a -
    print(filename) #this prints the new names