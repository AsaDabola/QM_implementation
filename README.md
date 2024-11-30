# QM_implementation
An implementation of the Quine McCluskey method 

This assignment has the implemented code of the Quine McCluskey method

From the beginning of this project, there were many challenges such as, figuring out how to actually implement the code. 
With the help of the internet and AI, I was able to get clues as to how to start structuring the code files for this project. 

Many of the challenges were understanding how Quine McCluskey would function. 

Here is a brief breakdown of the project approach: 

1.  Making sure that the input could be taken as a BLIF/PLA file, by parsing and validation, so that the output is the minimized Logic in PLA format
   - Pyhton has libraries for parsing and manipulation, and is one of the easier languages to implement, hence why it was chosen. 
3. We must understand the Prime implicant table in Quine McCulskey and how it is able to find prime implicants.
4. Understand file parsing libraries such as pyparsing, which help verify inputs. 
5. The code must be tested and verified with a handful of random testcases


Challenges Faced: 
1.  BLIF parsing is much more difficult than PLA, since it supports sequential logic as well, hence why I decided to stick soley to PLA format for simplicity. 
2.  QM cannot handle larger sets well, so if planning to scale, would need to adjust code for that
3.  Visualizing the Karnaugh Maps for QM as the inbetween process is very challenging





