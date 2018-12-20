import os
import sys
import re
import argparse
import matplotlib.pyplot as plt


# find_keywords function with walk through directory and subdirectories to find keyword in all files.
# The output will be dictionary with the key as directory name and value as no.of times the keyword
# appeared in the directory. Arguments as directory name and keyword.
def find_keywords(root_dir, keyword):
        keyword_count = {}
        if not os.path.exists(root_dir):
            raise Exception("invalid dirname")

        if not keyword:
            raise Exception("Keyword is required")

        for dirName, subdirList, fileList in os.walk(root_dir):
            for filename in fileList:
                count = 0
                try:
                    search_file = open(os.path.join(dirName, filename), "r")
                    for line in search_file:
                        if keyword in line:
                            count += 1
                    if dirName in keyword_count:
                        keyword_count[dirName] += count
                    else:
                        keyword_count[dirName] = count
                    search_file.close()

                except Exception as e:
                    print(e)
        return keyword_count


def plot_graph(dirname_keyword):
    plt.bar(range(len(dirname_keyword)), list(dirname_keyword.values()), align='center')
    plt.xticks(range(len(dirname_keyword)), list(dirname_keyword.keys()), rotation=90)
    plt.show()


if __name__ == '__main__':
    try:
        parser = argparse.ArgumentParser(description='Search some files')
        parser.add_argument('-root_dir', action='store', required=True, dest='dir', help='root directory')
        parser.add_argument('-keyword', action='store', required=True, dest='keyword', help='Keyword to search for')
        args = parser.parse_args()

        root_dir = args.dir
        keyword = args.keyword

        # check if path is valid
        if not os.path.exists(root_dir):
            print("Not a valid directory passed")
            sys.exit()

        # check if keyword is valid
        validExpression = r"([a-zA-Z0-9]+)"
        keyword_valid = re.search(validExpression, keyword)

        # if both keyword and path valid, pass them as arguments to find_keywords and graph functions.
        if keyword_valid:
            dirname_keyword = find_keywords(root_dir, keyword)
            print(dirname_keyword)
            plot_graph(dirname_keyword)
        else:
            print("Not a Valid Keyword - {}".format(keyword))
            sys.exit()

    except Exception as e:
        print(e)



