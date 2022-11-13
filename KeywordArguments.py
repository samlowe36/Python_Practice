def greet_user(first_name, last_name):
    print(f"Hi there {first_name} {last_name}!")
    print("Welcome aboard!")
#defines and stores the code as a function called greet_user
#gives name parameter to function so it can be called with a unique name easily


print("Start")
greet_user(last_name="Smith", first_name="John")
greet_user(last_name="Smith", first_name="Mary")
print("Finish")



#will give error if there is no argument (or value) for the parameter

#keyword arguments like above make it so the order of the arguments does not matter since the correct values are still assigned to first and last name
#keyword arguments also help with readability of code
#if mixing positional and keyword arguments, position MUST be first or you will get an error