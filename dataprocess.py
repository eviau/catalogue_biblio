# inspiration: https://stackoverflow.com/questions/17444679/reading-a-huge-csv-file

import csv

if __name__ == "__main__":
    filename = "donnees_ouverte.csv"
    with open(filename, 'r',) as csvfile:
        datareader  = csv.reader(csvfile)
        next(datareader)
        for row in datareader:
            if "Rosemont" in row[0]:
                if "Adultes" in row[1] and "Disponible" in row[5] and ("Documentaire" in row[1] or "Roman" in row[1]):
                    if int(row[3]) > 85:
                        if int(row[4]) == 0:
                            print(row[1] + " " + row[8] + " " + row[10]+ " " +  row[3] + " " + row[4])
                            print("\n")
                            input("Appuyez sur ENTRÉE pour le prochain livre! \n")
