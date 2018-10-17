"""
Contains components for representing sequences with the SequenceParameter

@author Lukas Zimmermann
"""
from Bio import SeqIO


class SequenceFileStats:
    """
    Collects some statistics on a Sequence File, using Biopythons SeqIO Module
    """
    def __init__(self, number_of_chars: int, number_of_sequences: int):
        self.number_of_chars = number_of_chars
        self.number_of_sequences = number_of_sequences

    @staticmethod
    def from_file(file_path: str, file_format: str):
        n_chars = 0
        n_seqs = 0
        for record in SeqIO.parse(file_path, file_format):
            n_seqs += 1
            n_chars += (len(record.seq) + len(record.id))
        return SequenceFileStats(n_chars, n_seqs)
