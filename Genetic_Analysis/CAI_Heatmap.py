#!/usr/bin/env python3

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from Bio import SeqIO
from Calculate_CAI import calculate_cai

"""
File name: CAI_Heatmap.py
Author: Victoria, Debra Pacheco
Created: 1/30/25
Version: 1.0
Description:
    This script displays an HAI heatmap of codon bias across different Influenza A H5 strains through the HA gene.

License: MIT License
"""

##########
# Data Manipulation #
##########

# Load CAI default data
default_cai_data = pd.DataFrame(columns=["ID", "CAI"])
default_cai_data = pd.read_csv("H5_CAI_Results_Influenza.csv")


# Option to add user data
answer = "0"
user_data = ""

while answer != "N" and answer != "Y":
    answer = input("Would you like to add you own FASTA data? Y/N\n")
    if answer.upper() == "Y":
        user_data = input("Please enter the FASTA file.")
    if answer.upper() == "N":
        print("User data not included. Generating map.\n")
        break
    else:
        print("Invalid choice.\nWould you like to enter data? Please choose Y for yes or N for no.\n")

# CAI calculation of user data.

if user_data != "":
    with open(user_data) as fasta_file:
        for record in SeqIO.parse(fasta_file, "fasta"):
            ID = record.id
            User_CAI = calculate_cai(str(record.seq))
            new_row = pd.DataFrame([{"Accession": ID, "CAI": User_CAI}])
            default_cai_data = pd.concat([default_cai_data, new_row], ignore_index=True)


##########
# Heatmap generation #
##########


#print(default_cai_data.head())

# Ensure Accession IDs are strings and limit length
default_cai_data["Accession"] = default_cai_data["Accession"].astype(str).str[:10]

# Set Accession as index
default_cai_data = default_cai_data.reset_index().set_index("Accession")

# Create heatmap
plt.figure(figsize=(6, 10))
sns.heatmap(default_cai_data, cmap="coolwarm", annot=True, linewidths=0.5, fmt=".4f")

# Titles and labels
plt.title("Codon Adaptation Index (CAI) Heatmap for H5 Strains")
plt.xlabel("CAI Score")
plt.ylabel("Accession Numbers")

# Save and display
# plt.savefig("H5_CAI_Heatmap.png", dpi=300, bbox_inches="tight")
plt.show()
