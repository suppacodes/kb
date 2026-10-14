from pathlib import Path

import pandas as pd

def check_duplicates():
    filename= input("File: ")
    path= Path(filename)
    if not path.exists():
        found= list (Path.cwd().rglob(filename))
        if not found:
            print(f"{filename} Not found")
            return
        found= found[0]
    if path.suffix == ".csv":

        df= pd.read_csv(path)
        print(df.isnull().sum())
        print(df)
    else:
        print("Not a CSV file")



check_duplicates()

