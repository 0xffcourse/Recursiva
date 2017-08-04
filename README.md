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

    Order of operands to be taken is from L to R. So 4 5- will mean 4-5 and not  5-4

    +: Plus 
    -: Minus
    *: Multiply
    /: Divide
    =: Check if equal
    >:greater than
    <:less than
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
    
# Function-like structure:

Let's say you want to create a function-like structure, to which just editing the parameters will save your time from writing the whole statement over and over. This is possible. The basic function-like feature in recursiva is given as:

    [statement_with_variables]@[argument_1]<whitespace>[argument_2]<whitespace>..........
    
The valid variables are lower case a-z, you cacn start from any alphabet but the rest alphabet must be selected in a consecutive manner such that, they go hand to hand with the order in which arguments are passed. This is confusing, an example might help:

For example you want a function that difference of squares of two numbers:

    >>mSnS-@4 5
    
## The above statement will evaluate as -9. Why?
    
Here a and b are variables, and 4 and 5 are arguments to the function. The first argument will be assigned to the lowest alphabet (i.e. m is assigned with 4, n is assigned to 5). The equivalent statement after assignment will be:

    >>4S5S-
    
And since the subtraction is done from left argument to right argument. This will be -9.

If your intention was to subtract (4)^2 from (5)^2, you could have done either:

    >>mSnS@5 4
    
OR:

    >>nSmS@4 5
    

# Conditionals:

The basic conditional statement structure is:

    [condition1]:[if_statement]![else_statement]

For example, this function returns 1 for x less than 5, otherwise 100:

    >>a<5:1!100@4
    
    will output:
    >>1
    
    While:
    
    >>a<5:1!100@5
    
    will output:
    >>100

Nesting conditionals is possible, though very very confusing:
For example, this will evaluate to 1 for argument less than or equal to 50, 2 for argument less than 75 and 3 for argument more than or equal to 75.

    >>a>50:a<75:2!3!1@[any_number]
    
# Recursive functions:

It is possible to write recursive functions in Recursiva(Well, what would be the essence of the name if it couldn't have been done, right? :D)


