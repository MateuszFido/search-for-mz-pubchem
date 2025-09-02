import pubchempy as pcp
import logging
from rdkit import Chem
from rdkit.Chem import Draw


logging.basicConfig(level=logging.DEBUG)


def main():
    list_of_compounds = ["taurocholic acid", "acetate"]

    for item in list_of_compounds:
        result = pcp.get_properties(
            ["SMILES", "MolecularFormula", "ExactMass"], item, namespace="name"
        )
        print(result)
        m = Chem.MolFromSmiles(result[0]["SMILES"])
        Draw.MolToFile(m, f"{item}.png")


if __name__ == "__main__":
    main()
