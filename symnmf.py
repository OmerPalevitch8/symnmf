import math
import sys
import mysymnmf as sm
import numpy as np

def main():
    num_arg = len(sys.argv)
    if (num_arg != 4):
        print("An Error Has Occurred")
        return
    else:
        k = float(sys.argv[1])
        goal = sys.argv[2]
        text_file = sys.argv[3]
    file_mat = np.loadtxt(text_file)
    rows = file_mat.shape[0]
    col = file_mat.shape[0][0]
    if(goal == "symnmf"):
        np.random.seed(0)
        W = sm.norm(file_mat,rows,col)
        W_array = np.array((W))
        n = W_array.shape[0]
        m = np.mean(W_array)
        r = math.sqrt(m / k)
        H = np.random.uniform(low=0, high=r, size=(n, k))
        sm.symnmf(H,W,n,k)
        return
    elif(goal == "sym"):
        sm.sym(file_mat,rows,col)
    elif(goal == "dgd"):
        sm.dgd(file_mat,rows,col)
    elif(goal == "norm"):
        sm.norm(file_mat,rows,col)
    else:
        print("An Error Has Occurred")
        return

if __name__ == "__main__":
    main()
