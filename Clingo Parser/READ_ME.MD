Instructions:

To run the Parser for a single file:
1. sh ./run_file.sh [clingo_input_file_location] [project_name] [number_of_PWs, optional, 0 by default i.e. all PWs]

To export in any combination of sql, msg_pack (msg), pickle (pkl), hdf (h5) and csv, just enter the keywords (in brackets), in a comma separated list.
eg. sql, pkl
would export in sql and pkl formats in their respective exports folders inside a folder the same as the project name. 

A copy of the input file with name project_name.lp4 will be put in the folder Mini\ Workflow/clingo_input.
The output of the clingo ASP on the given file, modified to be suitable for the Parser is put into Mini\ Workflow/clingo_output folder. The name is set to project_name.txt .
The output of the parser is put into the folder Mini\ Workflow/parser_output. The name of the file is project_name.txt .

To run multiple input file in the same folder with extension .lp4:
1. sh ./run_all.sh [folder_location] [number_of_PWs, optional, 0 by default i.e. all PWs]

eg. sh ./run_all.sh Test_Run_All_Folder

 
