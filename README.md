# Avian Influenza Genomics and Phylogenetics Comparison Tool

This Python program will perfom an analysis that is to be determined potentially including: sequence alignment, blast search, phylogenetic tree construction, and nucleotide and protein comparison. It may also display an interactive choropleth map.

## Features

- **Sequence Input**: The program can accept a nucleotide sequence either from a FASTA file or entered manually.
- **BLAST Search**: It connects to the NCBI BLAST service and performs a nucleotide BLAST search.
- **Sequence Alignment**: 
- **Phylogenetic Tree Construction**:
- **Nucleotide and Protein Comparison**:
- **Interactive Choropleth Map**:


## Installation

### Prerequisites

- **Python 3.8 or higher**

  
### Setting Up the Project

1. Clone this repository to your local machine:

```bash
git clone https://github.com/Debbie227/Avian_Influenza.git
cd Avian_Influenza
```
2. (Recommended) Create a virtual environment:

```bash
python -m venv venv

source venv/bin/activate    # On macOS/Linux
venv\Scripts\activate       # On Windows
```

3. Install dependencies:

The following Python libraries are required:
- `pandas` (>=1.3.0) for data manipulation and analysis
- `plotly` (>=5.0.0) for interactive visualizations
- `numpy` (>=1.21.0) for numerical operations
- `requests` (>=2.32.3) for http get operations
- `seaborn` (>=0.13.2) 
- `matplotlib` (>=3.10.0) 
- `bio` (>=1.7.1) 

```bash
pip install -r requirements.txt
```

### Usage

The program is run from the command line and accepts no arguments:

```bash
python Main.py
```

### Input:

- **input_sequence:** The nucleotide sequence to search. This can either be a FASTA file or a manually entered sequence.
    - If it's a file, use the dialog box to find select the file.
    - If it's a manually entered sequence, exit out of the dialog box and provide the sequence when prompted.

### Output:

- **To Be Determined**

### Example Usage:

1. Python 3.8 or above:

```bash
python Main.py
```



### Example Output Format:

To Be Determined

## Example Project Structure

```
├── LICENSE # License file for the project 
│
├── README.md # Project README with usage instructions 
│
├── Main.py # Main entry point for the program 
│
├── requirements.txt # Dependencies for the program 
│
├── Genetic_Analysis/ # Folder for genetic analysis scripts and resources 
│   │
│   ├── init.py # Marks this as a Python package
│
│   ├── MUSCLE.py # Multiple Sequence Alignment module
│
├── HPAI_maps/ # Folder for HPAI mapping and related functionalities 
│   │
│   ├── init.py # Marks this as a Python package 
│   │
│   ├── HPAI_map.py # Script for generating HPAI choropleth maps 
│   │
│   └── State_Conversion.py # Helper script for state name to abbreviation conversion 
│
├── Phylogenetics/ # Folder for phylogenetic analysis scripts and resources
│   │
│   ├── init.py # Marks this as a Python package 
│
├── Example_files/ # Folder for Example input
│   │
│   ├──H5_sequences.fasta  
│
├── Output_files/ # Folder for Output
│   │
│   ├──  
```

## Troubleshooting

- **No output generated:** Check if the input sequence is valid and ensure that Python is correctly installed.
- **Error in API connection:** Ensure that your system has internet access and the NCBI BLAST API is available.
- **Invalid input sequence:** If manually entering a sequence, ensure that it is in the correct nucleotide format (e.g., "ATGC").

## License

This project is licensed under the MIT License - see the [LICENSE](https://opensource.org/license/mit) file for details.
