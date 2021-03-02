

compas_pointer='north' 
coordinates=[0,0]   



def input_parser(inp_string):
	
    commands = inp_string.split(",")
    return commands
    

          
def commands_validator(commands):
    
    # The return Array. Default value is success
 	ret_array=[0,"Validation Success"]
 	# Loop through each command
 	for i in range(len(commands)):
 	    # Check if command length is 2. If not sets an error
 	    if( not(len(commands[i])==2)):
 	        ret_array[0]=1
 	        ret_array[1]=" invalid command '"+commands[i]+"' at position :"+str(i)+""
 	        break
 	    # Check if commands first letter is either 'F','B','R' or'L'. If not sets an errir
 	    if( not(commands[i][0] in ['F','B','R','L']) ):
 	        ret_array[0]=1
 	        ret_array[1]=" invalid command '"+commands[i]+"' at position :"+str(i)+""
 	        break
 	    #Check if command first letter is R or L
 	    if(commands[i][0] in ['R','L']):
 	        # Check if the command is R1 or L1. If not sets an error
 	        if(not (commands[i] in ['R1','L1'])):
 	            ret_array[0]=1
 	            ret_array[1]=" invalid command '"+commands[i]+"' at position :"+str(i)+""
 	            break
 	    # Check if the second letter of the command is numeric . If not sets an error  
 	    if(not (commands[i][1].isnumeric())):
 	        ret_array[0]=1
 	        ret_array[1]=" invalid command '"+commands[i]+"' at position :"+str(i)+""
 	        break



 	return ret_array

def move_robot(inp_string):
    global coordinates
    global compas_pointer
    # Robot move forward 
    if(inp_string[0]=='F'):
        if(compas_pointer=='east'):
            coordinates=[coordinates[0]+int(inp_string[1]),coordinates[1]]
        elif(compas_pointer=='west'):
            coordinates=[coordinates[0]-int(inp_string[1]),coordinates[1]]
        elif(compas_pointer=='north'):
            coordinates=[coordinates[0],coordinates[1]+int(inp_string[1])]
        elif(compas_pointer=='south'):
            coordinates=[coordinates[0],coordinates[1]-int(inp_string[1])]
    # Robot move backward 
    if(inp_string[0]=='B'):
        if(compas_pointer=='east'):
            coordinates=[coordinates[0]-int(inp_string[1]),coordinates[1]]
        elif(compas_pointer=='west'):
            coordinates=[coordinates[0]+int(inp_string[1]),coordinates[1]]
        elif(compas_pointer=='north'):
            coordinates=[coordinates[0],coordinates[1]-int(inp_string[1])]
        elif(compas_pointer=='south'):
            coordinates=[coordinates[0],coordinates[1]+int(inp_string[1])]  
    # Robot change the direction to right 
    if(inp_string[0]=='R'):
        if(compas_pointer=='north'):
            compas_pointer='east'
        elif(compas_pointer=='east'):
            compas_pointer='south'          
        elif(compas_pointer=='south'):
            compas_pointer='west'
        elif(compas_pointer=='west'):
            compas_pointer='north'   
    # Robot change the direction to left
    if(inp_string[0]=='L'):
        if(compas_pointer=='north'):
            compas_pointer='west'
        elif(compas_pointer=='west'):
            compas_pointer='south'          
        elif(compas_pointer=='south'):
            compas_pointer='east'
        elif(compas_pointer=='east'):
            compas_pointer='north'

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
    ret_array=commands_validator(commands) # Validating Input
    if(ret_array[0]==1):
        print(ret_array[1])
        print('----------------')
        continue
    for i in range(len(commands)):
        move_robot(commands[i]) # Robot Moving

        
    print("Minimum Distance = "+ str(coordinates[0]+coordinates[1]))
    break


print('Thank you')
        
    

