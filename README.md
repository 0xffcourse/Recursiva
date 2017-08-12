# Recursiva

Inspired by Dennis Mitchell's Jelly (and other languages made by guys in codegolf.stackexchange), Recursiva is an esolang, based mainly on recursive-approaches (in the making). 

# How to run? 

#### <i>You need python 3 (3.5+ recommended) to run the interpreter. REPL might need few modifications for non-windows platform</i> 

  1. Just Fire `python RecursivaInterpreter.py` to start the REPL.


# Play around with basic commands:
    
The expressions are (as of now) pre-fix evaluated.  

Some Operators that take 1-argument:

    ~: MinusOne
    S: Square 

Some Operators that take 2-arguments:

    Order of operands to be taken is from L to R. So 4 5- will mean 4- 5 and not  5- 4

    +: Plus 
    -: Minus
    *: Multiply
    /: Divide
    =: Check if equal
    >:greater than
    <:less than
    &: Logical And
    |: Logical Or
    %: modular
    
    To calculate (7)^2-1, use:
    >> ~S7 

    [Note: Literals are tokenized in a way that no whitespace is required to separate them from atoms]
    
    To add 4 and -4(negative integer) use:
    >> +4-4
    
    [Note: Negative integers should be written in such a way that the negative sign immediately follows the number part, This is to avoid the ambiguity between - sign and - operator]


    To caclculate (((7-1)^2)-1)^2-1, use:
    >> ~ S  ~ S ~  7

    [Note: Arbitrary whitespaces are allowed (except within same-literal, which would make it two separate literals)]


    To calculate ((4+6)*2)^2-1
    >> ~S*2+4 6
    
# Function-like structure:

Let's say you want to create a function-like structure, to which just editing the parameters will save your time from writing the whole statement over and over. This is possible. The basic function-like feature in recursiva is given as:

    [statement_with_variables]@[argument_1]<whitespace>[argument_2]<whitespace>..........
    
The valid variables are lower case a-z, you cacn start from any alphabet but the rest alphabet must be selected in a consecutive manner such that, they go hand to hand with the order in which arguments are passed. This is confusing, an example might help:

For example you want a function that difference of squares of two numbers:

    >> -SmSn@4 5
    
## The above statement will evaluate as -9. Why?
    
Here m and n are variables, and 4 and 5 are arguments to the function. The first argument will be assigned to the lowest alphabet (i.e. m is assigned with 4, n is assigned to 5). The equivalent statement after assignment will be:

    >> -S4S5
    
And since the subtraction is done from left argument to right argument. This will be -9.

If your intention was to subtract (4)^2 from (5)^2, you could have done either:

    >> -SmSn@5 4
    
OR:

    >> -SnSm@4 5
    

# Conditionals:

The basic conditional statement structure is:

    [condition1]:[if_statement]![else_statement]

For example, this function returns 1 for x less than 5, otherwise 100:

    >> <a 5:1!100@4
    
    will output:
    >> 1
    
    While:
    
    >> <a 5:1!100@5
    
    will output:
    >> 100

### Nesting conditionals is possible, though very very confusing:
For example, this will evaluate to 1 for argument less than or equal to 50, 2 for argument less than 75 and 3 for argument more than or equal to 75.

    >> >a 50:<a 75:2!3!1@[number_argument]
    
# Recursive functions:

If you have the grasp of the conditionals and function-like features in recursiva, you can write recursive functions in Recursiva(Well, what would be the essence of the name if it couldn't have been done, right? :D).

## Note: '#...$' acts as a marker for a recursive function call.  

A function that calculates sum of n-natural numbers is written in recursiva as follows:

    >> =a 1:1!+#~a$a@[number_argument]
    
## How the fuck does it even work?

For 1 (edge-case), the statement will be as:

    >> =1 1:1!+#1~$1
    
Here, the condition passes, so we evaluate 1(stopping the recursion). Of course, sum of 1-natural number is 1. 

Let's say we pass number 4 to the function, the expected value is 10 (i.e. 4+3+2+1)

    >> =a 1:1!+#a~$a@4
    
    This will be parsed as:
    
    >> =4 1:1!+#4~$4@4

First of all, the condition fails, so we execute the else part which is recursive(because of the #...$). Notice the part #4~$ This is where the magic happens. This will of course, evaluate to #3$. What does it mean?? This means "make the same function call but this time with 3 as the argument". Eventually after further recursion the 3$ will certainly evaluate to f(3) i.e. 6. Thus resulting statement will be something like: 

    >> =4 1:1!+6 4
    
    which is of course, 10.
    
# Challenges:

A few problems to sharpen your Recursiva skills.

1. Write a function in recursiva that commputes factorial for a given number.
2. Write a function in recursiva that outputs the n-th fibonacci number for a given number n.
