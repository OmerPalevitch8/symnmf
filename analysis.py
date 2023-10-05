import math
import sys
import numpy as np
import mysymnmf as sm
import pandas as pd

def main():
    np.random.seed(0)
    N = len(sys.argv)
    if (N == 2):
        path = sys.argv[1]
    else:
        print("An Error Has Occurred")
        return
    clusters1 = Hw1(path)
    # the m part is missing, need to use average of W
    file1_pd = pd.read_csv(path, header=None)
    n = file1_pd.shape[0]
    m = 0
    k = validateK(n)
    r = math.sqrt(m / k)
    H = np.random.uniform(low=0, high=r, size=(n, k))
    centroides = sm.symnmf(path, H, n)

if __name__ == "__main__":
    main()


def Hw1(path):
    arr = read_file(path)
    N = len(arr)
    try:
        K = validateK(N)
    except(AssertionError):
        print("Invalid number of clusters!")
        return
    iteration = 300
    try:
        clusters = k_means(K,iteration,arr)
    except(AssertionError):
        print("An Error Has Occurred")
        return
    return clusters



    #make sure k is valid
def validateK(N):
    try:
        k = float(sys.argv[0])
        if(k.is_integer()):
            k = int(k)
        else:
            assert 1 ==0
        if (k<1 or k>N):
            assert 1 ==0
    except:
        assert 1 == 0
    else:
        return k


def read_file(path):
    file = open(path,"r")
    line = file.readline()
    arr=[]
    while line.strip() != "":
        temp = []
        for word in line.split(","):
            temp.append(float(word))
        arr.append([tuple(temp)])
        line = file.readline()
    file.close()
    return arr


#calculate euclidean_distance
def euclidean_distance(p, q):
    dist = 0
    for i in range(len(p)):
        dist+=(p[i]-q[i])**2
    dist = dist**0.5
    return dist

def find_min_cluster(p,clusters):
    min_index = 0
    min_dist = euclidean_distance(p[0],clusters[0][0])
    for i in range(1,len(clusters)):
        dist = euclidean_distance(p[0],clusters[i][0])
        if(dist<min_dist):
            min_dist = dist
            min_index = i
    return min_index

def k_means(k,iter_max,arr):
    clusters = [0] * k
    #initialize clusters
    for i in range(k):
        clusters[i] = [arr[i][0],[]]
    smaller_then_eps = False
    iter_count = 0
    while(iter_count<iter_max and smaller_then_eps==False):
        for p in arr:
            index = find_min_cluster(p,clusters)
            if(len(p) !=1):
                clusters[p[1]][1].remove(p[0])
                p[1] = index
            else:
                p.append(index)
            clusters[index][1].append(p[0])
        smaller_then_eps = update_centroids(k,smaller_then_eps,clusters)
        iter_count+=1
    return clusters

def update_centroids(k,smaller_then_eps,clusters):
    eps = math.exp(-4)
    max_dist = 0
    for i in range(k):
        old_means= clusters[i][0]
        new_means = []
        for j in range(len(old_means)):
            cluster_size = len(clusters[i][1])
            sum1 = 0
            for k in clusters[i][1]:
                sum1+=k[j]
            new_means.append(sum1/cluster_size)
        clusters[i][0] = new_means
        dist = euclidean_distance(old_means,new_means)
        if dist>max_dist:
            max_dist = dist
    if(max_dist<eps):
        smaller_then_eps = True
    return smaller_then_eps
