class DNASequence(object):
    """ Represents a sequence of DNA """
    def __init__(self, nucleotides):
        """ constructs a DNASequence with the specified nucleotides.
             nucleotides: the nucleotides represented as a string of
                          capital letters consisting of A's, C's, G's, and T's """
        self.nucleotides = nucleotides


    def __str__(self):
        """ Returns a string containing the nucleotides in the DNASequence
        >>> seq = DNASequence("TTTGCC")
        >>> print seq
        TTTGCC
        """
        return self.nucleotides


    def get_reverse_complement(self):
        """ Returns the reverse complement DNA sequence represented
            as an object of type DNASequence

            >>> seq = DNASequence("ATGC")
            >>> rev = seq.get_reverse_complement()
            >>> print rev
            GCAT
            >>> print type(rev)
            <class '__main__.DNASequence'>
        """

        def get_complement(n):
            if n == 'A':
                return 'T'
            elif n == 'T':
                return 'A'
            elif n == 'C':
                return 'G'
            elif n == 'G':
                return 'C'

        tides = ''
        for i in range(1, len(self.nucleotides)+1):
            tides += get_complement(self.nucleotides[-i])
        rev = DNASequence(tides)
        return rev


    def get_proportion_ACGT(self):
        """ Computes the proportion of nucleotides in the DNA sequence
            that are 'A', 'C', 'G', and 'T'
            returns: a dictionary where each key is a nucleotide and the
                corresponding value is the proportion of nucleotides in the
            DNA sequence that are that nucleotide.
            (NOTE: this doctest will not necessarily always pass due to key
                    re-ordering don't worry about matching the order)
        >>> seq = DNASequence("AAGAGCGCTA")
        >>> d = seq.get_proportion_ACGT()
        >>> print (d['A'], d['C'], d['G'], d['T'])
        (0.4, 0.2, 0.3, 0.1)
        """
        dic = {'A': 0, 'C': 0, 'G': 0, 'T':0}
        for n in self.nucleotides:
            dic[n] += 1
        for n in 'ACGT':
            dic[n] = dic[n]*1.0/len(self.nucleotides)
        return dic

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    test = DNASequence('ATGC')
    rev = test.get_reverse_complement()
