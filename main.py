
import numpy as np
import k_means
import data_prep


if __name__ == '__main__':
    data = data_prep.DataPrep('penguins.csv', pingu=True)
    model = k_means.K_means(3, data.data, 1.17)
    model.fit()
    