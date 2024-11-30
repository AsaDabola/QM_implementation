# Final output of the function

# def show_pla(output_path, minimized_logic): 
def show_pla(output_path, minimized_logic, num_inputs, num_ouputs)
  # Simple code to display the PLA file 
  with open(output_path, "w") as file: 
    file.write(f".i {num_inputs}\n") 
    file.write(f".o {num_ouputs}\n")
    for term in minimized_logic
      file.write(f"{term} 1\n")
    file.write(".e\n") # PLA file ending
    # num_inputs = int(input().strip())
    # num_outputs = int(input().strip())

  
