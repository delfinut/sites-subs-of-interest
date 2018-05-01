# Readme is written. Read me. 

#Hmm I'm not sure this make sense to you but this might be better than going through this verbally! 


Script name:    
sitesofinterest.py

To run:    
python sitesofinterest.py [output from aasubs.py] [sitesofinterest - infile] [name of output file you want - outfile]

What this script does:
Reads a csv file (A) with pairwise description of amino acid differences
(substitutions) and the residue number at which they occur (such as an output
file from aasubs.py). Reads another csv file (B) that assigns certain residue
numbers to sites of interest (such as antigenic sites, polybasic cleavage site
etc.).
Checks if the residue numbers in each line in file A correspond to residue
numbers assigned to sites of interest in file B, if so assigns that difference
to that site. So for each pair of sequences, the functionally significant 
amino acid differences between them are shown.

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
File A is a .csv file of format: 
SeqID1,SeqID2, aa1Xaa2, aa3Yaa4
SeqID1,SeqID2,,,		
SeqID1,SeqID2,,,	

File B is a .csv file of format:
Sa, Sb, Ca1 
124-125, 184-195, 
166-170 153-157,,203-205



Output: 
.csv file with each line containing the name of sequence pair being compared 
followed by the differences which have been assigned to site of interest if any. 
In the first two columns, each line will contain the names of the pair of 
sequences being compared. The next columns will be headed by the name of the 
site of interest.

Output Example: 
,,Sa,Sb,Ca1 
SeqID1,SeqID2 ,eg. Y124G; S159N, P185D; Q190Y; N240A,,,, 
SeqID1,SeqID2 ,,,,, 
SeqID1,SeqID2 ,,,,,



Python dependencies: 
none 

Authors:   
David Matten, Divya Venkatesh


