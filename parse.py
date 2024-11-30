
# We need to parse the input so the program can understand and use the input 
def parser(file_path): 

  # An array for the minterms binary numbers 
    minterms = []
  # An array for the minterms dont care terms that are usually marked by a "-" marker
    dont_cares = []
    inputs = 0 # variable for input 
    outputs = 0 # variable for output 

# We open the file path to the test case 
 with open(file_path, "r") as file: 
   for line in file: 
       line = line.strip()
     if line.startswith(".i"): # get the number of inputs from the file
       inputs = int(line.split()[1])
     elif line.startswith(".o") # get the number of oututs from the file
       outputs = int(line.split()[1])
     # this is to skip any comments potentially made in the file and metadata lines 
     elif line.startswith(".") or line.strip() == "": 
       continue 
     else: 
        # parses the input and output from the file 
        parts = line.srip().split()
        if parts[1] == "1":
          minterms.append(parts[0])
        elif parts[1] == "-": 
          dont_care.append(parts[0])


return {"MIN terms": minterms, "DC terms": dont_cares}
