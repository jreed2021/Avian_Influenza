#!/usr/bin/env python3

from HPAI_maps import HPAI_map
import time

"""
File name: Main.py
Author: Debra Pacheco
Created: 1/25/25
Version: 1.0
Description:
    This script will run the Avian Influenza Genomics and Phylogenetics Comparison Tool and will allow the user to
    choose what analysis to run as well as input data if required.

License: MIT License
"""
def main():
    print("     Welcome to the Avian Influenza Genomics and Phylogenetics Comparison Tool!!")
    print("        *******************************************************************        ")
    print("  This program is under construction and has limited capabilities. Please be patient.")
    print("        *******************************************************************        ")

    choice = 0

    while choice != "4":

        print("                    Please choose from the following options.\n")

        print("1. Generate Avian Influenza in Mammals Map")
        print("2. Generate Phylogenetic Tree")
        print("3. Generate Nucleotide Comparison")
        print("4. Exit\n")

        choice = input("Enter your choice: ")

        if choice == "1":
            fig = HPAI_map.generate_map()
            fig.show()
        elif choice == "2":
            print("This is not currently available.\n")
            time.sleep(1)
        elif choice == "3":
            print("This is not currently available.\n")
            time.sleep(1)
        elif choice == "4":
            print("Exiting program. Goodbye!")
        else:
            print("Invalid choice. Please try again.\n")
            time.sleep(1)


if __name__ == "__main__":
    main()
