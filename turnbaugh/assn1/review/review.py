#/usr/bin/python

seqs = open('seqs.fa','r')

#solution type 1

# for line in seqs:
#     if '>' in line:
#         print (line[1:])

#solution type 2
        
for line in seqs:
    if line.startswith('>'):
        seqid = line.split('>')
        print seqid[1]





'''
review:

-commenting is a good habit

-file handle can be named anything, except python keywords 
-same for line iterator

-string slicing uses indices of characters in a string

-string splitting based on a delimter returns a list

'''