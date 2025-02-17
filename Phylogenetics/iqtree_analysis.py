"""
File Name: iqtree_analysis.py
Author: Janessa Reed
Created: 2/17/2024
Version: 1.0

License: MIT License
"""

import subprocess

# Define the command to run IQ-TREE
iqtree_command = [
    "iqtree2",
    "-s", "H5_Aligned_Official_fixed.fasta",  # Alignment file
    "-m", "GTR+I+G",  # Best-fit model
    "-bb", "1000",  # Bootstrap analysis with 1000 replicates
    "-alrt", "1000"  # Approximate Likelihood Ratio Test
]

# Run the command
try:
    print("Running IQ-TREE analysis...")
    subprocess.run(iqtree_command, check=True)
    print("IQ-TREE analysis completed successfully!")

except subprocess.CalledProcessError as e:
    print("Error during IQ-TREE execution:", e)

