
import numpy
import random
import math

# Home of the main algorithm

class K_means:
    def __init__(self, k:int, data: numpy.ndarray):
        self.k = k
        self.data = data

    def rand_sample(self):
        rand_samples = []
        rand_samples_indexes = []

        for _ in range(self.k):
            rand_index = random.randint(0, len(self.data))
            rand_samples_indexes.append(rand_index)
            rand_samples.append(self.data[rand_index])
        
        return rand_samples, rand_samples_indexes
    
    @staticmethod
    def euclidian_distance(a_point_coords, b_point_coords) -> int:
        return math.sqrt(sum((a_coord - b_coord)**2 for (a_coord, b_coord) in (a_point_coords, b_point_coords)))

    def closest_point_to(self, point):
        euclidistances = [] 
        for line in self.data:
            euclidistances.append([line[0]], self.euclidian_distance(point[1:], line[1:]))

        return min(euclidistances, key=lambda x: x[1])
    