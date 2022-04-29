import Bio
from Bio import SeqIO
from Bio import Entrez

Entrez.email = "izambrano19@ilg.cat"

#handle = Entrez.einfo()
#result = handle.read()
#handle.close()
#print(result)

handle = Entrez.einfo()
record = Entrez.read(handle)
print(record.keys())
#llista = record.keys()
#print(llista)
print(record["DbList"])

llista = record['DbList']
llista2 = record.values()

for bbdd in llista:
    print(bbdd)
#record["DbList"]