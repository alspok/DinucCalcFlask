from Bio import Entrez

class GBEntrez():
    def __init__(self, gbentrez):
        self.gbentrez = gbentrez

    def gbSearchResult(self):
        Entrez.email = "alspok@gmail.com"
        handle = Entrez.efetch(db = 'nucleotide', rettype='gb', id = self.gbentrez, retmode = 'text')
        
        return handle.read()

