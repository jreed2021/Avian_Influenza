#!/usr/bin/env python3

from Bio import SeqIO, AlignIO
from collections import Counter

"""
File name: seq_frequency.py
Author: Debra Pacheco
Created: 02/01/25
Version: 1.0
Description:
    This script will generate a dictionary of containing the counts of amino acids at each postion from a multiple sequence
    alignment.

License: MIT License
"""

# Define file paths
msa_file = "clustalo-I20250131-012913-0270-28960768-p1m.fa"

# Load the alignment
alignment = AlignIO.read(msa_file, "fasta")

# List of accession numbers from human hosts
human_accessions = []
with open ("HumanAcessions.fa") as file:
    for line in file:
        line = file.readline()
        human_accessions.append(line.strip())

#print(human_accessions)

# Separate human and animal sequences
human_seqs = []
animal_seqs = []

for record in alignment:
    accession = record.id
    if accession in human_accessions:
        human_seqs.append(record.seq)
    else:
        animal_seqs.append(record.seq)

#print(human_seqs)


# Identify differences at each position
sequence_length = len(alignment[0].seq)
substitutions = {}

for pos in range(sequence_length):
    column = [record.seq[pos] for record in alignment]
    freq = Counter(column)

    if len(freq) > 1:  # Only consider variable positions
        substitutions[pos + 1] = freq  # Store as 1-based index


# List other frequently changed positions
for pos, freq in substitutions.items():
    print(f"Position {pos}: {freq}")

