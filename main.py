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
        duplicates=df.duplicated().sum()
        print(f"Duplicates: {duplicates}")

    else:
        print("Not a CSV file")


def remove_duplicates():
    filename = input("File: ")
    path = Path(filename)
    if not path.exists():
        found = list(Path.cwd().rglob(filename))
        if not found:
            print(f"{filename} Not found")
            return
        found = found[0]
    if path.suffix == ".csv":
        df = pd.read_csv(path)
        duplicates=df.duplicated().sum()
        if duplicates <= 0:
            print(" No duplicates")
        else:
            print(f"Duplicates: {duplicates}")
            df.drop_duplicates(inplace=True)
            print("Duplicated removed✅")
    else:
        print("Not a CSV file")


check_duplicates()

def visualize():
    filename = input("File: ")
    path = Path(filename)
    if not path.exists():
        found = list(Path.cwd().rglob(filename))
        if not found:
            print(f"{filename} Not found")
            return
        found = found[0]
    if path.suffix == ".csv":
        df = pd.read_csv(path)

    # df: relationship between  years and unemployment of SA
    SA= df[df["Country Name"]=="South Africa"]
    years=range(1991,2022)
    unemployment = SA[[str(year) for year in years]].iloc[0] #iloc creates a SA series
    # use a loop instead of typing the years manually.
    
    # CREATE SCATTERPLOT
    plt.scatter(years,unemployment)
    plt.xlabel("Year")
    plt.ylabel("Country Name")
    plt.title("SA Unemployment")
    plt.show()

visualize()


