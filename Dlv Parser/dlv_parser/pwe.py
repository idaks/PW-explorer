#!/usr/bin/env python2.7
import argparse
import AntlrDlv as dlv
import query
def handler_export():
    arguments = [args.fileName]
    if args.sql:
        arguments.append('-sql')
    if args.csv:
        arguments.append('-csv')
    if args.output:
        arguments.extend(['-o', args.output[0]])
    dlv.init(arguments)

def handler_sql():
    arguments = ['sqlQuery', args.sql[0]]
    if args.output:
        arguments.extend(['-o', args.output[0]])
    if args.intersection:
        arguments.extend(['--intersection', args.intersection[0]])
    if args.display:
        arguments.append('-d')
    if args.query:
        arguments.extend(['-query', args.query[0]])
    query.init(arguments)
def handler_csv():
    pass
def argParser():
    parser = argparse.ArgumentParser(description='Possible World Explorer.')
    subparsers = parser.add_subparsers(help='sub-command help')

    #export
    parser_export = subparsers.add_parser('export', help='sqlQuery help')
    parser_export.add_argument('fileName', help='ASP file location')
    parser_export.add_argument('-o', '--output', nargs = 1, help='Specify project output folder')

    parser_export.add_argument('-sql', action='store_true', help='Output SQLite database')
    parser_export.add_argument('-csv', action='store_true', help='Output csv format')
    parser_export.set_defaults(func=handler_export)

    #sql subparser
    parser_sql = subparsers.add_parser('sqlQuery', help='sqlQuery help')
    parser_sql.add_argument('sql', nargs = 1, help='Input SQLite database location')
    parser_sql.add_argument('-d', '--display', action='store_true', help='Display Schema')
    parser_sql.add_argument('--intersection', nargs = 1, help='intersection relation name')
    parser_sql.add_argument('-query', nargs = 1, help='query input')
    parser_sql.add_argument('-o', '--output', nargs = 1, help='Output file location')
    parser_sql.set_defaults(func=handler_sql)
    
    # pandas subparser
    parser_csv = subparsers.add_parser('pandasQuery', help='pandasQuery help')
    parser_csv.add_argument('csv', nargs = 1, help='Input csv file location')
    parser_csv.set_defaults(func=handler_csv)
    
    return parser
if __name__ == '__main__':
    parser = argParser()
    args = parser.parse_args()
    args.func()
