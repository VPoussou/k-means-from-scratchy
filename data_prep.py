
import numpy

class DataPrep:
    def __init__(self, csv_path, column_headers) -> None:
        self.csv_path = csv_path

    def read_data(self):
        self.data = numpy.genfromtxt(self.csv_path, names=True)

    def clean_data():
        