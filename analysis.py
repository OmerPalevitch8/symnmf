import math
import sys
import numpy as np
#import mysymnmf as sm
from sklearn.metrics import silhouette_score

def main():
    np.random.seed(0)
    N = len(sys.argv)
    if (N == 3):
        k = float(sys.argv[1])
        if (k.is_integer()):
            k = int(k)
        path = sys.argv[2]
    else:
        print("An Error Has Occurred")
        return
    points_nmf = read_file_nmf(path)
    centroids_kmean = Hw1(k,points_nmf)
    clusters_kmean_label = find_clusters(points_nmf,k,centroids_kmean)
    rows = len(points_nmf[0])
    col = len(points_nmf)
    #W = sm.norm(file_mat, rows, col)
    path_norm = "C:/Users/omer.pa/Desktop/school/third_year/second_semester/Software_project/symnmf/norm.txt"
    W=read_file_nmf(path_norm)
    W_array = np.array(W)
    n = W_array.shape[0]
    m = np.mean(W_array)
    r = math.sqrt(m / k)
    H = np.random.uniform(low=0, high=r, size=(n, k))
    #H_new = sm.symnmf(H, W, n, k)
    H_path = "C:/Users/omer.pa/Desktop/school/third_year/second_semester/Software_project/symnmf/H_path.txt"
    H_new = read_file_nmf(H_path)
    H_new_pd = np.array(H_new)
    labels_nmf = np.argmax(H_new_pd, axis=1)
    Sil_symnmf = silhouette_score(points_nmf,labels_nmf)
    Sil_kmeans = silhouette_score(points_nmf,clusters_kmean_label)
    print("nmf: " + str(round(Sil_symnmf,4)))
    print("kmeans: " + str(round(Sil_kmeans,4)))


def add_to_clusters(cluster_num,row,clusters):
    for i in range(len(row)):
        clusters[cluster_num].append(row[i])

def Hw1(k,points):
    iteration = 300
    try:
        centroids = k_means(k,iteration,points)
    except(AssertionError):
        print("An Error Has Occurred")
        return
    return centroids

def read_file_nmf(path):
    file = open(path,"r")
    line = file.readline()
    arr=[]
    while line.strip() != "":
        temp = []
        for word in line.split(","):
            temp.append(float(word))
        arr.append(temp)
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

def k_means(k,iter_max,points):
    prev_centroid = points[:k]
    update_dist = euclidean_distance(prev_centroid[0],prev_centroid[1])
    centroids = []
    iter_count = 0
    while(iter_count<iter_max and update_dist>0.0001):
        iter_count +=1
        clusters = find_clusters(points,k,prev_centroid)
        centroids = update_centroids(points,k,clusters)
        update_dist = dist_cent(prev_centroid,centroids)
        prev_centroid = centroids
    return centroids

def dist_cent(prev_centroids, new_centroids):
    sum = 0
    for prev, new in zip(prev_centroids, new_centroids):
        sum += euclidean_distance(prev, new)
    return sum
def find_clusters(points,k,prev_centroid):
    clusters_points = [0] * len(points)
    for i in range(len(points)):
        min_index = 0
        min_dist = euclidean_distance(points[i],prev_centroid[0])
        for j in range(k):
            curr_dist = euclidean_distance(points[i],prev_centroid[j])
            if(curr_dist<min_dist):
                min_dist = curr_dist
                min_index = j
        clusters_points[i] = min_index
    return clusters_points
def update_centroids(points,k,clusters):
    new_centroid = [0] * k
    for i in range(k):
        coor_data_points = [points[j] for j in range(len(points)) if clusters[j] == i]
        points_amount = len(coor_data_points)
        new_centroid[i] = list(sum(coord) / points_amount for coord in zip(*coor_data_points))
    return new_centroid


if __name__ == "__main__":
    main()