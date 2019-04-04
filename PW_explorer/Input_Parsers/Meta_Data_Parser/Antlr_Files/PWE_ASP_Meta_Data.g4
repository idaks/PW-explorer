grammar PWE_ASP_Meta_Data;

options {
    language = Python3;
}


// Parser Rules

aspFile: (comment_line)* ;

comment_line: comment+ ;

comment: '%'+ meta_data_comment ;

meta_data_comment: (attr_def | temporal_dec | graphviz_styling) ;

attr_def: 'schema' REL_NAME '(' ATTR_NAME (',' ATTR_NAME)* ')' '.'? ;

temporal_dec: 'temporal' REL_NAME '(' TEMPORAL_ATTR_OPTIONS (',' TEMPORAL_ATTR_OPTIONS)* ')' '.'? ;

graphviz_styling: 'graphviz' (graphviz_graph_dec | graphviz_node_dec | graphviz_edge_dec) ;

graphviz_graph_dec: 'graph' graphviz_graph_style_option+ '.'? ;

graphviz_node_dec: 'node' REL_NAME '(' GRAPHVIZ_NODE_ATTR_OPTIONS (',' GRAPHVIZ_NODE_ATTR_OPTIONS)* ')' graphviz_node_style_option+ '.'? ;

graphviz_edge_dec: 'edge' REL_NAME '(' GRAPHVIZ_EDGE_ATTR_OPTIONS (',' GRAPHVIZ_EDGE_ATTR_OPTIONS)* ')' graphviz_edge_style_option+ '.'? ;

graphviz_graph_style_option: graphviz_style_option ;

graphviz_node_style_option: graphviz_style_option ;

graphviz_edge_style_option: graphviz_style_option ;

graphviz_style_option:  PROPERTY_NAME '=' (PROPERTY_VALUE | '$' NUMBER) ;

// Lexer Rules

REL_NAME: WORD ;

ATTR_NAME: WORD ;

PROPERTY_NAME: WORD ;

WORD: [a-zA-Z0-9_]+ ;

PROPERTY_VALUE: [a-zA-Z0-9_"\\<>\-#.:;,+'!?/]+ ;

NUMBER: [0-9]+ ;

TEMPORAL_ATTR_OPTIONS: ( '_' | 'T' ) ;

GRAPHVIZ_NODE_ATTR_OPTIONS : ( '_' | 'N' ) ;

GRAPHVIZ_EDGE_ATTR_OPTIONS: ( '_' | 'HEAD' | 'TAIL' ) ;

NON_COMMENT: [^%] ;

WHITESPACE : ( '\t' | ' ' | '\r' | '\n'| '\u000C' )+ -> skip ;

TEXT: [a-zA-Z0-9\\_.,/:\-<>"!=]+ ;

