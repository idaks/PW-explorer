grammar Dlv;

options {
    language = Python2;
}
                            //Parser Rules:
dlvOutput : solution* ;
solution : '{' atoms '}' ;

atoms : ( atom (',' atom)* ) ;

atom : atom_name atom_vals? ;

atom_vals : '(' val (',' val)* ')' ;

val : TEXT ;
atom_name : TEXT ;

    //Lexer Rules:
TEXT: [a-zA-Z0-9!"#$%&'*+-./:;<=>?@^_`|~]+ ;
WS : [ \t\r\n]+ -> skip;
