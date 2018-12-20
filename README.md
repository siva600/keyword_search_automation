Use Case:

In terminal enter: 
<<<<<<< HEAD
python filename.py -root_dir directory path -keyword 'keyword to search' 

=======
python <filename>.py -root_dir <directory path> -keyword '<keyword to search>' 
>>>>>>> 0736a3ae8aefe23bf65ec7b373996fc6979274ba



Working:

input:
1. Takes a command-line argument “root_dir” as a root directory to start traversing.
2. Takes a command-line argument “keyword” as a regular expression to detect that a file contains 
   the keyword of interest.
