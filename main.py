#  The start of the program
#  Where input is processed
#  All the parts of the code are in one file, decresing scalability, but increasing robustness for this project, since it is relatively small
#  Read arguements from the terminal on Mac and the Command line on Windows 


import sys
from parser import parse
from minimizer import minimized
from utils import show_pla 

def main()
  # Used to parse the input, minimze logic, write the output 

inputFile = "test_case/input.pla"
outputFile = "output.pla"

#parse the input 
data = parse(inputFile)
print(f"Parsed Data: {data}")

#Minimize logic with QM
minimize_logic = minimized(data)
print(f"Minimized logic using Quine-McCluskey: {minimized}")

# write the now minimized logic in PLA format to the output file 
show(outputFile, minimize_logic)
print(f"Output written to {outputFile}")

if __name__ = "__main__"
  main()
