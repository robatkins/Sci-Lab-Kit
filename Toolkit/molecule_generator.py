from rdkit import Chem
from rdkit.Chem import AllChem

def generate_molecules(atoms, max_atoms_per_molecule):
    molecules = []
    for i in range(1, max_atoms_per_molecule + 1):
        combinations = product(atoms, repeat=i)
        for combination in combinations:
            molecule_string = ''.join(combination)
            if is_valid_molecule(molecule_string):
                molecules.append(molecule_string)
    return molecules

def is_valid_molecule(molecule_string):
    mol = Chem.MolFromSmiles(molecule_string)
    if mol is not None:
        try:
            # Perform a sanitization check to ensure the molecule is valid
            Chem.SanitizeMol(mol)
            return True
        except ValueError:
            return False
    return False

if __name__ == "__main__":
    from itertools import product

    # Take user input for base atoms
    atoms_input = input("Enter base atoms separated by spaces (e.g., H O C): ")
    base_atoms = atoms_input.split()

    # Take user input for the maximum number of atoms per molecule
    max_atoms_per_molecule = int(input("Enter the maximum number of atoms per molecule: "))

    # Generate molecules
    generated_molecules = generate_molecules(base_atoms, max_atoms_per_molecule)

    # Print the generated molecules
    print("Generated Molecules:")
    for molecule in generated_molecules:
        print(molecule)
