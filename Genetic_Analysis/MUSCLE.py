#!/usr/bin/env python3

import os
import subprocess

"""
File name: MUSCLE.py
Author: Victoria, Debra Pacheco
Created: 1/28/25
Version: 1.0
Description:
    This script pulls the muscle biocontainer from DockerHub and runs an alignment on the Example fasta file.
    
    Requirement: Docker installed
    
    input: fasta file
    output: fasta alignment

License: MIT License
"""

# Get the absolute path to the project root
project_root = os.path.dirname(os.path.abspath(__file__))

# Define input and output file paths using os.path.join() for cross-platform compatibility
input_file = os.path.join(project_root, "Example_files", "H5_sequences.fasta")
output_file = os.path.join(project_root, "Output_files", "H5_Aligned.fasta")

# Define the Docker image name
image_name = "biocontainers/muscle:v1-3.8.1551-2-deb_cv1"

# Run MUSCLE inside the Docker container
try:
    subprocess.run([
        "docker", "run", "--rm",
        "-v", f"{input_file}:/input.fasta",  # Mount input file
        "-v", f"{output_file}:/output.fasta",  # Mount output file
        image_name,
        "muscle", "-align", "/input.fasta", "-output", "/output.fasta"
    ], check=True)

    print(f"Alignment complete! Output saved to: {output_file}")

except subprocess.CalledProcessError as e:
    print("Error running MUSCLE:", e)
except FileNotFoundError:
    print("Docker is not installed or not in PATH. Please check your Docker setup.")
except Exception as e:
    print("An unexpected error occurred:", e)