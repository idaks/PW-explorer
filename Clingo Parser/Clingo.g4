grammar Clingo;

//Parser Rules:

options {
    language = Python2;
}


clingoOutput: (solution)* OPTIMUM_FOUND? summary ;

summary: models optimum optimization calls time cpuTime ;

//models: 'Models' (SPACE)+ ':' (SPACE)* NUM_MODELS ;

models: 'Models' ':' TEXT ;

//optium: (SPACE)+ 'Optium' (SPACE)+ OPTIUM_FOUND_OR_NOT ;

optimum: 'Optimum' ':' OPTIMUM_FOUND_OR_NOT ;

//optimization: 'Optimization' (SPACE)+ ':' (SPACE)* OPTIMAL_SOLN ;

optimization: 'Optimization' ':' TEXT ;

//calls: 'Calls' (SPACE)+ ':' (SPACE)* NUM_CALLS ;

calls: 'Calls' ':' TEXT ;

//time: 'Time' ':' TEXT '(' TEXT ')' ;
time: (TEXT | '(' | ')' | ':')+ ;

//cpuTime: 'CPU Time' ':' TEXT ;
cpuTime: (TEXT | '(' | ')' | ':')+ ;

//might have to come from the input file??
//solution: 'Answer:' ANS_NUM (NEWLINE) actual_soln (NEWLINE) 'Optimization:' CURR_SOLN ;

solution: 'Answer:' TEXT actual_soln 'Optimization:' TEXT ;

actual_soln: (TEXT '(' custom_representation_soln ')')* ;

custom_representation_soln: (TEXT ',')* TEXT ;

//LEXER RULES

//NUM_MODELS: NUMBER ;

OPTIMUM_FOUND_OR_NOT: 'yes' | 'no' ;

//OPTIMAL_SOLN: NUMBER ;

//NUM_CALLS: NUMBER ;

//ANS_NUM: NUMBER ;

//CURR_SOLN: NUMBER ;

OPTIMUM_FOUND: 'OPTIMUM FOUND' ;

//NUMBER: [0-9]+ ;

//NUMBER: ('0'..'9')+ ;

//RELATION_NAME: TEXT ;

TEXT: [a-zA-Z0-9\\_.,:]+ ;

WHITESPACE : ( '\t' | ' ' | '\r' | '\n'| '\u000C' )+ -> skip ;

//SPACE: [ \t] ;

//NEWLINE: '\r'? '\n' ;

//TEXT: [a-zA-Z0-9\\_]+ ;

//TEXT: ('A'..'Z'|'a'..'z'|'0'..'9'|':'|'\\'|'/'|'-'|'_'|'.')+ ;

//STUFF: (TEXT)+ ;
