''' 

This module is used to practice looping and branching.
It provides functions for creating a series of project folders. 

'''

import math
import statistics
# import module from previous project: datafun-01-attr
#import maverick_analytics_utils 

import pathlib

'''
# Create a path object
project_path = pathlib.Path.cwd()

# Define the new sub folder path
data_path = project_path.joinpath('data')

# Create new if it doesn't exist, otherwise do nothing
data_path.mkdir(exist_ok=True)
'''

def create_project_directory(directory_name: str):# -> None: #no return type)
  '''
    Creates a project sub-directory.
    :param directory_name: Name to be created.
    '''
  pathlib.Path(directory_name).mkdir(exist_ok=True)

# Function 1: generate folders for a given range
def create_folders_range(start_year: int, end_year: int):
    for year in range(start_year, end_year +1):
        year_directory = pathlib.Path(directory_name).joinpath(str(year))
        create_project_directory(year_directory)

# Function 2: generate folders from a list
def create_folders_list(directory_name: str, folder_levels: list):
    for folder in folder_levels:
        folder_directory = pathlib.Path(directory_name).joinpath(folder)
        create_project_directory(folder_directory)


#Function 3: generate prefixed folders by transforming a list of names and combining with a prefix
def create_prefixed_folders(folder_list: list, prefix: str):
    prefix = folder_list
    folder_names = folder_list

# Function 4: create folders with a while loop
def create_folders_periodically(directory_name: str, duration):


def main():
    create_project_directory(directory_name='data_profile')

    folder_levels = ['elementary', 'middle school', 'high school']
    create_folders_list(directory_name='data_profile',folder_list=folder_levels)

    create_folders_range(start_year=2018, end_year=2024)

    create_prefixed_folders(folder_levels, prefix)



if __name__ == '__main__':
    main()
  