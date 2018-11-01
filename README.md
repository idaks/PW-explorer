# An Extensible Possible Worlds Explorer for Answer Set Programming

### To Get Started (using venv):

1. Install clingo. PW_explorer has been tested with clingo version: 5.2.1

2. Make sure the packages graphviz>=0.8.2 and pygraphviz>=1.5 are installed. These are required to be able to use the visualization functionality. You can find instructions to install pygraphviz [here](http://pygraphviz.github.io/documentation/pygraphviz-1.3.1/install.html).

These commands usually work as well:

  a.  ```apt-get install python-dev graphviz libgraphviz-dev pkg-config``` OR ```brew install graphviz``` 

  b.  ```pip3 install pygraphviz```
  
  (Might need to run them using sudo)
  
  [StackOverflow Reference](https://stackoverflow.com/questions/40528048/pip-install-pygraphviz-no-package-libcgraph-found)

3. ```python3 -m venv /path/to/new/virtual/environment```

4. ```source /path/to/new/virtual/environment/bin/activate```

5. ```python3 -m pip install PW_explorer```

To deactivate the virtualenv after you're done working:

6. ```deactivate```

Repeat Step 4 to resume work and Step 6 to exit the virtualenv again.

Installing PW_explorer will install all the modules within PW_explorer along with all their dependencies. It will also install the following Command Line Tools in /usr/bin/ :

1. pwe_run_clingo
2. pwe_load_worlds
3. pwe_dist_calc
4. pwe_complexity_calc
5. pwe_visualize
6. pwe_export
7. pwe_query

The above CLI tools leverage the installed PW_explorer modules.

### General Workflow:

```                                           
                                      run clingo to generate the Possible Worlds 
                                                       ⏬
                                    parse the output to load the Possible Worlds
                                                       ⏬
                             export Possible Worlds' descriptions to formats such as sql, csv
                                                       ⏬
                                               query using pandas
                                                       ⏬
                                               distance calculation 
                                                       ⏬
                                                complexity analysis
                                                       ⏬
                                               visualize your results
```

### CLI Scripts Used:
 
1. pwe_run_clingo : Produces the clingo output. Takes in clingo files, project/session name and number of solutions to produce (optional).
 ```
dependencies: argparse subprocess32 

usage: pwe_run_clingo [-h] [-n NUM_SOLUTIONS] fnames [fnames ...] project_name

positional arguments:
  fnames                provide the clingo files
  project_name          provide a suitable session/project name to reference
                        these results in future scripts

optional arguments:
  -h, --help            show this help message and exit
  -n NUM_SOLUTIONS, --num_solutions NUM_SOLUTIONS
                        number of solutions to generate using clingo,
                        optional, generates all by default
 ```


2. pwe_load_worlds : Parses the clingo output and fills up the relational databases. Puts them in a pkl file so they can be exported to other formats and used by other scripts directly.
 ```
dependencies: argparse pickle

usage: pwe_load_worlds [-h] [-f FNAME] [-clingo | -dlv] project_name

positional arguments:
  project_name          provide a suitable session/project name to reference
                        these results in future scripts

optional arguments:
  -h, --help            show this help message and exit
  -f FNAME, --fname FNAME
                        provide the preprocessed clingo output .txt file to
                        parse. Need not provide one if it already exists in
                        the asp_output folder as $project_name.txt
  -clingo
  -dlv

```
                      
                                  
 3. pwe_export: To export the parsed data into various formats.
 ```
dependencies: pandas numpy sqlite3 pickle argparse 
 
usage: pwe_export [-h] [-p PROJECT_NAME] [-s] [-sql] [-csv] [-h5] [-msg]
                  [-pkl]

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
  
 
 4. pwe_query : Runs the queries on the possible worlds.
 ```
dependencies: argparse
 
usage: pwe_query [-h] [-p PROJECT_NAME]
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
 
5. pwe_dist_calc : Distance calculation script. Can create a whole distance matrix, or just get distance between any two PWs. Can also supply your own distance function.
```
dependencies: pandas numpy pickle argparse importlib

usage: pwe_dist_calc [-h] [-p PROJECT_NAME]
                     [-symmetric_difference | -euler_num_overlaps_diff | -custom_dist_func CUSTOM_DIST_FUNC CUSTOM_DIST_FUNC | -show_relations]
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
  -custom_dist_func CUSTOM_DIST_FUNC CUSTOM_DIST_FUNC
                        provide the module name and complete file path to the
                        python module respectively The function signature
                        should be dist(pw_id_1, pw_id_2, **kwargs) where
                        kwargs contains the follwing:dfs, pws, relationswhere
                        the latter three arguments refer to the data acquired
                        from parsing the ASP solutions. The function should
                        return a floating point number. Ensure that the file
                        is in the same directory as this script. You can use
                        the functions in sql_funcs.py to design these dist
                        functions.
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
 
 6. pwe_complexity_calc : Complexity calculation script. Supports user defined complexity metrics.
```
dependencies: pandas numpy argparse importlib

usage: pwe_complexity_calc [-h] [-p PROJECT_NAME]
                           [-euler_complexity_analysis | -custom_complexity_func CUSTOM_COMPLEXITY_FUNC CUSTOM_COMPLEXITY_FUNC | -show_relations]
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
  -custom_complexity_func CUSTOM_COMPLEXITY_FUNC CUSTOM_COMPLEXITY_FUNC
                        provide the module name and the full path to the
                        python file containing your custom complexity function
                        respectively. The function signature should be
                        complexity(pw_id, **kwargs) where the kwargs provided
                        will be dfs, pws and relationswhere the kwargs refer
                        to the data acquired from parsing the ASP solutions
                        and the connection to the generated sqlite database
                        respectively. The function should return a floating
                        point number. Ensure that the file is in the same
                        directory as this script. You can use the functions in
                        sql_funcs.py to design these dist functions
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

7. pwe_visualize : Creates the visualisations.
```
dependencies: argparse importlib

usage: pwe_visualize [-h] [-p PROJECT_NAME] [-mds] [-mds_sklearn]
                     [-sdf SCALE_DOWN_FACTOR] [-clustering] [-dendrogram]
                     [-custom_visualization_func CUSTOM_VISUALIZATION_FUNC CUSTOM_VISUALIZATION_FUNC]

optional arguments:
  -h, --help            show this help message and exit
  -p PROJECT_NAME, --project_name PROJECT_NAME
                        provide session/project name used while parsing
  -mds                  produce a Multidimensional Scaling Graph Output using
                        the Neato Program. Provide a scale-down-factor for
                        graph generation. Default factor is 5.0
  -mds_sklearn          produce a MDS graph in 2D using skelearn's MDS
                        package.
  -sdf SCALE_DOWN_FACTOR, --scale_down_factor SCALE_DOWN_FACTOR
                        provide a scale factor for the Multidimensional
                        Scaling Graph. Deafults to 5.0
  -clustering           use DBScan Algorithm to cluster the Possible Worlds
  -dendrogram           create various dendrograms using scipy
  -custom_visualization_func CUSTOM_VISUALIZATION_FUNC CUSTOM_VISUALIZATION_FUNC
                        provide the module name and path to the python file
                        containing your custom visualisation function, in that
                        order The function signature should be
                        visualize(**kwargs) the following arguments are
                        provided: dfs, relations, pws, project_name,
                        dist_matrix, save_to_folder, of which the
                        visualization function may use any subsetfrom parsing
                        the ASP solutions and the connection to the generated
                        sqlite database respectively. The function should
                        create the visualization and may or may not return
                        anything. Ensure that the file is in the same
                        directory as this script. You can use the functions in
                        sql_funcs.py to design these visualisation functions
```

### Example:

Both CLI and module tutorials coming soon!
