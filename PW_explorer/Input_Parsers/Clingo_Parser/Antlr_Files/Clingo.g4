grammar Clingo;

options {
    language = Python2;
}

							//Parser Rules:

clingoOutput: (solution)* OPTIMUM_FOUND? summary ;

solution: 'Answer:' TEXT (actual_soln)* 'Optimization:'? TEXT? ;

actual_soln: TEXT+ '(' custom_representation_soln ')' ;

custom_representation_soln: TEXT ;

summary: models optimum? optimization? calls time cpuTime ;

models: 'Models' ':' TEXT '+'?;

optimum: 'Optimum' ':' TEXT ;

optimization: 'Optimization' ':' TEXT ;

calls: 'Calls' ':' TEXT ;

time: (TEXT | '(' | ')' | ':')+ ;

cpuTime: (TEXT | '(' | ')' | ':')+ ;


						//LEXER RULES

OPTIMUM_FOUND: 'OPTIMUM FOUND' | 'UNSATISFIABLE' | 'SATISFIABLE' ; 

TEXT: [a-zA-Z0-9\\_.,/:\-<>"!=]+ ;

WHITESPACE : ( '\t' | ' ' | '\r' | '\n'| '\u000C' )+ -> skip ;