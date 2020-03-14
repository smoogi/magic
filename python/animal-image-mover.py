"""
Developed by: Nitis Monburinon (2018).
This script fetch file paths from a csv file, then move those files to a particular directory.
To be use with animal_scan.csv only.
"""

import argparse
import glob
import os
import shutil
import pandas as pd

print("\nDeveloped by: Nitis Monburinon (2018).\n"
      "This script fetch file paths from a csv file, then move those files to a particular directory.\n"
      "To be use with animal_scan.csv only.\n")

# Set up the argument variables
parser = argparse.ArgumentParser()
parser.add_argument("working_directory", help="Path to a working directory")
parser.add_argument("destination_directory", help="Path to a destination directory")
parser.add_argument("csv_file", help="Path to a csv file that contains file paths")
args = parser.parse_args()
working_directory = args.working_directory
destination_directory = args.destination_directory
csv_file = args.csv_file

# Get the file in chunk to reduce memory usage
file_list = pd.read_csv(csv_file,low_memory=True,header=None,names=["id","path"],usecols=["id","path"],chunksize=500)

# Count file that has been processed
f_count = 0
# Count file that does not exist in working directory
de_count = 0

for chunk in file_list:
    for f in chunk["path"]:
        # Get only filename
        filename = os.path.basename(f) + ".jpg"
        # Build path to working directory
        f = os.path.join(working_directory, filename)
        # Check if file exist?
        if not os.path.exists(f):
            print(f + " Does not exist.")
            de_count += 1
            continue
        # Build path to a destination
        new_f = os.path.join(destination_directory, filename)
        # Move file to current script directory
        os.renames(f, new_f)       
        # Print feedback to user
        print("'" + filename + "' has been moved to destination")
        f_count += 1

print("Process finished successfully.\n")
print("Files processed: %s" % f_count)
print("Files that does not exist: %s" % de_count)
