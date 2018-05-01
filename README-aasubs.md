# OK how does this look? More details? 

Script name:  
aasubs.py

To run:  
python aasubs.py [fasta filename] [set outfile name]


What this script does:  
Searches the alignment pairwise for differences(substitutions/mutations), 
makes a note of these differencs and the residue number at which they occur  
all non-redundant pairs of sequences are searched. 

Note:
--The residue number is calculated according to the alignment where sequences 
of interest are aligned to a reference sequence and trimmed at the start 
accordingly. For HA proteins this would be according to the paper: 
Burke DF, Smith DJ (2014) A Recommended Numbering Scheme for 
Influenza A HA Subtypes. PLOS ONE 9(11): e112302. 
https://doi.org/10.1371/journal.pone.0112302
--The terms differences, mutations, and substitutions
here just refer to a change in the amino acid at a certain point in the
alignment - the  actual meaning will depend on the data.  


Input:  
multiple sequence alignment (amino acids) in fasta format


Output:  
.csv file with each line containing  name of sequence pair being
compared followed by the differences found in the format A56B


Output Example:  
SeqID1,SeqID2, aa1Xaa2, aa3Yaa4
SeqID1,SeqID2,,,		
SeqID1,SeqID2,,,	


Python dependencies:  
smallBixTools  


Authors:  
David Matten, Divya Venkatesh