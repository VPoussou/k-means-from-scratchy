
import numpy
import random
import math

# Home of the main algorithm

class K_means:
    def __init__(self, k:int, data: numpy.ndarray, elbow_coeff):
        self.k = k
        self.data = data
        self.elbow_coeff = elbow_coeff
        self.baricentres = []
        self.clusters = [0 for _ in range(len(self.data))]

    def rand_sample(self):
        rand_samples = []

        for _ in range(self.k):
            rand_index = random.randint(0, len(self.data))
            rand_samples.append(self.data[rand_index])
        
        self.baricentres = rand_samples
    
    @staticmethod
    def euclidian_distance(a_point_coords:list, b_point_coords:list) -> int:
        print(a_point_coords)
        return math.sqrt(sum((a_coord - b_coord)**2 for (a_coord, b_coord) in zip(a_point_coords, b_point_coords)))

    def closest_cluster(self, point):
        cluster_distances = []
        for bari_bari in self.baricentres[-1]:
            cluster_distances.append(self.euclidian_distance(bari_bari, point))
        return cluster_distances.index(min(cluster_distances))
    
    def get_clusters(self):
        clustered_data = []
        for _ in range(self.k):
            clustered_data.append([])

        for line, cluster in zip(self.data, self.clusters):
            clustered_data[cluster].append(line)

        return numpy.ndarray(clustered_data)
    
    def mean_clusters(self, clusters):
        means = []
        for cluster in clusters:
            means.append(numpy.mean(cluster, axis=1))
        self.baricentres.append(means)

    def get_elbow(self):
        if len(self.baricentres) < 3:
            return False
        diff1 = self.baricentres[-3] - self.baricentres[-2]
        diff2 = self.baricentres[-2] - self.baricentres[-1]
        elbow = diff1 / diff2
        if elbow > self.elbow_coeff:
            return True
        else:
            return False

    def fit(self):
        elbow = False
        self.rand_sample()

        while elbow == False:
            for line, cluster in zip(self.data, self.clusters):
                line[cluster] = self.closest_cluster(line[1:-1])
            
            self.baricentres.append(self.mean_clusters(self.get_clusters))
            elbow = self.get_elbow