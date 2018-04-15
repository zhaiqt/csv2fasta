
import csv
import re

#####

def read_csv(infilename,name_column,seq_column,):
    infile =open(infilename, 'r')
    seqdict={}

    split_symble =''
    if infilename.endswith('.csv'):
        split_symble = ','
    elif infilename.endswith('.txt'):
        split_symble = '\t'

    for row in infile:
        if row.startswith("#"):
            continue
        row = row.strip('\n')
        row = row.split(split_symble)
        ID=row[name_column]
        ID = exact_number(ID)

        #output=row[name_column]+'\t'+row[seq_column]+'\n'
        #alldict.append(row[0]:row[column_ID])
        seqdict[ID] = row[seq_column]

    return seqdict



########
def compare_2_dict(dict1,dict2,outfilename):
    outfilename = outfilename.rstrip('.txt')
    outfilename = outfilename.rstrip('.csv')

    outfilename1 = outfilename+"_unique.csv"
    outfile1 = open(outfilename1,'wb')


    outfilename2 = outfilename+"_uniquefasta.txt"
    outfile2 = open(outfilename2,'wb')

    outfilename3 = outfilename+"_overlap.csv"
    outfile3 = open(outfilename3,'wb')

    outfilename4 = outfilename+"_overlap.txt"
    outfile4 = open(outfilename4,'wb')

    outfilename5 = outfilename+"_missing.csv"
    outfile5 = open(outfilename5,'wb')


    for key_2, value_2 in dict2.iteritems():
        if key_2 not in dict1.keys():
            output1 = key_2 +','+ value_2+'\n'
            outfile1.write(output1)

            output2 = '>'+key_2.lstrip('>')+'\n'+value_2+'\n'
            #print output2
            outfile2.write(output2)
        else:
            output3 = key_2 +','+ value_2+'\n'
            outfile3.write(output3)

            output4 = '>'+key_2.lstrip('>')+'\n'+value_2+'\n'
            #print output2
            outfile4.write(output4)

    outfile1.close()
    outfile2.close()
    outfile3.close()
    outfile4.close()

    for key_1, value_1 in dict1.iteritems():
        if key_1 not in dict2.keys():
            output3 = key_1 +', ,'+ '\n'
            outfile5.write(output3)

    outfile5.close()



###########
#######
def exact_number(string):
    q=''
    string = string.split(';')
    string = string [0]
    if string:
        IDs= re.search('\d{4}',string)

    print "String :" + string
    #print IDs
    return IDs.group(0)


######### iniate new data ########
infilename1= raw_input("First file name, in .txt or .csv format?   ") or "tillerHC.csv"
infilename2= raw_input("Second file name, in .txt or .csv format?    ") or "Craig_smart.csv"

namecolumn = raw_input("In which column contains the ID?   ") or '1'
namecolumn = int(namecolumn) -1

seq_column=raw_input("In which column the last 2 amino acids will be removed?   ") or "2"
seq_column = int(seq_column) -1


outfilename = raw_input("Output name?   ") or "L"


race_dict = read_csv(infilename1,namecolumn,seq_column)
tiller_dict = read_csv(infilename2,namecolumn,seq_column)
compare_2_dict(race_dict,tiller_dict,outfilename)
