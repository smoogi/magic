"""
Developed by: Nitis Monburinon (2018)
This script rename all files in the specified directory to lowercase and then replace all white space with hyphen (-).
"""

import os
import sys
import glob
import argparse

# Print welcome message
print("\nDeveloped by: Nitis Monburinon (2018)\n"
      "This script rename all files in the specified directory to lowercase.\n"
      "and then replace all white space with hyphen (-).\n")

# Set up the argument variables
parser = argparse.ArgumentParser()
parser.add_argument("working_directory", help="Path to a working directory")
args = parser.parse_args()
working_directory = args.working_directory

# Get the iterator in case file list is so large
file_list = glob.iglob(os.path.join(working_directory, '*'))

print("Beginning the process...")

for f in file_list:
    # Don't process a directory
    if os.path.isdir(f):
        continue
    # Get only filename
    filename = os.path.basename(f)
    # Split filename and extension
    filename_split = os.path.splitext(filename)
    # Change to filename lowercase and replace whitespace with hyphen then concat with extension again
    new_f = os.path.join(working_directory, filename_split[0].replace(" ", "-").lower() + filename_split[1])
    # Rename old file name to new file name
    os.renames(f, new_f)
    # Print feedback to user
    print("'" + f + "' has been renamed.")

print("Process finished successfully.\n")
