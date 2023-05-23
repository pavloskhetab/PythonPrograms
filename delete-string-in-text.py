# Created a python program to remove strings in a text filename

infile = "Project-replace.txt"
outfile = "Cleaned-project-replace.txt"

delete_list = ["Stuck? Get a hint"]
fin = open(infile, "rt", encoding='utf8')
fout = open(outfile, "w+")
for line in fin:
    for word in delete_list:
        line = line.replace(word, "")
    fout.write(line)
fin.close()
fout.close()
