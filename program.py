

compas_pointer='north' 
coordinates=[0,0]   



def input_parser(inp_string):
	
    commands = inp_string.split(",")
    return commands
    

          



print('Welcome')
print('The robot is currently facing north at position 0,0')
while(True):
    print('Available commands are F<0-9>, B<0-9>,R1,L1 ')
    print("Enter 'q' at any time to quit the program")
    user_input=input('Enter the commands :')
    if(user_input=='q'):
        break
    commands=input_parser(user_input)
    print("commands are:")
    print(commands)
    print("-------------------")


print('Thank you')
        
    

