import re

ASP_COMMENT_SYMBOL = '%'

ASP_SYNTAX_TEMPORAL_DEC_KEYWORD = 'temporal'
ASP_SYNTAX_TEMPORAL_DEC_ATTR_KEYWORD = 'T'
ASP_SYNTAX_ATTRIBUTE_DEF_KEYWORD = 'schema'

META_DATA_KEYWORD = 'meta_data'
META_DATA_TEMPORAL_DEC_KEYWORD = 'temporal_dec'
META_DATA_ATTRIBUTE_DEF_KEYWORD = 'attr_def'

TEMPORAL_FIELD_DEF_REGEX="{}\s*\w+\(\s*[_T]+\s*(,\s*[_T]+\s*)*\)".format(ASP_SYNTAX_TEMPORAL_DEC_KEYWORD)
ATTRIBUTES_DEF_REGEX = "{}\s*\w+\(\s*\w+\s*(,\s*\w+\s*)*\)".format(ASP_SYNTAX_ATTRIBUTE_DEF_KEYWORD)


def filter_comments(lines):
    return list(filter(lambda l: l.find(ASP_COMMENT_SYMBOL) != -1, lines))


def extract_comment(comment_line):
    comment_start_idx = comment_line.find(ASP_COMMENT_SYMBOL)
    comment = comment_line[comment_start_idx + 1:].strip()
    return comment


def parse_for_temporal_declarations(asp_rules: list):
    """
    :param asp_rules: a single \n separated string of rules or a list of rules
    :return: dict mapping rel_name --> list of temporal_indices
    """
    if isinstance(asp_rules, str):
        asp_rules = asp_rules.splitlines()
    temporal_decs = {}
    pattern = re.compile(TEMPORAL_FIELD_DEF_REGEX)

    comments = filter_comments(asp_rules)

    for i, line in enumerate(comments):
        comment = extract_comment(line)
        pattern_object = pattern.search(comment)
        if pattern_object is not None:
            declaration = comment[pattern_object.span()[0]:pattern_object.span()[1]]
            declaration = declaration.split(ASP_SYNTAX_TEMPORAL_DEC_KEYWORD, maxsplit=1)[1].strip()
            temp = declaration.split('(', maxsplit=1)
            rel_name = temp[0]
            attrs = temp[1].rsplit(')', maxsplit=1)[0].split(',')
            attrs = list(map(str.strip, attrs))
            rel_name = "{}_{}".format(rel_name, len(attrs))
            temporal_indices = [i for i, attr in enumerate(attrs) if attr == ASP_SYNTAX_TEMPORAL_DEC_ATTR_KEYWORD]
            temporal_decs[rel_name] = temporal_indices

    return temporal_decs


def parse_for_attribute_defs(asp_rules: list):
    """
    :param asp_rules: a single \n separated string of rules or a list of rules
    :return: dict mapping rel_name --> list of attr_names
    """
    if isinstance(asp_rules, str):
        asp_rules = asp_rules.splitlines()
    attribute_defs = {}
    pattern = re.compile(ATTRIBUTES_DEF_REGEX)

    comments = filter_comments(asp_rules)

    for i, line in enumerate(comments):
        comment = extract_comment(line)
        pattern_object = pattern.search(comment)
        if pattern_object is not None:
            definition = comment[pattern_object.span()[0]:pattern_object.span()[1]]
            definition = definition.split(ASP_SYNTAX_ATTRIBUTE_DEF_KEYWORD, maxsplit=1)[1].strip()
            temp = definition.split('(', maxsplit=1)
            rel_name = temp[0]
            attrs = temp[1].rsplit(')', maxsplit=1)[0].split(',')
            attrs = list(map(str.strip, attrs))
            attribute_defs["{}_{}".format(rel_name, len(attrs))] = attrs

    return attribute_defs


def parse_meta_data(asp_rules):
    if isinstance(asp_rules, str):
        asp_rules = asp_rules.splitlines()
    meta_data = {
        META_DATA_ATTRIBUTE_DEF_KEYWORD: parse_for_attribute_defs(asp_rules),
        META_DATA_TEMPORAL_DEC_KEYWORD: parse_for_temporal_declarations(asp_rules),
    }
    return meta_data