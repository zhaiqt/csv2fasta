
import csv

#####


##############

########
def rm_last2aa_csv(infilename,name_column,seq_column):
    infile =open(infilename, 'r')
    outfilename = infilename.rstrip('.txt').rstrip('.csv')

    print "parsed table(removed the last 2 amino acids) are saved in -------- %s_table.txt. " %outfilename
    outfilename1= outfilename+'_table.csv'
    outfile1=open(outfilename1,"wb")
    split_symble =''

    if infilename.endswith('.csv'):
        split_symble = ','
    elif infilename.endswith('.txt'):
        split_symble = '\t'

    count_row =0
    alldict={}
    for row in infile:
        #print row
        if row.startswith("#"):
            continue
        count_row +=1
        row = row.strip('\n')
        row = row.split(split_symble)
        row[name_column]= exact_number(row[name_column])

        q=''
        for j in row[seq_column] :
            if j.isalpha():
                q=''.join([q,j])
        row[seq_column] =q[:-2]


        output=row[name_column]+','+row[seq_column]+'\n'
        #alldict.append(row[0]:row[column_ID])
        alldict[row[name_column]] = row[seq_column]
        outfile1.write(output)

    print "The last two residue in column %d of table has been rewrite into the %s." % (seq_column,outfilename+'_table.csv')

    fastafilename= outfilename+'_fasta.txt'

    write_fasta(alldict,fastafilename)
    print "The table has been rewrite into the fasta file ---- %s." % fastafilename
    return


def write_fasta(indict,outputname):
    Outfile1 = open(outputname,'w')
    for name, seq in indict.iteritems():
        output=">"+name+"\n"+seq+"\n"
        Outfile1.write (output)
    Outfile1.close()




#######
def exact_number(string):
    q=''
    string = string.split(';')
    string = string [0]
    for i in string:
        if i.isdigit():
             q=''.join([q,i])

    return q






######### iniate new data ########





infilename= raw_input("Tablename in txt format?   ") or "fixed_VH.txt"

namecolumn = raw_input("In which column contains the ID?   ") or '1'
namecolumn = int(namecolumn) -1

seq_column=raw_input("In which column the last 2 amino acids will be removed?   ") or "2"
seq_column = int(seq_column) -1


rm_last2aa_csv(infilename,namecolumn,seq_column)
