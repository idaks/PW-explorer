grammar Clingo;

options {
    language = Python2;
}

							//Parser Rules:

clingoOutput: (solution)* OPTIMUM_FOUND? summary ;

solution: 'Answer:' TEXT (actual_soln)* 'Optimization:' TEXT ;

actual_soln: TEXT '(' custom_representation_soln ')' ;

custom_representation_soln: TEXT ;

summary: models optimum? optimization? calls time cpuTime ;

models: 'Models' ':' TEXT ;

optimum: 'Optimum' ':' TEXT ;

optimization: 'Optimization' ':' TEXT ;

calls: 'Calls' ':' TEXT ;

time: (TEXT | '(' | ')' | ':')+ ;

cpuTime: (TEXT | '(' | ')' | ':')+ ;


						//LEXER RULES

OPTIMUM_FOUND: 'OPTIMUM FOUND' | 'UNSATISFIABLE' ; 

TEXT: [a-zA-Z0-9\\_.,:-]+ ;

WHITESPACE : ( '\t' | ' ' | '\r' | '\n'| '\u000C' )+ -> skip ;





				//Unused Variable from past versions:

//OPTIMUM_FOUND_OR_NOT: 'yes' | 'no' ;

//SPACE: [ \t] ;

//NEWLINE: '\r'? '\n' ;

//TEXT: [a-zA-Z0-9\\_]+ ;

//TEXT: ('A'..'Z'|'a'..'z'|'0'..'9'|':'|'\\'|'/'|'-'|'_'|'.')+ ;

//STUFF: (TEXT)+ ;

//models: 'Models' (SPACE)+ ':' (SPACE)* NUM_MODELS ;

//optium: (SPACE)+ 'Optium' (SPACE)+ OPTIUM_FOUND_OR_NOT ;

//optimization: 'Optimization' (SPACE)+ ':' (SPACE)* OPTIMAL_SOLN ;

//calls: 'Calls' (SPACE)+ ':' (SPACE)* NUM_CALLS ;

//time: 'Time' ':' TEXT '(' TEXT ')' ;

//cpuTime: 'CPU Time' ':' TEXT ;

//might have to come from the input file??
//solution: 'Answer:' ANS_NUM (NEWLINE) actual_soln (NEWLINE) 'Optimization:' CURR_SOLN ;

//custom_representation_soln: (TEXT ',')* TEXT ;

//NUM_MODELS: NUMBER ;

//OPTIMAL_SOLN: NUMBER ;

//NUM_CALLS: NUMBER ;

//ANS_NUM: NUMBER ;

//CURR_SOLN: NUMBER ;

//NUMBER: [0-9]+ ;

//NUMBER: ('0'..'9')+ ;

//RELATION_NAME: TEXT ;
