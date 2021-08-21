from Bio import Entrez

class GBSeq():
    """description of class"""
    def __init__(self, trm):
        self.trm = trm

    def gbSeq():
        Entrez.email = 'alspok@gmail.com'
        handle = Entrez.esearch(db = 'nucleotide', term = trm)
        record = Entrez.read(handle)


