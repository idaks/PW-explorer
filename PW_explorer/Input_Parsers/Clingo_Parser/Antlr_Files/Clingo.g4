grammar Clingo;

options {
    language = Python3;
}

							//Parser Rules:

clingoOutput: (pw)* OPTIMUM_FOUND? summary ;

pw: 'Answer:' TEXT (fact)* 'Optimization:'? TEXT? ;

fact: TEXT ('(' fact_content ')')? ;

fact_content: ((fact_text|fact) ',')* (fact_text|fact) ;

fact_text: TEXT ;

summary: models optimum? optimization? calls time cpuTime ;

models: 'Models' ':' TEXT '+'?;

optimum: 'Optimum' ':' TEXT ;

optimization: 'Optimization' ':' TEXT ;

calls: 'Calls' ':' TEXT ;

time: (TEXT | '(' | ')' | ':')+ ;

cpuTime: (TEXT | '(' | ')' | ':')+ ;


						//LEXER RULES

OPTIMUM_FOUND: 'OPTIMUM FOUND' | 'UNSATISFIABLE' | 'SATISFIABLE' ; 

TEXT: [a-zA-Z0-9\\_./:\-<>"!=]+ ;

WHITESPACE : ( '\t' | ' ' | '\r' | '\n'| '\u000C' )+ -> skip ;