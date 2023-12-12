def get_valence_electrons(element_symbol):
    # Define the periodic table with elements and their corresponding valence electrons
    periodic_table = {
        'H': 1, 'He': 2,
        'Li': 1, 'Be': 2,
        'B': 3, 'C': 4, 'N': 5, 'O': 6, 'F': 7, 'Ne': 8,
        'Na': 1, 'Mg': 2,
        'Al': 3, 'Si': 4, 'P': 5, 'S': 6, 'Cl': 7, 'K': 1, 'Ar': 8,
        'Ca': 2, 'Sc': 3, 'Ti': 4, 'V': 5, 'Cr': 6, 'Mn': 7, 'Fe': 8, 'Ni': 8, 'Co': 7, 'Cu': 9, 'Zn': 10,
        'Ga': 3, 'Ge': 4, 'As': 5, 'Se': 6, 'Br': 7, 'Kr': 8,
        'Rb': 1, 'Sr': 2,
        'Y': 3, 'Zr': 4, 'Nb': 5, 'Mo': 6, 'Tc': 7, 'Ru': 8, 'Rh': 9, 'Pd': 10, 'Ag': 11, 'Cd': 12,
        'In': 3, 'Sn': 4, 'Sb': 5, 'Te': 6, 'I': 7, 'Xe': 8,
        'Cs': 1, 'Ba': 2,
        'La': 3, 'Ce': 4, 'Pr': 5, 'Nd': 6, 'Pm': 7, 'Sm': 8, 'Eu': 9, 'Gd': 10, 'Tb': 11, 'Dy': 12, 'Ho': 13, 'Er': 14, 'Tm': 15, 'Yb': 16, 'Lu': 17,
        'Hf': 4, 'Ta': 5, 'W': 6, 'Re': 7, 'Os': 8, 'Ir': 9, 'Pt': 10, 'Au': 11, 'Hg': 12,
        'Tl': 3, 'Pb': 4, 'Bi': 5, 'Th': 3, 'Pa': 4, 'U': 3, 'Np': 4, 'Pu': 4, 'Am': 4, 'Cm': 4, 'Bk': 4, 'Cf': 4, 'Es': 4, 'Fm': 4, 'Md': 4, 'No': 4, 'Lr': 4,
        # Add more elements as needed
    }

    # Convert the input to uppercase to handle case-insensitivity
    element_symbol = element_symbol.capitalize()

    # Check if the element is in the periodic table
    if element_symbol in periodic_table:
        return periodic_table[element_symbol]
    else:
        return None

# Example usage:
element_symbol = input("Enter the element symbol: ")
valence_electrons = get_valence_electrons(element_symbol)

if valence_electrons is not None:
    print(f"The number of valence electrons for {element_symbol} is {valence_electrons}.")
else:
    print(f"Element {element_symbol} not found in the periodic table.")
