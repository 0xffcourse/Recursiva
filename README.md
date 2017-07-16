# Recursiva

An esolang, based mainly on recursive-approaches (in the making)

# How to run? 

#### <i>You need python (3.5+ recommended) to run the interpreter. REPL might need few modifications for non-windows platform</i> 

  1. Just Fire `python Recursiva.py` to start the REPL. Or,

  2. Follow these steps

    a. Set RECURSIVA_ENV to the folderpath containing the RecursivaInterpreter.py, Recursiva.py(REPL) and 
       recursiva.bat(batch file).
  
    b. Add '%RECURSIVA_ENV%' to the Path variable  
  
    c. Now typing `recursiva` in the command line anywhere will run the REPL.   

# Play around with basic commands:
    
    Operators that take 1-argument:
    
    ¬: MinusOne
    S: Square
    R: List of n-natural numbers
    r: List of n-natural numbers (n excluded)

    Operators that take 2-arguments:

    +: Plus 
    -: Minus
    *: Multiply
    /: Divide
    

To calculate (7)^2-1, use:
>>¬S7 

[Note: Literals are tokenized in a way that no whitespace is required to separate them from atoms]


To caclculate (((7-1)^2)-1)^2-1, use:
>>¬	S	¬ S ¬ 7    

[Note: Arbitrary whitespaces are allowed (except within same-literal, which would make it two separate literals)]


To calculate ((4+6)*2)^2-1
>>¬S*2 + 4 6

This would also work for ((4+6)*2)^2-1 [Though not purely pre-fix]
>>¬S*2 4+6

Or this:
>>¬S2* 4+6