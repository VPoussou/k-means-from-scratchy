
import numpy as np
import k_means
import data_prep


if __name__ == '__main__':

    data_prep.DataPrep('penguins.csv', pingu=True).read_data()
    