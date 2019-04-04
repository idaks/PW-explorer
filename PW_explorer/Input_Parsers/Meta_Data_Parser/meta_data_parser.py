from antlr4 import *
from antlr4.tree.Trees import Trees

import re

from .Antlr_Files.PWE_ASP_Meta_DataLexer import PWE_ASP_Meta_DataLexer
from .Antlr_Files.PWE_ASP_Meta_DataParser import PWE_ASP_Meta_DataParser
from .Antlr_Files.PWE_ASP_Meta_DataListener import PWE_ASP_Meta_DataListener
from ...helper import isfloat


# Update the PWE_ASP_Meta_Data.g4 file accordingly and rerun with antlr4 if changing any of the below
ASP_COMMENT_SYMBOL = '%'

ASP_SYNTAX_ATTRIBUTE_DEF_KEYWORD = 'schema'
ASP_SYNTAX_TEMPORAL_DEC_KEYWORD = 'temporal'
ASP_SYNTAX_GRAPHVIZ_DEC_KEYWORD = 'graphviz'

# Add from above when declaring new meta_data types
ASP_SYNTAX_DEC_KEYWORDS = [
    ASP_SYNTAX_ATTRIBUTE_DEF_KEYWORD,
    ASP_SYNTAX_TEMPORAL_DEC_KEYWORD,
    ASP_SYNTAX_GRAPHVIZ_DEC_KEYWORD,
]

# Regex for detecting meta_data comments
META_DATA_COMMENT_REGEX = "^%+\s*({}).*".format("|".join(ASP_SYNTAX_DEC_KEYWORDS))

# For graphviz meta_data
ASP_SYNTAX_GRAPHVIZ_GRAPH_DEC_KEYWORD = 'graph'
ASP_SYNTAX_GRAPHVIZ_NODE_DEC_KEYWORD = 'node'
ASP_SYNTAX_GRAPHVIZ_EDGE_DEC_KEYWORD = 'edge'
ASP_SYNTAX_NODE_DEC_ATTR_KEYWORD = 'N'
ASP_SYNTAX_EDGE_HEAD_DEC_ATTR_KEYWORD = 'HEAD'
ASP_SYNTAX_EDGE_TAIL_DEC_ATTR_KEYWORD = 'TAIL'

# For temporal meta_data
ASP_SYNTAX_TEMPORAL_DEC_ATTR_KEYWORD = 'T'

# For use within package
META_DATA_KEYWORD = 'meta_data'
META_DATA_TEMPORAL_DEC_KEYWORD = 'temporal_dec'
META_DATA_ATTRIBUTE_DEF_KEYWORD = 'attr_def'
META_DATA_GRAPHVIZ_DEF_KEYWORD = 'graphviz'
META_DATA_GRAPHVIZ_GRAPH_DEF_KEYWORD = 'graph'
META_DATA_GRAPHVIZ_NODE_DEF_KEYWORD = 'node'
META_DATA_GRAPHVIZ_EDGE_DEF_KEYWORD = 'edge'


def preprocess(lines):

    def has_a_comment(line):
        return line.find(ASP_COMMENT_SYMBOL) != -1

    def extract_comment(comment_line):
        comment_start_idx = comment_line.find(ASP_COMMENT_SYMBOL)
        comment = comment_line[comment_start_idx:].strip()
        return comment

    def is_a_valid_meta_data_comment(comment):
        pattern = re.compile(META_DATA_COMMENT_REGEX)
        return pattern.search(comment) is not None

    lines_with_comments = filter(has_a_comment, lines)
    comments = map(extract_comment, lines_with_comments)
    comments_with_meta_data = filter(is_a_valid_meta_data_comment, comments)

    return list(comments_with_meta_data)


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