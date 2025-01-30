#!/usr/bin/env python3

import math

"""
File name: Calculate_CAI.py
Author: Victoria, Debra Pacheco
Created: 1/30/25
Version: 1.0
Description:
    This script calculates the CAI value for influenza A viruses.

License: MIT License
"""

# Influenza-specific codon usage table (from Kazusa database)
influenza_codon_usage = {
    "TTT": 20.7, "TTC": 20.5, "TTA": 11.0, "TTG": 10.8,
    "CTT": 11.4, "CTC": 9.1, "CTA": 7.1, "CTG": 11.1,
    "ATT": 16.5, "ATC": 14.7, "ATA": 4.9, "ATG": 22.4,
    "GTT": 12.5, "GTC": 11.3, "GTA": 5.9, "GTG": 14.7,
    "TAT": 15.3, "TAC": 15.4, "TAA": 1.2, "TAG": 0.3,
    "CAT": 7.3, "CAC": 7.1, "CAA": 11.2, "CAG": 14.9,
    "AAT": 21.3, "AAC": 21.2, "AAA": 29.1, "AAG": 28.1,
    "GAT": 24.2, "GAC": 25.1, "GAA": 29.3, "GAG": 27.3,
    "TCT": 14.1, "TCC": 14.2, "TCA": 12.8, "TCG": 6.5,
    "CCT": 8.5, "CCC": 6.3, "CCA": 10.2, "CCG": 4.3,
    "ACT": 14.1, "ACC": 15.2, "ACA": 13.0, "ACG": 6.1,
    "GCT": 16.1, "GCC": 17.5, "GCA": 14.1, "GCG": 8.2,
    "TGT": 6.2, "TGC": 6.7, "TGA": 0.5, "TGG": 13.3,
    "CGT": 6.2, "CGC": 6.4, "CGA": 4.0, "CGG": 4.9,
    "AGT": 12.1, "AGC": 12.7, "AGA": 5.3, "AGG": 5.2,
    "GGT": 11.8, "GGC": 14.3, "GGA": 10.4, "GGG": 9.1}


def calculate_cai(sequence):
    codons = [sequence[i:i + 3] for i in range(0, len(sequence), 3) if len(sequence[i:i + 3]) == 3]
    valid_codons = [influenza_codon_usage[c] for c in codons if c in influenza_codon_usage]

    if not valid_codons:
        return 0  # Avoid division by zero

    cai_value = math.exp(sum(math.log(w) for w in valid_codons) / len(valid_codons))
    return round(cai_value, 4)
