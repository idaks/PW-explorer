grammar Telingo_Output;

options {
    language = Python3;
}

							//Parser Rules:

telingoOutput: (pw)* OPTIMUM_FOUND? summary ;

pw: 'Answer:' TEXT (state_desc)* 'Optimization:'? TEXT? ;

state_desc: 'State' TEXT (fact)* ;

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