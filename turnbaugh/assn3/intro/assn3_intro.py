'''
Similar to R packages, Biopython provides us with tools for bioinformatics 
It allows us to interact with common file formats; e.g., fasta, genbank, pdb...
'''


# the SeqIO class facilitates input and output - hence the "IO"
from Bio import SeqIO

# iterate through sequence records in a fasta file
for seq_record in SeqIO.parse("seqs.fa", "fasta"):
    
    # each record is an object with various attributes
    # because this is fasta format, attributes include id and seq
    print seq_record.id


'''
Notice how readable this code is, when compared to the first assignment in Python
that accomplished the same task as this script.

One of my close friends, a former Google engineer, has a philosophy I like: in his
view, it is a mistake to think that code is written for a computer; code should be
thought of as being written for other humans.

It's not hard to hack together something that does what you want it to do; but if
we're to share scripts, we should strive for comprehensible, easy-to-read code.
On that note, please practice commenting your code in the scripts that you submit.
'''
