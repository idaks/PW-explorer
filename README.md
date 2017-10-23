# PW-explorer

 Scripts Used:
 
 1. helper.py : Contains basic definitions used by all other scripts
 
 2. clingo_out.py : Produces the clingo output. Takes in clingo files, project/session name and number of solutions to produce (optional).
 ```
usage: clingo_out.py [-h] [-n NUM_SOLUTIONS] fnames [fnames ...] project_name

positional arguments:
  fnames                provide the clingo files
  project_name          provide a suitable session/project name to reference
                        these results in future scripts

optional arguments:
  -h, --help            show this help message and exit
  -n NUM_SOLUTIONS, --num_solutions NUM_SOLUTIONS
                        number of solutions to generate using clingo,
                        optional, generates all by default
 ```


3. parse.py : Parses the clingo output and fills up the relational databases. Puts them in a pkl file so they can be exported to other formats and used by other scripts directly.
 ```
usage: parse.py [-h] [-f FNAME] project_name

positional arguments:
  project_name          provide a suitable session/project name to reference
                        these results in future scripts

optional arguments:
  -h, --help            show this help message and exit
  -f FNAME, --fname FNAME
                        provide the preprocessed clingo output .txt file to
                        parse. Need not provide one if it already exists in
                        the clingo_output folder as $project_name.txt
```
                      
                                  
 4. export.py: To export the parsed data into various formats.
 ```
 usage: export.py [-h] [-p PROJECT_NAME] [-s] [-sql] [-csv] [-h5] [-msg] [-pkl]

optional arguments:
  -h, --help            show this help message and exit
  -p PROJECT_NAME, --project_name PROJECT_NAME
                        provide session/project name used while parsing
  -s, --schema          generate sql schemas
  -sql                  include if you want to export a sql db
  -csv                  include if you want to export in csv
  -h5                   include if you want to export in hdf5 format
  -msg                  include if you want to export in msgpack format
  -pkl                  include if you want to export in pickle format
  ```
  
5. sql_query.py: Run sql queries on the extracted sqlite database.
```
usage: sql_query.py [-h] [-p PROJECT_NAME]
                    [-intersection | -union | -freq | -num_tuples | -difference {one-way,symmetric} | -redundant_column | -unique_tuples | -custom CUSTOM | -custom_file CUSTOM_FILE | -show_relations]
                    [-rel_name REL_NAME] [-rel_id REL_ID]
                    [-cols [COLS [COLS ...]]] [-pws [PWS [PWS ...]]]
                    [-vals [VALS [VALS ...]]]

optional arguments:
  -h, --help            show this help message and exit
  -p PROJECT_NAME, --project_name PROJECT_NAME
                        provide session/project name used while parsing
  -intersection         provide either relation name or relation_id using the
                        -rel_name or -rel_id flag respectively, columns to
                        consider using the -cols flag and possible worlds to
                        consider using the -pws flag.
  -union                provide either relation name or relation_id using the
                        -rel_name or -rel_id flag respectively, columns to
                        consider using the -cols flag and possible worlds to
                        consider using the -pws flag.
  -freq                 provide either relation name or relation_id using the
                        -rel_name or -rel_id flag respectively, columns to
                        consider using the -cols flag, possible worlds to
                        consider using the -pws flag and the values for the
                        columns (in the mentioned order) using the -vals flag
                        (optional).
  -num_tuples           provide either relation name or relation_id using the
                        -rel_name or -rel_id flag respectively and the
                        possible world ids to count the tuples in using the
                        -pws flag.
  -difference {one-way,symmetric}
                        provide either relation name or relation_id using the
                        -rel_name or -rel_id flag respectively, columns to
                        consider using the -cols flag and the two possible
                        world ids using the -pws flag.
  -redundant_column     provide either relation name or relation_id using the
                        -rel_name or -rel_id flag respectively, columns to
                        consider using the -cols flag and possible worlds to
                        consider using the -pws flag.
  -unique_tuples        provide either relation name or relation_id using the
                        -rel_name or -rel_id flag respectively, columns to
                        consider using the -cols flag and possible worlds to
                        consider using the -pws flag.
  -custom CUSTOM        provide the query enclosed in '' .
  -custom_file CUSTOM_FILE
                        provide the .sql file containing the query.
  -show_relations       to get a list of relations and corresponding relation
                        ids.
  -rel_name REL_NAME    provide the relation name to query. Note that if both
                        rel_id and rel_name are provided, rel_name is
                        disregarded.
  -rel_id REL_ID        provide the relation id of the relation to query. To
                        view relation ids, use -show_relations
  -cols [COLS [COLS ...]]
                        provide the columns of the selected relations to
                        consider for the chosen query. If you want to consider
                        all the columns, do not include this flag.
  -pws [PWS [PWS ...]]  provide the possible world ids of the possible world
                        to consider for this query. If you want to consider
                        all the possible worlds, do not include this flag.
                        Please note that difference query requires exactly 2
                        arguments for this flag.
  -vals [VALS [VALS ...]]
                        provide the values for the freq query in the same
                        order as the mentioned columns. If you want to query
                        all possible tuples, do not include this flag.
 ```
 
 6. sql_funcs.py : Built in Sql functions from PW Explorer such as intersection and union. These however can be used independently and used to create your own distance and complexity calculation metrics.
 
 7. pd_query.py : Runs the queries on the pandas database. Similar to sql_query.py.
 ```
usage: pd_query.py [-h] [-p PROJECT_NAME]
                  [-intersection | -union | -freq | -num_tuples | -difference {one-way,symmetric} | -redundant_column | -unique_tuples | -custom CUSTOM | -show_relations]
                  [-rel_name REL_NAME] [-rel_id REL_ID]
                  [-cols [COLS [COLS ...]]] [-pws [PWS [PWS ...]]]
                  [-vals [VALS [VALS ...]]]

optional arguments:
 -h, --help            show this help message and exit
 -p PROJECT_NAME, --project_name PROJECT_NAME
                       provide session/project name used while parsing
 -intersection         provide either relation name or relation_id using the
                       -rel_name or -rel_id flag respectively, columns to
                       consider using the -cols flag and possible worlds to
                       consider using the -pws flag.
 -union                provide either relation name or relation_id using the
                       -rel_name or -rel_id flag respectively, columns to
                       consider using the -cols flag and possible worlds to
                       consider using the -pws flag.
 -freq                 provide either relation name or relation_id using the
                       -rel_name or -rel_id flag respectively, columns to
                       consider using the -cols flag, possible worlds to
                       consider using the -pws flag and the values for the
                       columns (in the mentioned order) using the -vals flag
                       (optional).
 -num_tuples           provide either relation name or relation_id using the
                       -rel_name or -rel_id flag respectively and the
                       possible world ids to count the tuples in using the
                       -pws flag.
 -difference {one-way,symmetric}
                       provide either relation name or relation_id using the
                       -rel_name or -rel_id flag respectively, columns to
                       consider using the -cols flag and the two possible
                       world ids using the -pws flag.
 -redundant_column     provide either relation name or relation_id using the
                       -rel_name or -rel_id flag respectively, columns to
                       consider using the -cols flag and possible worlds to
                       consider using the -pws flag.
 -unique_tuples        provide either relation name or relation_id using the
                       -rel_name or -rel_id flag respectively, columns to
                       consider using the -cols flag and possible worlds to
                       consider using the -pws flag.
 -custom CUSTOM        provide the query enclosed in '' and either relation
                       name or relation_id using the -rel_name or -rel_id
                       flag respectively.
 -show_relations       to get a list of relations and corresponding relation
                       ids.
 -rel_name REL_NAME    provide the relation name to query. Note that if both
                       rel_id and rel_name are provided, rel_name is
                       disregarded.
 -rel_id REL_ID        provide the relation id of the relation to query. To
                       view relation ids, use -show_relations
 -cols [COLS [COLS ...]]
                       provide the columns of the selected relations to
                       consider for the chosen query. If you want to consider
                       all the columns, do not include this flag.
 -pws [PWS [PWS ...]]  provide the possible world ids of the possible world
                       to consider for this query. If you want to consider
                       all the possible worlds, do not include this flag.
                       Please note that difference query requires exactly 2
                       arguments for this flag.
 -vals [VALS [VALS ...]]
                       provide the values for the freq query in the same
                       order as the mentioned columns. If you want to query
                       all possible tuples, do not include this flag.
 ```
 
 8. dist_calc.py : Distance calculation script. Can create a whole distance matrix, or just get distance between any two PWs. Can also supply your own distance function.
```
usage: dist_calc.py [-h] [-p PROJECT_NAME]
                    [-symmetric_difference | -euler_num_overlaps_diff | -custom_dist_func CUSTOM_DIST_FUNC | -show_relations]
                    [-rel_names [REL_NAMES [REL_NAMES ...]]]
                    [-rel_ids [REL_IDS [REL_IDS ...]]] [-rel_name REL_NAME]
                    [-rel_id REL_ID] [-calc_dist_matrix] [-pws PWS PWS]
                    [-col COL]

optional arguments:
  -h, --help            show this help message and exit
  -p PROJECT_NAME, --project_name PROJECT_NAME
                        provide session/project name used while parsing
  -symmetric_difference
                        this option measures distance by measuring the size of
                        the symmetric difference set of two PWs. Use either
                        the -rel_ids or -rel_names flag to specify the
                        relations to use in this calculation.
  -euler_num_overlaps_diff
                        use this if working with an euler result. This
                        measures the distance as the absolute difference in
                        the number of overlaps (><) in two PWs. Provide the
                        relation name or relation id to use using the
                        -rel_name or rel_id flag respectively. Provide the
                        column name to use using the -col flag.
  -custom_dist_func CUSTOM_DIST_FUNC
                        provide the .py file (without the .py) containing your
                        custom distance function. The function signature
                        should be dist(pw_id_1, pw_id_2, dfs = None, pws =
                        None, relations = None, conn = None) where the latter
                        four arguments refer to the data acquired from parsing
                        the ASP solutions and the connection to the generated
                        sqlite database respectively. The function should
                        return a floating point number. Ensure that the file
                        is in the same directory as this script. You can use
                        the functions in sql_funcs.py to design these dist
                        functions
  -show_relations       to get a list of relations and corresponding relation
                        ids.
  -rel_names [REL_NAMES [REL_NAMES ...]]
                        provide the relation names to use in the distance
                        calculation. Note that if both rel_ids and rel_names
                        are provided, rel_names is disregarded.
  -rel_ids [REL_IDS [REL_IDS ...]]
                        provide the relation ids of the relation to use in the
                        distance calculation. To view relation ids, use
                        -show_relations
  -rel_name REL_NAME    provide the relation name to use in the distance
                        calculation. Note that if both rel_id and rel_name are
                        provided, rel_name is disregarded.
  -rel_id REL_ID        provide the relation id of the relation to use in the
                        distance calculation. To view relation ids, use
                        -show_relations
  -calc_dist_matrix     specify this flag to calculate the distance matrix
  -pws PWS PWS          provide the two possible world ids of the possible
                        world to calculate the distance between. At least one
                        of -pws and -calc_dist_matrix must be used.
  -col COL              provide the column to use for the distance
                        calculation, required with the euler_num_overlaps_diff
                        distance metric.
 ```
 
 9. complexity_calc.py : Complexity calculation script. Supports user defined complexity metrics.
```
usage: complexity_calc.py [-h] [-p PROJECT_NAME]
                          [-euler_complexity_analysis | -custom_complexity_func CUSTOM_COMPLEXITY_FUNC | -show_relations]
                          [-rel_name REL_NAME] [-rel_id REL_ID] [-col COL]
                          [-pws [PWS [PWS ...]]]

optional arguments:
  -h, --help            show this help message and exit
  -p PROJECT_NAME, --project_name PROJECT_NAME
                        provide session/project name used while parsing
  -euler_complexity_analysis
                        use this if working with an euler result. This
                        measures the complexity as the number of overlaps (><)
                        in two PWs. Provide the relation name or relation id
                        to use using the -rel_name or rel_id flag
                        respectively. Provide the column name to use using the
                        -col flag. Calculates complexity on all PWs by
                        default. Use the -pws flag to specify the possible
                        world ids if compexity of only a few are required.
  -custom_complexity_func CUSTOM_COMPLEXITY_FUNC
                        provide the .py file (without the .py) containing your
                        custom complexity function. The function signature
                        should be complexity(pw_id, dfs = None, pws = None,
                        relations = None, conn = None) where the latter four
                        arguments refer to the data acquired from parsing the
                        ASP solutions and the connection to the generated
                        sqlite database respectively. The function should
                        return a floating point number. Ensure that the file
                        is in the same directory as this script. You can use
                        the functions in sql_funcs.py to design these dist
                        functions
  -show_relations       to get a list of relations and corresponding relation
                        ids.
  -rel_name REL_NAME    provide the relation name to use in the distance
                        calculation. Note that if both rel_id and rel_name are
                        provided, rel_name is disregarded.
  -rel_id REL_ID        provide the relation id of the relation to use in the
                        distance calculation. To view relation ids, use
                        -show_relations
  -col COL              provide the column to use for the complexity analysis,
                        required with the euler_complexity_analysis function
  -pws [PWS [PWS ...]]  provide the possible world ids of the possible world
                        to calculate the complexity for. Calculates for all
                        PWs if not used.
```

10. visualisation.py : Creates the visualisations. No modularity currently. Will add soon.
```
usage: visualize.py [-h] [-p PROJECT_NAME]

optional arguments:
  -h, --help            show this help message and exit
  -p PROJECT_NAME, --project_name PROJECT_NAME
                        provide session/project name used while parsing
```

 
