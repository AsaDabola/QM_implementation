#  The start of the program
#  Where input is processed
#  All the parts of the code are in one file, decresing scalability, but increasing robustness for this project, since it is relatively small
#  Read arguements from the terminal on Mac and the Command line on Windows 

# import sys  for terminal use?
from parse import parser
from minimized import minimizer
from display import show_pla 

def main():
  # Used to parse the input, minimze logic, write the output 
  in_file = "test_case/input.pla"
  out_file = "output.pla"

  #parse the input 
  data = parse(in_file)
  print(f"Parsed Data: {data}")

  # get the inputs from the file test cases
  inputs = data["inputs"]
  outputs = data["outputs"]

  #Minimize logic with QM
  minimized_logic = minimizer(data)
  print(f"Minimized logic using Quine-McCluskey: {minimizer}")

  # write the now minimized logic in PLA format to the output file 
  show_pla(out_file, minimized_logic, inputs, outputs)
  print(f"Output written to : {out_file}")

  if __name__ = "__main__":
    main()
