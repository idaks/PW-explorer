grammar DLV_Out;

options {
    language = Python3;
}


// Parser Rules

dlvOutput: (pws_out | wf_mode_out | optimization_out)?;

pws_out: (pw)* ;

pw: atom_set;

wf_mode_out: (true_part)? (undefined_part)?;

optimization_out: (opt_model)+;

opt_model: 'Best model:' atom_set 'Cost ([Weight:Level]):' '<[' TEXT ']>';

true_part: 'True:' atom_set;

undefined_part: 'Undefined:' atom_set;

atom_set: '{' ((atom ',')* atom)? '}';

// atom: TEXT+ ('(' TEXT ')')? ;
atom: TEXT ('(' atom_content ')')? ;

atom_content: ((atom_text|atom) ',')* (atom_text|atom) ;

atom_text: TEXT ;


// Lexer Rules

// TEXT: [a-zA-Z0-9\\_.,/:\-<>"!=]+ ;
TEXT: [a-zA-Z0-9\\_./:\-<>"!=]+ ;

WHITESPACE : ( '\t' | ' ' | '\r' | '\n'| '\u000C' )+ -> skip ;