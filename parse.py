
# We need to parse the input so the program can understand and use the input 
def parse(file_path): 

  # An array for the minterms binary numbers 
    minterms = []
  # An array for the minterms dont care terms that are usually marked by a "-" marker
    dont_cares = []

# We open the file path to the test case 
 with open(file_path, "r") as file: 
   for line in file: 
     # this is to skip any comments potentially made in the file and metadata lines 
     if line.startswith(".") or line.strip() == "": 
       continue 
    # We must parse the input-output pairs 
    parts = line.srip().split()
    if parts[1] == "1":
      minterms.append(parts[0])
    elif parts[1] == "-": 
      dont_care.append(parts[0])

return {"MIN terms": minterms, "DC terms": dont_cares}
