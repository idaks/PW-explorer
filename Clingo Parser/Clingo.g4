grammar Clingo;

//Parser Rules:

options {
    language = Python3;
}


clingoOutput: (solution)* OPTIUM_FOUND? summary ;

OPTIUM_FOUND: 'OPTIUM FOUND' ;

summary: models optium optimization calls time cpuTime ;

models: 'Models' (SPACE)+ ':' (SPACE)* NUM_MODELS ;

optium: (SPACE)+ 'Optium' (SPACE)+ OPTIUM_FOUND_OR_NOT ; 

OPTIUM_FOUND_OR_NOT: 'yes' | 'no' ;

optimization: 'Optimization' (SPACE)+ ':' (SPACE)* OPTIMAL_SOLN ;

OPTIMAL_SOLN: [0-9]+ ;

calls: 'Calls' (SPACE)+ ':' (SPACE)* NUM_CALLS ;

NUM_CALLS: [0-9]+ ;

time: TEXT ;

cpuTime: TEXT ;

TEXT: [a-zA-Z0-9\\_]+ ;

SPACE: [ \t] ;

NEWLINE: '\r'? '\n' ;

Word: [a-zA-Z0-9\\_]+ ;

WHITESPACE : ( '\t' | ' ' | '\r' | '\n'| '\u000C' )+ -> skip ;

solution: 'Answer:' ANS_NUM (NEWLINE) actual_soln (NEWLINE) 'Optimization:' CURR_SOLN ;

ANS_NUM: [0-9]+ ;

CURR_SOLN: [0-9]+ ;

//might have to come from the input file??

actual_soln: STUFF ;

STUFF: (TEXT)+ ;
