grammar Clingo;

//Parser Rules:

options {
    language = Python2;
}


clingoOutput: (solution)* OPTIUM_FOUND? summary ;

summary: models optium optimization calls time cpuTime ;

//models: 'Models' (SPACE)+ ':' (SPACE)* NUM_MODELS ;
models: 'Models' ':' NUM_MODELS ;

//optium: (SPACE)+ 'Optium' (SPACE)+ OPTIUM_FOUND_OR_NOT ;
optium: 'Optium' OPTIUM_FOUND_OR_NOT ;

//optimization: 'Optimization' (SPACE)+ ':' (SPACE)* OPTIMAL_SOLN ;
optimization: 'Optimization' ':' OPTIMAL_SOLN ;

//calls: 'Calls' (SPACE)+ ':' (SPACE)* NUM_CALLS ;
calls: 'Calls' ':' NUM_CALLS ;

time: TEXT ;

cpuTime: TEXT ;

//might have to come from the input file??
//solution: 'Answer:' ANS_NUM (NEWLINE) actual_soln (NEWLINE) 'Optimization:' CURR_SOLN ;
solution: 'Answer:' ANS_NUM actual_soln 'Optimization:' CURR_SOLN ;

actual_soln: (RELATION_NAME '(' custom_representation_soln ')')* ;

custom_representation_soln: (Word ',')* Word ;

//LEXER RULES

NUM_MODELS: NUMBER ;

OPTIUM_FOUND_OR_NOT: 'yes' | 'no' ;

OPTIMAL_SOLN: NUMBER ;

NUM_CALLS: NUMBER ;

TEXT: [a-zA-Z0-9\\_.]+ ;

fragment NUMBER: [0-9]+ ;

//SPACE: [ \t] ;

//NEWLINE: '\r'? '\n' ;

Word: [a-zA-Z0-9\\_]+ ;

WHITESPACE : ( '\t' | ' ' | '\r' | '\n'| '\u000C' )+ -> skip ;

ANS_NUM: NUMBER ;

CURR_SOLN: NUMBER ;

RELATION_NAME: Word ;

OPTIUM_FOUND: 'OPTIUM FOUND' ;

//STUFF: (TEXT)+ ;
