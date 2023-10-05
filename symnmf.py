import math
import sys
import pandas as pd
import mysymnmf as sm
import numpy as np

def main():
    num_arg = len(sys.argv)
    if (num_arg != 3):
        print("An Error Has Occurred")
        return
    else:
        k = float(sys.argv[0])
        goal = sys.argv[1]
        text_file = sys.argv[2]
    if(goal == "symnmf"):
        np.random.seed(0)
        W = sm.norm(text_file)
        W_array = np.array((W))
        n = W_array.shape[0]
        m = np.mean(W_array)
        # the m part is missing, need to use average of W
        r = math.sqrt(m / k)
        H = np.random.uniform(low=0, high=r, size=(n, k))
        sm.symnmf(text_file,H,W)
        return
    elif(goal == "sym"):
        sm.sym(text_file)
    elif(goal == "dgd"):
        sm.dgd(text_file)
    elif(goal == "norm"):
        sm.norm(text_file)
    else:
        print("An Error Has Occurred")
        return

if __name__ == "__main__":
    main()
