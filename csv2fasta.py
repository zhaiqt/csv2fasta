
import csv

#####

def read_csv(inFile,name_column,seq_column):

    seq_dict = {}
    with open(inFile,'rbU') as csvfile:
        readCSV = csv.reader((x.replace('\0','') for x in csvfile))
        for row in readCSV:
            if len(row) == 0: # ignore empty line
                continue
            seq_dict[row[name_column]] = row[seq_column]
    return seq_dict

def write_txt(indict,outputname):
    print indict
    if outputname.endswith(".txt"):
        Outfile1= open(outputname,"w+")
    else:
        Outfile1= open(outputname+".txt","w+")
    for name, seq in indict.iteritems():
        output=">"+name+"\n"+seq+"\n"
        Outfile1.write (output)
    Outfile1.close()


######### iniate new data ########
infile= raw_input("Tablename in csv format?")
namecolumn=raw_input("Name position in the table?")
namecolumn = int(namecolumn) -1
seqcolumn=raw_input("Seq position in the table?")
seqcolumn = int(seqcolumn) -1
outfile = raw_input("Output Fasta file name?")

extracted_dict= read_csv(infile,namecolumn,seqcolumn)
write_txt(extracted_dict,outfile)
