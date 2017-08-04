# Recursiva

An esolang, based mainly on recursive-approaches (in the making)

# How to run? 

#### <i>You need python (3.5+ recommended) to run the interpreter. REPL might need few modifications for non-windows platform</i> 

  1. Just Fire `python RecursivaInterpreter.py` to start the REPL.


# Play around with basic commands:
    
    The expressions are really fix-agnostic i.e. any operation is done immediately once a matching number of operands for a current         operator is found, otherwise, operator will stay in the stack.  

    Some Operators that take 1-argument:
    
    ¬: MinusOne
    S: Square
    R: List of n-natural numbers
    r: List of n-natural numbers (n excluded)

    Some Operators that take 2-arguments:

    +: Plus 
    -: Minus
    *: Multiply
    /: Divide
    =: Compare
    &: Logical And
    |: Logical Or
    

    To calculate (7)^2-1, use:
    >>7S¬ 

    [Note: Literals are tokenized in a way that no whitespace is required to separate them from atoms]


    To caclculate (((7-1)^2)-1)^2-1, use:
    >>7 ¬  S ¬ S ¬  

    [Note: Arbitrary whitespaces are allowed (except within same-literal, which would make it two separate literals)]


    To calculate ((4+6)*2)^2-1
    >>4 6+2*S¬

    ##Conditionals: 
