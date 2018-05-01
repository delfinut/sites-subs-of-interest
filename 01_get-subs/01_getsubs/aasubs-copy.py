#!/anaconda/bin/python3.5

from smallBixTools import smallBixTools as st 

import os, sys 

filename = sys.argv[1]
outfile = filename+"subs.csv"


fastaDict = st.fasta_to_dct(filename)

seqID_list = [] 
# here we can create a list to keep track of what we have compared already.

# lets open a file for writing
# it can be in the same place as where we found the input file.
# we will use "os" to get the pieces of the filename.

# first we have to import os


# now we can use it
root, fn = os.path.split(filename)
# This will give us a tuple like this: ('/home/dave/scratch/aa_subs', 'example_inputfile.fasta')
# we can catch the returns as 2 variables:          root                      fn

# we can create a new output filename using the root part

# now that we have a filename to write to, we can create a handle. Python uses handles to read and write files on the filesystem.
filewriter_handle = open(outfile, "w") # we want to open this file for writing, so we use the "w". The other options are: "r" for reading, or "a" for appending.


for seqID1, sequenceA in fastaDict.items():# .items is a function that acts on fastaDict (all objects have functions. You can access these functions with a dot notation (read: full stop))
    for seqID2, sequenceB in fastaDict.items(): 
        if seqID1 != seqID2: # check that you are not comparing a sequence to itself 
            if ([seqID1, seqID2] not in seqID_list) or ([seqID2, seqID1] not in seqID_list): # check if sequence ID pair have already been checked 
                seqID_list.append([seqID1, seqID2]) # then add that pair of sequence Ids to the list so can be checked next time
                seqID_list.append([seqID2, seqID1]) # A vs B = B vs A                 
                currentpos = 0 # initialize this to 1 for every new comparison.
                
                filewriter_handle.write("%s,%s,"%(seqID1, seqID2)) # removed the colon after %s,%s and added a comma because otherwise the csv file adds the first sub to the seqID as it can only separate commas 
                for aa1, aa2 in zip(sequenceA, sequenceB): # zip will return matched pairs of characters from sequenceA and sequenceB
                    currentpos += 1 # next position
                    d = {} # create an empty dictionary to keep comparisons outputs we have done.
                    subslist = [] # create an empty list 
                    if aa1 != aa2: # if the two AA's are not equal to each other, we want to do keep track of this.
                        #subslist.append([aa1, currentpos, aa2]) 
                        d[seqID1, seqID2] = subslist
                        #print(d)
                        
                        # filewriter handles take strings and write them to file systems. We can either create the string in place, or create a seperate variable and give the variable to the filewriter.
                        # here, creating the variable first:
                        #line_to_write = "%s, %s, %s, %s, %s"%(seqID2, seqID2, aa1, currentpos, aa2, os.linesep)
                        #filewriter_handle.write(line_to_write)
                        
                        # and here, instead of creating a variable, we can do it all on one line.
                        filewriter_handle.write("%s%s%s, "%(aa1, currentpos, aa2))
                filewriter_handle.write(os.linesep)
                        
                # We need to seperate the lines with a line seperator. On almost all linux machines this is the "\n" character. However, mac's are different. But you can do something thats almost like asking Python's "os" module, "What system are you running on?". You get the operating system line seperator with "os.linesep".


# once we have finished, we want to close the file.
filewriter_handle.close()
#>>>>>>> daad244c703969d057066e8c68056db9a7f0e02a
