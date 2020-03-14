"""
Developed by: Nitis Monburinon (2018)
This script move all file in 1st Argument subdirectories to 2nd Argument.
"""

import argparse
import glob
import os

print("\nDeveloped by: Nitis Monburinon (2018)\n"
      "This script move all file in 1st Argument subdirectories to 2nd Argument\n")

# Set up the argument variables
parser = argparse.ArgumentParser()
parser.add_argument("working_directory", help="Path to a working directory")
parser.add_argument("destination_directory", help="Path to a destination directory")
args = parser.parse_args()
working_directory = args.working_directory
destination_directory = args.destination_directory

# Get the iterator in case file list is so large
working_directory = os.path.join(working_directory, "**")
file_list = glob.iglob(working_directory, recursive=True)

print("Beginning the process...")

for f in file_list:
    # Don't process a directory
    if os.path.isdir(f):
        continue
    # Get only filename
    filename = os.path.basename(f)
    # Build path to a destination
    new_f = os.path.join(destination_directory, filename)
    # Move file to current script directory
    os.renames(f, new_f)
    # Print feedback to user
    print("'" + filename + "' has been moved to destination")

print("Process finished successfully.\n")
