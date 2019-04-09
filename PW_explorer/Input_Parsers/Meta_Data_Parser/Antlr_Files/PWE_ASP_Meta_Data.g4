grammar PWE_ASP_Meta_Data;

options {
    language = Python3;
}


// Parser Rules

aspFile: (comment)* ;

comment: '%'+ meta_data_comment ;

meta_data_comment: (attr_def | temporal_dec | graphviz_styling) ;

attr_def: 'schema' TEXT '(' TEXT+ ')' '.'? ;

temporal_dec: 'temporal' TEXT '(' TEXT+ ')' '.'? ;

graphviz_styling: 'graphviz' (graphviz_graph_dec | graphviz_node_dec | graphviz_edge_dec) ;

graphviz_graph_dec: 'graph' graphviz_graph_style_option* '.'? ;

graphviz_node_dec: 'node' TEXT '(' TEXT+ ')' graphviz_node_style_option* '.'? ;

graphviz_edge_dec: 'edge' TEXT '(' TEXT+ ')' graphviz_edge_style_option* '.'? ;

graphviz_graph_style_option: graphviz_style_option ;

graphviz_node_style_option: graphviz_style_option ;

graphviz_edge_style_option: graphviz_style_option ;

graphviz_style_option:  TEXT '=' TEXT ;

// Lexer Rules

TEXT: [a-zA-Z0-9_"\\<>\-#.:;+'!,?/$]+ ;

WHITESPACE : ( '\t' | ' ' | '\r' | '\n'| '\u000C' )+ -> skip ;

