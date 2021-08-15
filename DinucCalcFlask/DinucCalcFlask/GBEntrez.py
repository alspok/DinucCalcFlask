from Bio import Entrez, SeqIO

class GBEntrez():
    """ """
    def __init__(self, gbentrez):
        self.gbentrez = gbentrez

    def gbSearchResult(self):
        Entrez.email = "alspok@gmail.com"
        handle = Entrez.efetch(db = 'nucleotide', rettype='fasta', id = self.gbentrez, retmode = 'text')
        record = SeqIO.read(handle, 'fasta')
        handle.close()

        return record

