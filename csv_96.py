
#######
def read_csv(infilename,column):
    infile =open(infilename, 'rU')
    seqdict={}
    count =0

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
        row[column] = row[column].replace(' ','')
        row[column] = row[column].replace('\t','')
        if row[column]:
            count +=1
            seqdict[count] = row[column]

    return seqdict

########

#####################
def write_selected_into96(Dict,outfileName):
	Outfile = open (outfileName, 'w+')
	count =0
	keys = Dict.keys()
	keys.sort()
	for key in keys:

		if count % 96 ==0:
			Outfile.write("\n\n,1,2u")
			count =0
		if count% 12 ==0:
			Outfile.write ("\n"+ chr((count/12)+65)+ ',')
		Outfile.write(Dict[key]+',')
		#Outfile.write(str(value)+',')
		count +=1

	print "positive clones have been reformated into 96well plate: " + outfileName
        return

#########
#####################
import collections
import csv
def write_selected_into96_bycolumn(Dict,outfileName):
    row_size = 8
    chunk_size = 96

    ordered_dict = collections.OrderedDict(sorted(Dict.items()))
    num_entry = len(ordered_dict)
    if not num_entry: return
    num_chunk = (num_entry - 1) / chunk_size + 1  ### 96 as one chunk;


    with open(outfileName, 'wb') as csvfile:
        writer = csv.writer(csvfile)
        for j in xrange(num_chunk):
            for i in xrange(row_size):
                start, end = j * chunk_size, min(num_entry, (j + 1) * chunk_size)
                row = [val for key, val in ordered_dict.items()[start:end] if (key - 1) % row_size == i]
                writer.writerow(row)
            writer.writerow([])

	print "positive clones have been reformated into 96well plate: " + outfileName

######### iniate new data ########
infile= raw_input("Tablename in csv format?   ") or "arm4_VH.csv"
column=raw_input("Name position in the table?   ") or '5'
column = int(column) -1

#outfile = raw_input("Output Fasta file name?   ") or 'H_fasta.txt'
outfilename = infile.rstrip('.csv')+'_column'+ str(column) + '_96.csv'

extracted_list= read_csv(infile,column)
write_selected_into96_bycolumn(extracted_list,outfilename)
