To execute:
*Tested using Python 3.8.5 
*To run the program 
	Open CLI --> Go to the folder containing the program file.
	Run the command "python program.py"
*Or can simply execute it online using JupytrLab.


Assumptions:
* Robot can turn only 90 degrees at a time which means for right and left commands the only allowed value is 1. For example, R1,L1 values are valid, but R2,R3 etc are invalid.
* When robot traverses either directions of negative axes, make the value positive.
* While calculating the minimum distance, as the robot moves in 90 degrees sum up both the axes cordinate values.


Limitation:
* Units range from 0-9. For example, F1,B9,F9 are valid. Whereas, F10,F11 are invalid.
