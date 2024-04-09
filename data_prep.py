
import numpy

class DataPrep:
    def __init__(self, csv_path, **kwargs) -> None:
        '''Initializes the class with the path to the csv file and the column headers.
        pingu:bool (if you are working with the penguins dataset)
        '''
        self.csv_path = csv_path
        self.pingu = kwargs.get('pingu', False)
        self.read_data()
        print(self.data.shape)
        self.clean_data()

    def read_data(self):
        self.data = numpy.genfromtxt(self.csv_path, delimiter=',', skip_header=1)

    def clean_data(self):
        if self.pingu == True:
            for index, line in enumerate(self.data):
                for el in line:
                    if el == 'NA':
                        self.data[index] = 0.5