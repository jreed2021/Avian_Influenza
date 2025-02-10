#!/usr/bin/env python3

from Bio import Phylo
from Bio.Phylo.TreeConstruction import DistanceTreeConstructor, DistanceMatrix
from Bio import AlignIO
from Bio.Phylo.TreeConstruction import DistanceCalculator
import matplotlib.pyplot as plt

"""
File name: build_tree.py
Author: Janessa Reed
Created: 02/04/25
Version: 1.0
Description:
    

License: MIT License
"""

# Load the alignment
alignment = AlignIO.read("H5_Aligned_Official (3).fasta", "fasta")

# Compute pairwise distances
calculator = DistanceCalculator("identity")
dm = calculator.get_distance(alignment)

# Construct a UPGMA tree
constructor = DistanceTreeConstructor()
tree = constructor.nj(dm)  # Neighbor-Joining method

# Save the tree in Newick format
#Phylo.write(tree, "H5_tree_upgma.nwk", "newick")

# Display ASCII tree
print("\nUPGMA Phylogenetic Tree:\n")
Phylo.draw_ascii(tree)

# Graphical visualization
plt.figure(figsize=(10, 8))
Phylo.draw(tree, do_show=False)
#plt.savefig("H5_tree_upgma.png")
#print("\nTree saved as H5_tree_upgma.png")
