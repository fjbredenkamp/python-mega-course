#types

#you can multiply a string, but not add:

a = '10'
a + 1

#this will throw and error

#but this won't:

a * 10

#will print out:
'10101010101010101010' #10 a's'

 #you can convert a string to an int like this

 a = int('10')

 #so now a + 1 will equal 11

 #you can't convert normal strings into int or float

 int('Hi')
 float('hi')

 #will throw an error

 float("10")
 #shows 10.0

int("10")
#shows 10

my_list = ['a', 'b', 'c']
dir(my_list)
#you can use python methods directly like this:
my_list.__setitem__(1, 'd')
#that will change the list to:
#['a', 'd', 'c']
#but that is not needed and can be written this way:
mylist[1] = 'd'
#which means change mylist at index 1 to 'd'