#  The start of the program
#  Where input is processed
#  All the parts of the code are in one file, decresing scalability, but increasing robustness for this project, since it is relatively small
#  Read arguements from the terminal on Mac and the Command line on Windows 


import sys
from parse import parser
from minimized import minimizer
from display import show_pla 

def main()
  # Used to parse the input, minimze logic, write the output 

in_file = "test_case/input.pla"
out_file = "output.pla"

#parse the input 
data = parse(in_file)
print(f"Parsed Data: {data}")

#Minimize logic with QM
minimize_logic = minimizer(data)
print(f"Minimized logic using Quine-McCluskey: {minimizer}")

# write the now minimized logic in PLA format to the output file 
show(out_file, minimize_logic)
print(f"Output written to {out_file}")

if __name__ = "__main__"
  main()
