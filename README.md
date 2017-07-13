# Recursiva

An esolang, based mainly on recursive-approaches (in the making)

# How to run? 

Just Fire `python Recursiva.py` to start the REPL. Or,

#Play around with basic commands:

AS of now only few monadic atoms like ¬(minus one) and S(square) are available. The operations are basically postfix.

To calculate (7)^2-1, use:
>>¬S7 
=>48

[Note: Literals are tokenized in a way that no whitespace is required to separate them from atoms]

To caclculate (((7-1)^2)-1)^2-1, use:
>>¬	S	¬ S ¬ 7 
=>1224   

[Note: Arbitrary whitespaces are allowed (except in literals)]
