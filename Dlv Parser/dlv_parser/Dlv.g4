grammar Dlv;

options {
    language = Python2;
}
                            //Parser Rules:
//solution : ( '{' atoms '}' )+ ; 
solution : '{' atoms (',' atoms)* '}' ;

atoms : atom atom_vals ;

atom_vals : '(' val (',' val)* ')' ;

val : TEXT ;
atom: TEXT ;

    //Lexer Rules:
TEXT: [a-zA-Z0-9_]+ ;
WS : [ \t\r\n]+ -> skip;
