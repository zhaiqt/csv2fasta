
import csv

#####


def read_csv(infilename,name_column,seq_column,):
    infile =open(infilename, 'rU')
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
        #ID = exact_number(ID)

        #output=row[name_column]+'\t'+row[seq_column]+'\n'
        #alldict.append(row[0]:row[column_ID])
        row[seq_column] = row[seq_column].replace(' ','')
        row[seq_column] = row[seq_column].replace('\t','')
        seqdict[ID] = row[seq_column]

    return seqdict
'''
def read_csv(inFile,name_column,seq_column):

    seq_dict = {}
    with open(inFile,'rbU') as csvfile:
        readCSV = csv.reader((x.replace('\0','') for x in csvfile))
        for row in readCSV:
            if len(row) == 0: # ignore empty line
                continue
            seq_dict[row[name_column]] = row[seq_column]
    return seq_dict
'''
def write_txt(indict,outputname):
    print indict
    if outputname.endswith(".txt"):
        Outfile1= open(outputname,"w+")
    else:
        Outfile1= open(outputname+".txt","w+")
    for name, seq in indict.iteritems():
        if name and seq:
            output=">"+name+"\n"+seq+"\n"
        Outfile1.write (output)
    Outfile1.close()


######### iniate new data ########
infile= raw_input("Tablename in csv format?   ") or "uniquepair.csv"
namecolumn=raw_input("Name position in the table?   ") or '1'
namecolumn = int(namecolumn) -1
seqcolumn=raw_input("Seq position in the table?   ") or '2'
seqcolumn = int(seqcolumn) -1
outfile = raw_input("Output Fasta file name?   ") or 'H_fasta.txt'

extracted_dict= read_csv(infile,namecolumn,seqcolumn)
write_txt(extracted_dict,outfile)
