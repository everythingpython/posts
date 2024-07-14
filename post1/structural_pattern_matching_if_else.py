import sys
import pandas as pd


def pattern_matching_if_else(file_name):
    x = file_name.split(".")[-1]
    df = None
    print(f"File format = {x}")
    if x == "json":
        df = pd.read_json(file_name)
        result = "Success"
    elif x == "csv":
        df = pd.read_csv(file_name)
        result = "Success"
    elif x == "pq" or x == "parquet":
        result = "Fail"
        print("Conversion for parquet Unsupported.")
    else:
        result = "Fail"
        print("Unrecognized file format.")
    return result, df


filename = sys.argv[1]
res, df = pattern_matching_if_else(filename)
if res == "Fail":
    pass
elif res == "Success":
    print(df)
