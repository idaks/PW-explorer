import networkx as nx

from ..Input_Parsers.Meta_Data_Parser.meta_data_parser import (
    META_DATA_GRAPHVIZ_GRAPH_DEF_KEYWORD,
    META_DATA_GRAPHVIZ_NODE_DEF_KEYWORD,
    META_DATA_GRAPHVIZ_EDGE_DEF_KEYWORD,
    META_DATA_GRAPHVIZ_EDGE_HEAD_IDX_DEF_KEYWORD,
    META_DATA_GRAPHVIZ_EDGE_TAIL_IDX_DEF_KEYWORD,
    META_DATA_GRAPHVIZ_NODE_ID_IDX_DEF_KEYWORD,
    META_DATA_GRAPHVIZ_STYLES_KEYWORD,
    META_DATA_GRAPHVIZ_STYLE_PROPERTY_ARG_IDX_TYPE,
    META_DATA_GRAPHVIZ_ORD_KEYWORD,
    META_DATA_GRAPHVIZ_GRAPH_TYPE,
    META_DATA_GRAPHVIZ_DIRECTED_KEYWORD,
    META_DATA_GRAPHVIZ_UNDIRECTED_KEYWORD,
)


def build_nx_from_metadata(pw_rel_dfs: dict, graphviz_meta_data: dict):

    graph_type = graphviz_meta_data[META_DATA_GRAPHVIZ_GRAPH_DEF_KEYWORD][META_DATA_GRAPHVIZ_GRAPH_TYPE]
    if graph_type == META_DATA_GRAPHVIZ_UNDIRECTED_KEYWORD:
        G = nx.Graph()
    elif graph_type == META_DATA_GRAPHVIZ_DIRECTED_KEYWORD:
        G = nx.DiGraph()
    else:
        print("Unrecognized {} attribute. Choose one of ({})".
              format(META_DATA_GRAPHVIZ_GRAPH_TYPE,
                     ", ".join([META_DATA_GRAPHVIZ_UNDIRECTED_KEYWORD, META_DATA_GRAPHVIZ_DIRECTED_KEYWORD])))
        return None

    graph_styles = graphviz_meta_data[META_DATA_GRAPHVIZ_GRAPH_DEF_KEYWORD][META_DATA_GRAPHVIZ_STYLES_KEYWORD]
    for prop_name, prop_type, prop_value in graph_styles:
        G.graph[prop_name] = prop_value

    sort_by_ord_key = lambda x: x[1][META_DATA_GRAPHVIZ_ORD_KEYWORD]

    for edge_rel_name, edge_rel_details in sorted(graphviz_meta_data[META_DATA_GRAPHVIZ_EDGE_DEF_KEYWORD].items(),
                                                  key=sort_by_ord_key):
        if edge_rel_name in pw_rel_dfs:
            rel_df = pw_rel_dfs[edge_rel_name]
            edge_head_attr_name = rel_df.columns[edge_rel_details[META_DATA_GRAPHVIZ_EDGE_HEAD_IDX_DEF_KEYWORD] + 1]
            edge_tail_attr_name = rel_df.columns[edge_rel_details[META_DATA_GRAPHVIZ_EDGE_TAIL_IDX_DEF_KEYWORD] + 1]
            edge_styles = edge_rel_details[META_DATA_GRAPHVIZ_STYLES_KEYWORD]

            for i, row in rel_df.iterrows():
                head, tail = row[edge_head_attr_name], row[edge_tail_attr_name]
                curr_edge_style = {}
                for prop_name, prop_type, prop_value in edge_styles:
                    if prop_type == META_DATA_GRAPHVIZ_STYLE_PROPERTY_ARG_IDX_TYPE:
                        prop_value = row[rel_df.columns[prop_value - 1 + 1]]
                        # -1 to convert from 1-indexed user input to 0-indexed machine index and
                        # +1 to account for the first column that is 'pw'
                    curr_edge_style[prop_name] = prop_value
                G.add_edge(head, tail, **curr_edge_style)

    for node_rel_name, node_rel_details in sorted(graphviz_meta_data[META_DATA_GRAPHVIZ_NODE_DEF_KEYWORD].items(),
                                                  key=sort_by_ord_key):
        if node_rel_name in pw_rel_dfs:
            rel_df = pw_rel_dfs[node_rel_name]
            node_id_idx = node_rel_details[META_DATA_GRAPHVIZ_NODE_ID_IDX_DEF_KEYWORD]
            node_styles = node_rel_details[META_DATA_GRAPHVIZ_STYLES_KEYWORD]
            node_id_idx_attr_name = rel_df.columns[node_id_idx + 1]
            for i, row in rel_df.iterrows():
                node_name = row[node_id_idx_attr_name]
                curr_node_style = {}
                for prop_name, prop_type, prop_value in node_styles:
                    if prop_type == META_DATA_GRAPHVIZ_STYLE_PROPERTY_ARG_IDX_TYPE:
                        prop_value = row[rel_df.columns[prop_value - 1 + 1]]
                        # -1 to convert from 1-indexed user input to 0-indexed machine index and
                        # +1 to account for the first column that is 'pw'
                    curr_node_style[prop_name] = prop_value
                G.add_node(node_name, **curr_node_style)

    return G
