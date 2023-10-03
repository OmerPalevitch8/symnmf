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
    file1_pd = pd.read_csv(text_file, header=None)
    n = file1_pd.shape[0]
    if(goal == "symnmf"):
        np.random.seed(0)
        # the m part is missing, need to use average of W
        m = 0
        r = math.sqrt(m / k)
        H = np.random.uniform(low=0, high=r, size=(n, k))
        centroides = sm.symnmf(file1_pd,H,n)
        for centroid in centroides:
            print(",".join(["%.4f" % x for x in centroid]))
        return
    elif(goal == "sym"):
        centroides = sm.sym(file1_pd)
    elif(goal == "dgd"):
        centroides = sm.dgd(file1_pd)
    elif(goal == "norm"):
        centroides = sm.norm(file1_pd)
    else:
        print("An Error Has Occurred")
        return
    for centroid in centroides:
        print(",".join(["%.4f" % x for x in centroid]))
    return

if __name__ == "__main__":
    main()
