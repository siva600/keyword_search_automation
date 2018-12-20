Use Case:

In terminal enter: 
python filename.py -root_dir directory_path -keyword 'keyword to search' 


Working:

input:
1. Takes a command-line argument “root_dir” as a root directory to start traversing.
2. Takes a command-line argument “keyword” as a regular expression to detect that a file contains 
   the keyword of interest.


main_module function carries to functions:

1. find_keywords : This function with walk through directory and subdirectories to find keyword in all files.
The output will be dictionary with the key as directory name and value as no.of times the keyword appeared in the directory.
example: {’a/b’: 6, ’a/b/c’: 7, ‘/a/b/c/d’:0}.

2. plot_graph: This function takes dictionary type input and displays a plot with x-axis as directory name and y-axis as a bar graph with 
no.of times the keyword occurs.


Test module tests three test cases.
One for validating valid dirname, keyword and expected output. Other for testing exception handling and rest for testing valid keyword. 


