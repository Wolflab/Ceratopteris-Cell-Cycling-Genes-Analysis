# this is a drop in replacement for grep, this was more reliable than grep. The purpose of this script is to find the orthogroups of interest from orthogroups.tsv file and print them.
def main():
    with open('cell_cycling_list.txt','rt') as small_list: # this is the list of genes you are interested in, one per line
        small_list_lines = small_list.readlines()

    for i in small_list_lines:
        i = i.rstrip('\n')
        parser(i)

def parser(current):
    
    with open('Orthogroups.tsv','rt') as big_list: # this is the orthogroups.tsv file that orthofinder makes
        big_list_lines = big_list.readlines()
    
    for line in big_list_lines:
        split_by_tabs = line.rsplit('\t')
        for the_comma_group in split_by_tabs:
            split_by_commas = the_comma_group.rsplit(',')
            for the_gene in split_by_commas: #this opens the individual words/genes in the line as a list and tries to see for partial strings in indiviudual words/genes
                if current in the_gene:
                    print(line)

main()

