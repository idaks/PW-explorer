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

