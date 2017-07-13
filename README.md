# Recursiva

An esolang, based mainly on recursive-approaches (in the making)

# How to run? 

  1. Just Fire `python Recursiva.py` to start the REPL. Or,

  2. If you are on windows:

    a. Set RECURSIVA_ENV to the folderpath containing the RecursivaInterpreter.py, Recursiva.py(REPL) and 
       recursiva.bat(batch file).
  
    b. Add '%RECURSIVA_ENV%' to the Path variable  
  
    c. Now typing `recursiva` in the command line anywhere will run the REPL.   

# Play around with basic commands:

AS of now only few monadic atoms like ¬(minus one) and S(square) are available. The operations are basically postfix.

To calculate (7)^2-1, use:
>>¬S7 

[Note: Literals are tokenized in a way that no whitespace is required to separate them from atoms]

To caclculate (((7-1)^2)-1)^2-1, use:
>>¬	S	¬ S ¬ 7    

[Note: Arbitrary whitespaces are allowed (except in literals)]
