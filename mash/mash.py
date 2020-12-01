#!/usr/bin/env python

import numpy as np
import pandas as pd
from skbio import DistanceMatrix
from skbio.tree import nj

def parse_triangle(file):
    with open(file, 'r') as file:
        num_samples = int(file.readline().strip())

        rows = []
        names = []

        for line in file:
            line = line.strip()
            tokens = line.split('\t')

            # Remove sample name
            name = tokens.pop(0)

            # Pad rest of row with '0'
            tokens.extend([0] * (num_samples - len(tokens)))

            rows.append(tokens)
            names.append(name)

        matrix = np.matrix(rows).astype('float64')

        # Restore to full matrix instead of triangular matrix
        matrix = matrix + matrix.transpose()

        return pd.DataFrame(matrix, index=names, columns=names)
    
def build_tree(input_file: str, output_file: str):
    matrix_df = parse_triangle(input_file)
    matrix = DistanceMatrix(matrix_df.to_numpy(), matrix_df.index)

    # Write tree to file
    nj_tree = nj(matrix, result_constructor=str)
    with open(output_file, 'w') as f:
        f.write(nj_tree)