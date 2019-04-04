from antlr4 import *
from .Antlr_Files.PWE_ASP_Meta_DataLexer import PWE_ASP_Meta_DataLexer
from .Antlr_Files.PWE_ASP_Meta_DataParser import PWE_ASP_Meta_DataParser
from .Antlr_Files.PWE_ASP_Meta_DataListener import PWE_ASP_Meta_DataListener
from ...helper import isfloat
from antlr4.tree.Trees import Trees


# Update the PWE_ASP_Meta_Data.g4 file accordingly and rerun with antlr4 if changing any of the below
ASP_COMMENT_SYMBOL = '%'

ASP_SYNTAX_TEMPORAL_DEC_KEYWORD = 'temporal'
ASP_SYNTAX_GRAPHVIZ_DEC_KEYWORD = 'graphviz'
ASP_SYNTAX_GRAPHVIZ_GRAPH_DEC_KEYWORD = 'graph'
ASP_SYNTAX_GRAPHVIZ_NODE_DEC_KEYWORD = 'node'
ASP_SYNTAX_GRAPHVIZ_EDGE_DEC_KEYWORD = 'edge'
ASP_SYNTAX_ATTRIBUTE_DEF_KEYWORD = 'schema'

ASP_SYNTAX_TEMPORAL_DEC_ATTR_KEYWORD = 'T'
ASP_SYNTAX_NODE_DEC_ATTR_KEYWORD = 'N'
ASP_SYNTAX_EDGE_HEAD_DEC_ATTR_KEYWORD = 'HEAD'
ASP_SYNTAX_EDGE_TAIL_DEC_ATTR_KEYWORD = 'TAIL'

META_DATA_KEYWORD = 'meta_data'
META_DATA_TEMPORAL_DEC_KEYWORD = 'temporal_dec'
META_DATA_ATTRIBUTE_DEF_KEYWORD = 'attr_def'


class AntlrPWEMetaDataListener(PWE_ASP_Meta_DataListener):

    def __init__(self):
        self.meta_data = {}

def parse_meta_data(fname, silent=False, print_parse_tree=False):

    input_ = FileStream(fname)
    lexer = PWE_ASP_Meta_DataLexer(input_)

    # use this line to take input from the cmd line
    # lexer = PWE_ASP_Meta_DataLexer(StdinStream())

    stream = CommonTokenStream(lexer)
    parser = PWE_ASP_Meta_DataParser(stream)
    tree = parser.aspFile()
    if print_parse_tree:
        print(Trees.toStringTree(tree, None, parser))
    pw_analyzer = AntlrPWEMetaDataListener()
    pw_analyzer.silent = silent
    walker = ParseTreeWalker()
    walker.walk(pw_analyzer, tree)

    return pw_analyzer.meta_data