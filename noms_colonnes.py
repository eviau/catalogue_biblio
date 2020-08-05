import csv

if __name__ == "__main__":
    filename = "donnees_ouverte.csv"
    with open(filename, 'r',) as csvfile:
        datareader  = csv.reader(csvfile)
        print(next(datareader))
