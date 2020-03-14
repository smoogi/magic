import os
import sys
import glob
import argparse

# Print welcome message
print("\nDeveloped by: smoogi (2020)"
      "Use pandoc to convert .org to .md")

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
    name = filename_split[0]
    extension = filename_split[1]
    # use pandoc to convert the stuff
    os.system("pandoc -s {}.org -o {}.md".format(name, name))
    print("'" + f + "' has been converted.")

print("Process finished successfully.\n")
