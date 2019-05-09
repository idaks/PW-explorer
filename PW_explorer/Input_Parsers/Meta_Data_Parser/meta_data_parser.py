from antlr4 import *
from antlr4.tree.Trees import Trees

import re
from copy import deepcopy

from .Antlr_Files.PWE_ASP_Meta_DataLexer import PWE_ASP_Meta_DataLexer
from .Antlr_Files.PWE_ASP_Meta_DataParser import PWE_ASP_Meta_DataParser
from .Antlr_Files.PWE_ASP_Meta_DataListener import PWE_ASP_Meta_DataListener
from ...helper import (
    isfloat,
    is_int,
)


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

# For graphviz meta_data
ASP_SYNTAX_GRAPHVIZ_GRAPH_DEC_KEYWORD = 'graph'
ASP_SYNTAX_GRAPHVIZ_NODE_DEC_KEYWORD = 'node'
ASP_SYNTAX_GRAPHVIZ_EDGE_DEC_KEYWORD = 'edge'
ASP_SYNTAX_NODE_DEC_ATTR_KEYWORD = 'N'
ASP_SYNTAX_EDGE_HEAD_DEC_ATTR_KEYWORD = 'HEAD'
ASP_SYNTAX_EDGE_TAIL_DEC_ATTR_KEYWORD = 'TAIL'
ASP_SYNTAX_ARG_IDX_SYMBOL = '$'
ASP_SYNTAX_GRAPHVIZ_STYLE_ORD_KEYWORD = 'ord'
ASP_SYNTAX_GRAPHVIZ_GRAPH_TYPE_KEYWORD = 'graph_type'

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
META_DATA_GRAPHVIZ_EDGE_HEAD_IDX_DEF_KEYWORD = 'head'
META_DATA_GRAPHVIZ_EDGE_TAIL_IDX_DEF_KEYWORD = 'tail'
META_DATA_GRAPHVIZ_NODE_ID_IDX_DEF_KEYWORD = 'node_id'
META_DATA_GRAPHVIZ_STYLES_KEYWORD = 'styles'
META_DATA_GRAPHVIZ_STYLE_PROPERTY_DIRECT_TYPE = 'direct'
META_DATA_GRAPHVIZ_STYLE_PROPERTY_ARG_IDX_TYPE = 'arg_idx'
META_DATA_GRAPHVIZ_ORD_KEYWORD = 'ord'
META_DATA_GRAPHVIZ_GRAPH_TYPE = 'graph_type'
META_DATA_GRAPHVIZ_DIRECTED_KEYWORD = 'directed'
META_DATA_GRAPHVIZ_UNDIRECTED_KEYWORD = 'undirected'

META_DATA_TEMPLATE = {
    META_DATA_TEMPORAL_DEC_KEYWORD: {},
    META_DATA_ATTRIBUTE_DEF_KEYWORD: {},
    META_DATA_GRAPHVIZ_DEF_KEYWORD: {
        META_DATA_GRAPHVIZ_GRAPH_DEF_KEYWORD: {
            META_DATA_GRAPHVIZ_GRAPH_TYPE: META_DATA_GRAPHVIZ_UNDIRECTED_KEYWORD,
            META_DATA_GRAPHVIZ_STYLES_KEYWORD: [],
        },
        META_DATA_GRAPHVIZ_NODE_DEF_KEYWORD: {},
        META_DATA_GRAPHVIZ_EDGE_DEF_KEYWORD:{},
    }
}

# Regex for detecting meta_data comments
META_DATA_COMMENT_REGEX = "^%+\s*({}).*".format("|".join(ASP_SYNTAX_DEC_KEYWORDS))

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
        self.meta_data = deepcopy(META_DATA_TEMPLATE)
        self.curr_meta_data_type = None
        self.curr_meta_data = None
        self.silent = False

    @staticmethod
    def gen_meta_data_rel_name_key(rel_name, rel_arity):

        return "{}_{}".format(rel_name, str(rel_arity))

    @staticmethod
    def get_values_from_CSV_list(words):

        words = "".join(words)
        words = words.split(',')
        words = list(map(str.strip, words))
        return words

    @staticmethod
    def convert_property_value_to_appropriate_type(value):

        if is_int(value):
            return int(value)
        elif isfloat(value):
            return float(value)
        else:
            return value

    def enterAttr_def(self, ctx:PWE_ASP_Meta_DataParser.Attr_defContext):
        self.curr_meta_data_type = META_DATA_ATTRIBUTE_DEF_KEYWORD
        rel_name = ctx.TEXT(0).getText()
        vals = []
        i = 1
        while ctx.TEXT(i) is not None:
            vals.append(ctx.TEXT(i).getText())
            i += 1
        attr_names = AntlrPWEMetaDataListener.get_values_from_CSV_list(vals)
        rel_arity = len(attr_names)
        self.curr_meta_data = (rel_name, rel_arity, attr_names)


    def exitAttr_def(self, ctx:PWE_ASP_Meta_DataParser.Attr_defContext):

        (rel_name, rel_arity, attr_names) = self.curr_meta_data
        temp_rel_name = AntlrPWEMetaDataListener.gen_meta_data_rel_name_key(rel_name, rel_arity)
        self.meta_data[META_DATA_ATTRIBUTE_DEF_KEYWORD][temp_rel_name] = attr_names

        self.curr_meta_data = None
        self.curr_meta_data_type = None

    def enterTemporal_dec(self, ctx:PWE_ASP_Meta_DataParser.Temporal_decContext):
        self.curr_meta_data_type = META_DATA_TEMPORAL_DEC_KEYWORD
        rel_name = ctx.TEXT(0).getText()
        vals = []
        i = 1
        while ctx.TEXT(i) is not None:
            vals.append(ctx.TEXT(i).getText())
            i += 1
        vals = AntlrPWEMetaDataListener.get_values_from_CSV_list(vals)
        rel_arity = len(vals)
        temporal_indices = [i for i in range(len(vals)) if vals[i] == ASP_SYNTAX_TEMPORAL_DEC_ATTR_KEYWORD]
        self.curr_meta_data = (rel_name, rel_arity, temporal_indices)

    def exitTemporal_dec(self, ctx:PWE_ASP_Meta_DataParser.Temporal_decContext):

        (rel_name, rel_arity, temporal_indices) = self.curr_meta_data
        temp_rel_name = AntlrPWEMetaDataListener.gen_meta_data_rel_name_key(rel_name, rel_arity)
        self.meta_data[META_DATA_TEMPORAL_DEC_KEYWORD][temp_rel_name] = temporal_indices

        self.curr_meta_data = None
        self.curr_meta_data_type = None

    def enterGraphviz_styling(self, ctx:PWE_ASP_Meta_DataParser.Graphviz_stylingContext):

        self.curr_meta_data_type = META_DATA_GRAPHVIZ_DEF_KEYWORD

    def enterGraphviz_graph_dec(self, ctx:PWE_ASP_Meta_DataParser.Graphviz_graph_decContext):

        self.curr_meta_data_type += '_' + META_DATA_GRAPHVIZ_GRAPH_DEF_KEYWORD
        self.curr_meta_data = (None, None, None, [])

    def enterGraphviz_node_dec(self, ctx:PWE_ASP_Meta_DataParser.Graphviz_node_decContext):

        self.curr_meta_data_type += '_' + META_DATA_GRAPHVIZ_NODE_DEF_KEYWORD
        rel_name = ctx.TEXT(0).getText()
        vals = []
        i = 1
        while ctx.TEXT(i) is not None:
            vals.append(ctx.TEXT(i).getText())
            i += 1
        vals = AntlrPWEMetaDataListener.get_values_from_CSV_list(vals)
        rel_arity = len(vals)
        rel_node_id_idx = None
        try:
            rel_node_id_idx = vals.index(ASP_SYNTAX_NODE_DEC_ATTR_KEYWORD)
        except ValueError as e:
            print("Couldn't find node name indicator {} in declaration of the graphviz node"
                  .format(ASP_SYNTAX_NODE_DEC_ATTR_KEYWORD))
            print(e)
        self.curr_meta_data = (rel_name, rel_arity, rel_node_id_idx, [])

    def enterGraphviz_edge_dec(self, ctx:PWE_ASP_Meta_DataParser.Graphviz_edge_decContext):

        self.curr_meta_data_type += '_' + META_DATA_GRAPHVIZ_EDGE_DEF_KEYWORD
        rel_name = ctx.TEXT(0).getText()
        vals = []
        i = 1
        while ctx.TEXT(i) is not None:
            vals.append(ctx.TEXT(i).getText())
            i += 1
        vals = AntlrPWEMetaDataListener.get_values_from_CSV_list(vals)
        rel_edge_id_idxs = None

        try:
            rel_edge_id_idxs = {
                META_DATA_GRAPHVIZ_EDGE_HEAD_IDX_DEF_KEYWORD: vals.index(ASP_SYNTAX_EDGE_HEAD_DEC_ATTR_KEYWORD),
                META_DATA_GRAPHVIZ_EDGE_TAIL_IDX_DEF_KEYWORD: vals.index(ASP_SYNTAX_EDGE_TAIL_DEC_ATTR_KEYWORD),
            }
        except ValueError as e:
            print("Couldn't find edge head or tail indicators")
            print(e)

        rel_arity = len(vals)
        self.curr_meta_data = (rel_name, rel_arity, rel_edge_id_idxs, [])

    def enterGraphviz_style_option(self, ctx:PWE_ASP_Meta_DataParser.Graphviz_style_optionContext):

        _, _, _, graphviz_styles_list = self.curr_meta_data

        property_name = ctx.TEXT(0).getText()
        property_type = None
        property_value = None
        if ctx.TEXT(1) is not None:
            temp = ctx.TEXT(1).getText()
            if temp[0] == ASP_SYNTAX_ARG_IDX_SYMBOL:
                property_type = META_DATA_GRAPHVIZ_STYLE_PROPERTY_ARG_IDX_TYPE
                temp = temp[1:]
            else:
                property_type = META_DATA_GRAPHVIZ_STYLE_PROPERTY_DIRECT_TYPE
            property_value = AntlrPWEMetaDataListener.convert_property_value_to_appropriate_type(temp)

        graphviz_styles_list.append((property_name, property_type, property_value))

    def exitGraphviz_edge_dec(self, ctx:PWE_ASP_Meta_DataParser.Graphviz_edge_decContext):

        rel_name, rel_arity, rel_edge_id_idxs, graphviz_edge_styles = self.curr_meta_data
        style_ord = 1
        for property_name, property_type, property_value in graphviz_edge_styles:
            if property_name == ASP_SYNTAX_GRAPHVIZ_STYLE_ORD_KEYWORD:
                style_ord = property_value

        temp_rel_name = AntlrPWEMetaDataListener.gen_meta_data_rel_name_key(rel_name, rel_arity)
        self.meta_data[META_DATA_GRAPHVIZ_DEF_KEYWORD][META_DATA_GRAPHVIZ_EDGE_DEF_KEYWORD][temp_rel_name] = {
            META_DATA_GRAPHVIZ_EDGE_HEAD_IDX_DEF_KEYWORD: rel_edge_id_idxs[META_DATA_GRAPHVIZ_EDGE_HEAD_IDX_DEF_KEYWORD],
            META_DATA_GRAPHVIZ_EDGE_TAIL_IDX_DEF_KEYWORD: rel_edge_id_idxs[META_DATA_GRAPHVIZ_EDGE_TAIL_IDX_DEF_KEYWORD],
            META_DATA_GRAPHVIZ_STYLES_KEYWORD: graphviz_edge_styles,
            META_DATA_GRAPHVIZ_ORD_KEYWORD: style_ord,
        }

        self.curr_meta_data = None
        self.curr_meta_data_type = None

    def exitGraphviz_node_dec(self, ctx:PWE_ASP_Meta_DataParser.Graphviz_node_decContext):

        rel_name, rel_arity, rel_node_id_idx, graphviz_node_styles = self.curr_meta_data
        style_ord = 1
        for property_name, property_type, property_value in graphviz_node_styles:
            if property_name == ASP_SYNTAX_GRAPHVIZ_STYLE_ORD_KEYWORD:
                style_ord = property_value

        temp_rel_name = AntlrPWEMetaDataListener.gen_meta_data_rel_name_key(rel_name, rel_arity)
        self.meta_data[META_DATA_GRAPHVIZ_DEF_KEYWORD][META_DATA_GRAPHVIZ_NODE_DEF_KEYWORD][temp_rel_name] = {
            META_DATA_GRAPHVIZ_NODE_ID_IDX_DEF_KEYWORD: rel_node_id_idx,
            META_DATA_GRAPHVIZ_STYLES_KEYWORD: graphviz_node_styles,
            META_DATA_GRAPHVIZ_ORD_KEYWORD: style_ord,
        }

        self.curr_meta_data = None
        self.curr_meta_data_type = None

    def exitGraphviz_graph_dec(self, ctx:PWE_ASP_Meta_DataParser.Graphviz_graph_decContext):

        _, _, _, graphviz_styles_list = self.curr_meta_data
        graph_type = META_DATA_GRAPHVIZ_UNDIRECTED_KEYWORD

        for property_name, property_type, property_value in graphviz_styles_list:
            if property_name == ASP_SYNTAX_GRAPHVIZ_GRAPH_TYPE_KEYWORD:
                graph_type = property_value

        self.meta_data[META_DATA_GRAPHVIZ_DEF_KEYWORD][META_DATA_GRAPHVIZ_GRAPH_DEF_KEYWORD] = {
            META_DATA_GRAPHVIZ_STYLES_KEYWORD: graphviz_styles_list,
            META_DATA_GRAPHVIZ_GRAPH_TYPE: graph_type
        }

        self.curr_meta_data = None
        self.curr_meta_data_type = None

    def exitGraphviz_styling(self, ctx:PWE_ASP_Meta_DataParser.Graphviz_stylingContext):

        self.curr_meta_data_type = None


def __parse_meta_data__(input_stream, silent=False, print_parse_tree=False):
    lexer = PWE_ASP_Meta_DataLexer(input_stream)

    # use this line to take input from the cmd line
    # lexer = PWE_ASP_Meta_DataLexer(StdinStream())

    ct_stream = CommonTokenStream(lexer)
    parser = PWE_ASP_Meta_DataParser(ct_stream)
    tree = parser.aspFile()
    if print_parse_tree:
        print(Trees.toStringTree(tree, None, parser))
    asp_meta_data_listener = AntlrPWEMetaDataListener()
    asp_meta_data_listener.silent = silent
    walker = ParseTreeWalker()
    walker.walk(asp_meta_data_listener, tree)

    return asp_meta_data_listener.meta_data


def parse_meta_data_from_file(fname, silent=False, print_parse_tree=False):
    input_stream = FileStream(fname)
    return __parse_meta_data__(input_stream, silent, print_parse_tree)


def parse_meta_data_from_string(asp_input_string, silent=False, print_parse_tree=False):
    input_stream = InputStream(asp_input_string)
    return __parse_meta_data__(input_stream, silent, print_parse_tree)
