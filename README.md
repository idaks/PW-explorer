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
 
 
 
