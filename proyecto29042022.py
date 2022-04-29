import Bio
from Bio import SeqIO
from Bio import Entrez

Entrez.email = "izambrano19@ilg.cat"

#handle = Entrez.einfo()
#result = handle.read()
#handle.close()
#print(result)

# handle = Entrez.einfo()
# record = Entrez.read(handle)
#print(record.keys())
#llista = record.keys()
#print(llista)
#print(record["DbList"])

# llista = record['DbList']
#llista2 = record.values()

# for bbdd in llista:
#     print(bbdd)
#     handle = Entrez.einfo(db=bbdd)
#     record2 = Entrez.read(handle)
#     print(record2.keys())
#     print(record2['DbInfo']['Description'])
# #record["DbList"]

# Buscar con esearch 10 ids de nucleotidos con el termino asthma

handle = Entrez.esearch(db="nucleotide", term="asthma", retmax="10")
record = Entrez.read(handle)
llista = record['IdList']

print(record)
print(llista)

##ESTO NO RULA
# for id in llista:
#     handle = Entrez.esearch(db ='nucleotide', term=id)
#     for rec in SeqIO.parse(handle,"genbank"):
#         record = Entrez.read(handle)
#         print(record)

handle2 = Entrez.efetch(db='nucleotide', id="NM_001354619.2", rettype="gb", retmode="text")
record2 = Entrez.read(handle2)
print(record2[0])