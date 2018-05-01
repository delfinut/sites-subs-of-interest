#!/anaconda/bin/python3.5

import os,sys

#run as 

#python sitesofinterest.py [aasubsoutput - aa_subs_output_fn] [sitesofinterest - infile] [name of output file you want - outfile]

aa_subs_output_fn = sys.argv[1]
infile = sys.argv[2]
outfile = sys.argv[3]

#outfile = "SOIoutput.csv"
#outfile - "H3eq1output"
#outfile - "H3eq2output"
#outfile = "domainoutput.csv"
#outfile = "burkesmithoutput.csv"


# now that we have a filename to write to, we can create a handle. Python uses handles to read and write files on the filesystem.
filewriter_handle = open(outfile, "w") # we want to open this file for writing, so we use the "w".

# read in the output file from aa_subs.py, append each line in file, as an element of a list (called data here)

#aa_subs_output_fn = "/home/dave/scratch/sitesofinterest/aa_subs_output.csv"
#aa_subs_output_fn = "/Users/divyavenkatesh/Dropbox/BitBucket/sitesofinterest/from_aasubs.csv"


data = []
with open(aa_subs_output_fn, "r") as fh: #open to read "r"
    for line in fh:
        data.append(line.strip()) #append the list called data with each line from file stripped of leading and trailing whitespace



# read in the input file. This file defines which sites are of interest. append each line in file as an element of a list (called sitesOfInterest)

#infile = "/home/dave/scratch/sitesofinterest/input_to_sitesOfInterest.csv"
#infile = "/Users/divyavenkatesh/Dropbox/BitBucket/sitesofinterest/SOI.csv"
#infile = "/Users/divyavenkatesh/Dropbox/BitBucket/sitesofinterest/FunctionalDomain_SOI.csv"
#infile = "/Users/divyavenkatesh/Dropbox/BitBucket/sitesofinterest/BurkeSmith_SOI.csv"
#infile = "/Users/divyavenkatesh/Dropbox/BitBucket/sitesofinterest/H3eq_SOI.csv"
#infile = "/Users/divyavenkatesh/Dropbox/BitBucket/sitesofinterest/H3eq_SOI2.csv"

sitesOfInterest = [] #open an empty list 
with open(infile, "r") as fh: #open to read "r"
    for line in fh:
        sitesOfInterest.append(line.strip()) #append the list called sitesOfInterest with each line from file, stripped of leading and trailing whitespace


#populate an ordered dictionary (takes order from input) with the data from list sitesOfInterest. keys = type of site of interest (SOI), values = associated residue numbers 

filewriter_handle.write(",,") #because first two columns will be taken up by names of the sequence pairs

from collections import OrderedDict

sitesOfInterestDct = OrderedDict() #open an empty ordered dictionary

for line in sitesOfInterest: #each line should have a cateogry of sites 
    #print("line: {}".format(line)) #prints exactly what's in each line of input file
    chunks = line.split(",") #make a variable called chunks that takes the elements of the line split with , 
    SOI_type = chunks[0] #the first element (which is 0 in python) is the name of the type of site of interest i.e SOI_type
    #print("These sites are: {}".format(SOI_type)) #check that you have SOI_type correct by pprinting first element 
    all_sites = [] #open an empty list called all sites 
    for sites in chunks[1:]: #start considering sites from the second element as first is a name of site category not the site itself 
        if "-" in sites: #is it a range of values eg. from 152-155
            start, stop = sites[:sites.find("-")], sites[sites.find("-")+1:] #start = element before it finds a - and stop is the thing after the -
            all_sites += list(range(int(start), int(stop)+1)) #include the range of numbers from start to stop i.e 152,153,154,155 and add to list all_sites 
        else:
            all_sites += [int(sites)] #if not just add the number of type integer to the list of all_sites 
    all_sites = list(set(all_sites)) #if there are repeats then set gets rid of them
    all_sites.sort() #sort the numbers in ascending order (which is default, I guess)
    sitesOfInterestDct[SOI_type] = all_sites #to the key SOI_type in dictionary, add all the the site numbers (this is python grammar format assumes SOI_type is the key and all_sites are values)

    filewriter_handle.write("%s,"%(SOI_type)) #write down list of SOI_types in the first line (will be in order) 
filewriter_handle.write(os.linesep) #go to next line 


SOIkeylist = list(sitesOfInterestDct) #a list of all the keys to be used later 

#open a dictionary to assign the substitution info in file (eg N143K) to sequence pairs, and another to assign associated residue numbers (here, 143) only to them

allSiteDataInSeqpairDct = {} 
allSitesInSeqpairDct = {}

for pair in data: #this is the list of data from output file from the aasubs.py 
    #print(pair) # so this = the whole first line read as "pair"
    pair = pair.split(",") #splits the line whereever it finds a , (great for a csv yaargh)
    seqID1, seqID2 = pair[0], pair[1] #assign the first and second element of the line "pair" (which is an element of big list data) as the seq IDs 
    this_pair_all_sites = [] #open empty list 
    this_pair_all_siteData = []
    for siteData in pair[2:]: #for each element after the names ie. element 3 to the end (i.e after sequence names, the subs list) each is a siteData i.e E14G H234Y
        #print(siteData)
        siteData = siteData.replace(" ", "") #there would be a space after the comma? remove that 
        #print(siteData[1:-1]) #this is the number between the aa. this means slice the element E14D, and output what comes 2nd (after first aa) upto but not including the last (-1) - last being the second aa 
        #input("aafs")
        if siteData != "": #because it kept saying '' could not be read as an integer 
            site = int(siteData[1:-1]) #this number is an integer eg. 14 and is assigned to the variable called 'site'
        this_pair_all_sites.append(site) #append this number to the list you just opened up there: this_pair_all_sites. So now you have a list of all the residue in which there has been change between that pair
        this_pair_all_siteData.append(siteData)
        allSiteDataInSeqpairDct[seqID1,seqID2] = this_pair_all_siteData
        allSitesInSeqpairDct[seqID1,seqID2] = this_pair_all_sites
    #print("this pair all sitse =", this_pair_all_sites)
    #print("this pair all sitedata =", this_pair_all_siteData)
    #input("dddddd")


    filewriter_handle.write("%s,%s,"%(seqID1, seqID2)) #write names of seqIDs separated by commas 
    for i in range(0,len(sitesOfInterestDct)): #to loop over each key of dictionary, python starts counting at 0
        for SOIpos in sitesOfInterestDct.get(SOIkeylist[i]): #this is looking for value (we name SOIpos) in current (i) key (each SOI_type) 
                if SOIpos in this_pair_all_sites: #defined above 
                    for siteData in this_pair_all_siteData: #for siteData (eg E14H), if it is not just a space (as the last one always is), and if the site number is same as SOIpos, write it to line
                        if siteData != "":
                            if int(siteData[1:-1]) == SOIpos:
                                filewriter_handle.write("%s;  "%(siteData))
                                #filewriter_handle.write("%s;  "%(SOIpos))
        filewriter_handle.write(",") #once all the siteData correspinging to one SOI_type is write, make a delimitation (, for csv)

    filewriter_handle.write(os.linesep) #once all siteData for given pair of seqIDs is done, go to newline, and new pair of seqIDs                
filewriter_handle.close()

print("Khatam!")





