import pandas as pd # will need this to 

import re

import os

start_point_string = "./"

end_point_string = ".pal"

ceratopteris_string = "Ceric"

home_address = os.getcwd()

full_address = f'{home_address}/{"parsed_absrel_json.txt"}'

def main():

    list_of_orthgroups = []

    main_table = {'Orthgroup':[],'count':[],"Cericv":[]}

    df = pd.DataFrame(main_table)

    with open(full_address,'r') as main_file:
        main_file_lines = main_file.readlines()

    # main_file_lines = iter(main_file_lines)

    for i in main_file_lines:
        i = i[i.find(start_point_string)+2 : i.find(end_point_string)]
        if i not in list_of_orthgroups:
            list_of_orthgroups.append(i)

    orthcount = 0 # counting the number of orthogroups

    ceriv_count = 0 # counting the occurence of ceratopteris

    # for k in main_file_lines:
    #     print(k)
    print("Orthgroup",'\t','orthcount','\t','ceriv_count')
    for j in list_of_orthgroups:
        j = j.rstrip('\n')
        for k in main_file_lines:
            if j in k:
                orthcount = orthcount + 1
            if j in k and ceratopteris_string in k:
                ceriv_count = ceriv_count + 1
        print(j,'\t',orthcount,'\t',ceriv_count)
        orthcount = 0
        ceriv_count = 0
    

main()