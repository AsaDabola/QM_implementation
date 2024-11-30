# Final PLA output

def show_pla(output_path, minimized_logic, input_count, ouput_count)
  
  # Simple code to display the PLA file 
  with open(output_path, "w") as file: 
    file.write(f".i {input_count}\n") 
    file.write(f".o {output_count}\n")
    
    for term in minimized_logic
      file.write(f"{term} 1\n")
    # PLA file end
    file.write(".e\n") 
    
   
  
