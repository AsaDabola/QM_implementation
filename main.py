
import os
import argparse
from parse import parser
from minimized import minimizer
from display import show_pla 

def main():
  # Used to parse the input, minimze logic, write the output 

  # Collect the input and ouput count from the testcase file 
  in_file = args.in_file
  out_file = args.out_file

  # Check if the file actually exists 
  if not os.path.exists(in_file):
    print(f"Error: The input file {in_file} does not exist :( ")
    return

  #parse the inputs 
  data = parser(in_file)
  print(f"Parsed Data: {data}")

  # Get the inputs from the file test cases
  inputs = data["inputs"]
  outputs = data["outputs"]

  # Minimize logic with QM
  minimized_logic = minimizer(data)
  print(f"Minimized logic using Quine-McCluskey: {minimized_logic}")

  # Write the now minimized logic in PLA format to the output file 
  show_pla(out_file, minimized_logic, inputs, outputs)
  print(f"Output written to : {out_file}")

if __name__ == "__main__":
    main()
