# Recipe - local vars are not directly available in the rest of your code,
# like message/new_message.
def greet():
    message = "hello"
    new_message = message.capitalize()
    # The function can't work without a return and will return None:
    return new_message


#  You also have to assign it to a variable(greeting in this case)
#  in order to use the function. This is known as a function call:
greeting = greet()
# You still need to do something with the function in order for it to be executed:
print(greeting)
# You can now do other things with the output of the function like get length:
print(len(greeting))
