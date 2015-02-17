# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 11:24:42 2014

@author: Rebecca Jordan
            Greenlightrj

"""

# you may find it useful to import these variables (although you are not required to use them)
from amino_acids import aa, codons, aa_table
import random
from load import load_seq


def shuffle_string(s):
    """ Shuffles the characters in the input string
        NOTE: this is a helper function, you do not have to modify this in any way """
    return ''.join(random.sample(s,len(s)))

### YOU WILL START YOUR IMPLEMENTATION FROM HERE DOWN ###


def get_complement(nucleotide):
    """ Returns the complementary nucleotide

        nucleotide: a nucleotide (A, C, G, or T) represented as a string
        returns: the complementary nucleotide
        these unit tests check all valid inputs and ensure the function doesn't break with invalid input

    >>> get_complement('A')
    'T'
    >>> get_complement('C')
    'G'
    >>> get_complement('T')
    'A'
    >>> get_complement('G')
    'C'
    >>> get_complement('echidna')
    echidna is not a nucleotide
    """
    if nucleotide == 'A':
        return 'T'
    elif nucleotide == 'T':
        return 'A'
    elif nucleotide == 'C':
        return 'G'
    elif nucleotide == 'G':
        return 'C'
    else:
        print nucleotide + ' is not a nucleotide'


def get_reverse_complement(dna):
    """ Computes the reverse complementary sequence of DNA for the specfied DNA
        sequence
    
        dna: a DNA sequence represented as a string
        returns: the reverse complementary DNA sequence represented as a string
        these unit tests check two normal inputs using every letter, and two inputs
         of unusual length. The function breaks if the input is something other than ACTGs
    >>> get_reverse_complement("ATGCCCGCTTT")
    'AAAGCGGGCAT'
    >>> get_reverse_complement("CCGCGTTCA")
    'TGAACGCGG'
    >>> get_reverse_complement('A')
    'T'
    >>> get_reverse_complement('')
    ''

    """
    reverse = ''
    for i in range(0, len(dna)):
        reverse += get_complement(dna[i])
    reverse = reverse[::-1]
    return reverse


def rest_of_ORF(dna):
    """ Takes a DNA sequence that is assumed to begin with a start codon and returns
        the sequence up to but not including the first in frame stop codon.  If there
        is no in frame stop codon, returns the whole string.
        
        dna: a DNA sequence
        returns: the open reading frame represented as a string
        the unit tests test three normal scenarios (one for each stop codon) 
        and the cases of an empty ORF and a missing stop codon and length that isn't a multiple of three. stop codons shifted by 1 in the tests prove that only stop codons aligned with the start codon work.
    >>> rest_of_ORF("ATGTGAA")
    'ATG'
    >>> rest_of_ORF("ATGAGATAGG")
    'ATGAGA'
    >>> rest_of_ORF("ATAGCCACGTAA")
    'ATAGCCACG'
    >>> rest_of_ORF("TACCCGCA")
    'TACCCGCA'
    >>> rest_of_ORF("TAG")
    ''
    """
    orf = ''
    for i in range(0, 1+len(dna)//3):
        if dna[3*i: 3*i+3] in ('TAG', 'TAA', 'TGA'):
            break
        elif 3*i + 3 > len(dna):
            orf += dna[3*i:len(dna)]
        else:
            orf += dna[3*i: 3*i+3]
    return orf


def find_all_ORFs_oneframe(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence and returns
        them as a list.  This function should only find ORFs that are in the default
        frame of the sequence (i.e. they start on indices that are multiples of 3).
        By non-nested we mean that if an ORF occurs entirely within
        another ORF, it should not be included in the returned list of ORFs.

        dna: a DNA sequence
        returns: a list of non-nested ORFs

        the first unit test checks the output of multiple ORFs and that the reading frame is maintained
        the second checks that nested ORFs are not included and that end-to-end ORFs are read, even when they are length 1
    >>> find_all_ORFs_oneframe("ATGCATGAATGTAGATAGATGTGCCC")
    ['ATGCATGAATGTAGA', 'ATGTGCCC']
    >>> find_all_ORFs_oneframe("ATGCGGATGTCCTAAATGTGAATGGGGTAG")
    ['ATGCGGATGTCC', 'ATG', 'ATGGGG']

    """
    i = 0
    orfs = []
    while i <= len(dna)-3:
        if dna[i:i + 3] == "ATG":
            orfs.append(rest_of_ORF(dna[i:len(dna)]))
            i += len(rest_of_ORF(dna[i:len(dna)]))
        else:
            i += 3
    return orfs


def find_all_ORFs(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence in all 3
        possible frames and returns them as a list.  By non-nested we mean that if an
        ORF occurs entirely within another ORF and they are both in the same frame,
        it should not be included in the returned list of ORFs.

        dna: a DNA sequence
        returns: a list of non-nested ORFs
        this unit test checks that orfs from all three potential reading frames are returned.
    >>> find_all_ORFs("ATGCATGAATGTAG")
    ['ATGCATGAATGTAG', 'ATGAATGTAG', 'ATG']
    """
    orfs = []
    for i in range(0, 3):
        result = (find_all_ORFs_oneframe(dna[i:len(dna)]))
        for i in range (0, len(result)):
            orfs.append(result.pop(0))
    return orfs


def find_all_ORFs_both_strands(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence on both
        strands.

        dna: a DNA sequence
        returns: a list of non-nested ORFs
        this unit test checks orfs in both the backward and forward directions, and that they are returned in the correct order and format.
    >>> find_all_ORFs_both_strands("ATGCGAATGTAGCATCAAA")
    ['ATGCGAATG', 'ATGCTACATTCGCAT']
    """
    otherstrand = get_reverse_complement(dna)
    orfs = []
    firstorfs = find_all_ORFs(dna)
    secondorfs = find_all_ORFs(otherstrand)
    for i in range(0, len(firstorfs)):
        orfs.append(firstorfs.pop(0))
    for i in range(0, len(secondorfs)):
        orfs.append(secondorfs.pop(0))
    return orfs

#end of first week assignment


def longest_ORF(dna):
    """ Finds the longest ORF on both strands of the specified DNA and returns it
        as a string
    the first unit test checks a normal case
    the second checks the case in which the two longest orfs are the same length
    the third checks the case in which there is only one orf (and it is length 1)
    the fourth checks the case in which there are no orfs
    >>> longest_ORF("ATGCGAATGTAGCATCAAA")
    'ATGCTACATTCGCAT'
    >>> longest_ORF("ATGGATCCCGCCTAGGTA")
    'ATGGATCCCGCC'
    >>> longest_ORF("ATGTAG")
    'ATG'
    >>> longest_ORF("CCCGCT")
    ''
    """
    allorfs = (find_all_ORFs_both_strands(dna))
    allorfs = sorted(allorfs, key=len)
    allorfs.reverse()
    if len(allorfs)>0:
        return allorfs.pop(0)
    else:
        return ''


def longest_ORF_noncoding(dna, num_trials):
    """ Computes the maximum length of the longest ORF over num_trials shuffles
        of the specfied DNA sequence

    dna: a DNA sequence
    num_trials: the number of random shuffles
    returns: the maximum length longest ORF
    this function can't really be unit tested 
    """
    longests=[]
    for i in range(1, num_trials):
        shuffled=shuffle_string(dna)
        longests.append(longest_ORF(shuffled))
    longests = sorted(longests, key=len)
    longests.reverse()
    return len(longests.pop(0))


def coding_strand_to_AA(dna):
    """ Computes the Protein encoded by a sequence of DNA.  This function
        does not check for start and stop codons (it assumes that the input
        DNA sequence represents an protein coding region).

    dna: a DNA sequence represented as a string
    returns: a string containing the sequence of amino acids encoded by the
             the input DNA fragment
    these unit tests check fragments of both proper and improper length
    it would not be worth it to test every single amino acid.
    >>> coding_strand_to_AA("ATGCGA")
    'MR'
    >>> coding_strand_to_AA("ATGCCCGCTTT")
    'MPA'
    """
    i = 3
    protein = ''
    while i <= len(dna):
        nextcodon = dna[i-3:i]
        protein += aa_table[nextcodon]
        i += 3
    return protein


def gene_finder(dna):
<<<<<<< HEAD
    """ Returns the amino acid sequences coded by all genes that have an ORF
        larger than the specified threshold.

        dna: a DNA sequence
        threshold: the minimum length of the ORF for it to be considered a valid
                   gene.
        returns: a list of all amino acid sequences whose ORFs meet the minimum
                 length specified.
        this unit test just checks that the function is working for a reasonable input
        >>> gene_finder('ATGCCGATCAAACATCACGCGCGCGGGCTCGTGCACGAGTAG')
        []
=======
    """ Returns the amino acid sequences that are likely coded by the specified dna
        
        dna: a DNA sequence
        returns: a list of all amino acid sequences coded by the sequence dna.
>>>>>>> 922a6e32441860ab0413630f74531e6e47a16a7c
    """
    threshold = longest_ORF_noncoding(dna, 1500)
    orfs = find_all_ORFs_both_strands(dna)
    longorfs = []
    proteins = []
    for element in orfs:
        if len(element) >= threshold:
            longorfs.append(element)
        else:
            pass
    for element in longorfs:
        proteins.append(coding_strand_to_AA(element))
    return proteins

if __name__ == "__main__":
    import doctest
    doctest.testmod()

dna = load_seq('./data/X73525.fa')
print gene_finder(dna)
