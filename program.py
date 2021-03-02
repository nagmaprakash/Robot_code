'''
This program is to calculate the distance between final destination and starting point.
Executed in Python 3.8.5

'''

compas_pointer='north' # Global.Points to the current direction of the robot.Initial is default 'north'. Will get updated on L and R commands
coordinates=[0,0]   # Global. Saves the coordinates of the robot. Will get updated on F and B commands. 

################INPUT PARSER ###################################################
'''
Input parser parses the input string based on comma.
input : the user input string
output : a list(array) of commands

'''
def input_parser(inp_string):
    
    commands = inp_string.split(",")
    return commands
    
################## Command Validator ##########################################
'''
Command validator validates if the input commands are valid commands or not.
input: A list(array) of commands
output: an array. 0 if all commands are valid. 1 if there is an invalid command.

Valuidations:
1- Check if all commands are having a length of 2 (ex: F3, R1 etc)
2- Check if the first letter of each command is either 'F','B','R' or 'L'
3- if command if either R or L , then check if the second letter is 1.
PS: Since the robot can only turn 90 at a time, we limit the imput to R1,L1. (Ex: R2,R4,L5 etc are invalid )
4- Check if the second letter of each command is numeric.
'''
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
            
######################ROBOT MOVE###############################
'''
The robot move function helps to move the robot depending on each command
input: a single command
output: Nil
'''
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

############### MAIN PROGRAM STARTS #########################

print('Welcome')
print('The robot is currently facing north at position 0,0')
while(True):
    print('Available commands are F<0-9>, B<0-9>,R1,L1 ')
    print("Enter 'q' at any time to quit the program")
    user_input=input('Enter the commands :')
    if(user_input=='q'):
        break
    commands=input_parser(user_input)# Parsing input
    print("commands are:")
    print(commands)
    print("-------------------")
    ret_array=commands_validator(commands) # Validating Input
    if(ret_array[0]==1):
        print(ret_array[1])
        print('----------------')
        continue
    print('Robot moving')
    #Looping through each commands
    for i in range(len(commands)):
        move_robot(commands[i]) # Robot Moving
        print(commands[i]+":direction:"+compas_pointer+" ,Coordinates :"+str(coordinates))
    # Calculating the distance after converting both coordinates into positive values    
    if(coordinates[0]<0):
        coord_x=(coordinates[0]*-1) 
    else: 
        coord_x=coordinates[0]
    if(coordinates[1]<0):
        coord_y=(coordinates[1]*-1) 
    else: 
        coord_y=coordinates[1]
        
    print("Minimum Distance = "+ str(coord_x+coord_y))
    break
print('Thank you')
        
    

