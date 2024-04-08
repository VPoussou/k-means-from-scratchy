
import numpy

class DataPrep:
    def __init__(self, csv_path, **kwargs) -> None:
        '''Initializes the class with the path to the csv file and the column headers.
        pingu:bool (if you are working with the penguins dataset)
        '''
        self.csv_path = csv_path
        self.pingu = kwargs.get('pingu', False)
        self.read_data()
        self.clean_data()

    def read_data(self):
        self.data = numpy.genfromtxt(self.csv_path, delimiter=',', names=True)

    def clean_data(self):
        if self.pingu == True:
            for line in self.data:
                for el in line:
                    if el == 'NA':
                        el = 0.5