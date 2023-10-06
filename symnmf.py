import math
import sys
import mysymnmf as sm
import numpy as np
import pandas as pd

def main():
    num_arg = len(sys.argv)
    if (num_arg != 4):
        print("An Error Has Occurred")
        return
    else:
        k = float(sys.argv[1])
        goal = sys.argv[2]
        text_file = sys.argv[3]
    file_mat = pd.read_csv(text_file,header=None).values.tolist()
    rows = len(file_mat[0]) if (file_mat is not None) else 0
    col = len(file_mat) if (file_mat is not None) else 0
    if(goal == "symnmf"):
        np.random.seed(0)
        W = sm.norm(file_mat,rows,col)
        m = np.mean(W)
        r = math.sqrt(m / k)
        H = np.random.uniform(low=0, high=r, size=(col, k))
        H_new = sm.symnmf(H,W,n,k)
        print_matrix(H_new)
        return
    elif(goal == "sym"):
        A = sm.sym(file_mat,rows,col)
        print_matrix(A)
    elif(goal == "dgd"):
        D = sm.dgd(file_mat,rows,col)
        print_matrix(D)
    elif(goal == "norm"):
        W = sm.norm(file_mat,rows,col)
        print_matrix(W)
    else:
        print("An Error Has Occurred")
        return
def print_matrix(matrix):
    for row in matrix:
        row_round= [f'{item:.4f}' for item in row]
        print(','.join(row_round))

if __name__ == "__main__":
    main()
