import shutil # this is a module necessary for moving files around

import os # this is a module necessary for parsing the os tree

def main(): # this is the function where everything is done

    list_of_files = os.listdir() # this will give us all the files in list format

    desired_location = '/home/wolf/Desktop/the_ortho_files' # this is the location where all the filtered files will go

    location = '/home/wolf/Desktop/Rijan_folder/OrthoFinder/ProteinData/OrthoFinder/Results_Aug09/Orthogroup_Sequences' # this is the locaton of the files

    with open('Ortho_groups_of_interest_.txt', 'rt') as desired_list: # this is the file where the list of orthogroups should be, you can rename it to anything you want
        list_of_names = desired_list.readlines() 

    for i in list_of_names: # the for loop to open the names of the desired files and to open the files 
        list_of_names = list_of_names.rstrip('\n') # this is important to remove whitespaces, since the python interpreter does not automatically remove the whitespaces in strngs
        for root_path, dir_names, file_names in os.walk(location,topdown=True):
            for file_name in file_names:
                file_path = os.path.join(root_path,file_name)
                file_path_upper = file_path.upper()
                if i in file_path_upper:
                    shutil.copy(file_path,desired_location)

main()
