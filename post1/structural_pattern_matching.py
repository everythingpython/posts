import sys
import pandas as pd 

def pattern_matching(file_name):
    x = file_name.split(".")[-1]
    df = None
    print(f"File format = {x}")
    match x:
        case "json":
            df = pd.read_json(file_name)
            result = "Success"
        case "csv":
            df = pd.read_csv(file_name)
            result = "Success"
        case "pq" | "parquet":
            result = "Fail"
            print("Conversion for parquet Unsupported.")
        case _:
            result = "Fail"
            print("Unrecognized file format.")
    return (result,df)


filename = sys.argv[1]
(result,df) = pattern_matching(filename)
match result:
    case "Fail":
        pass
    case "Success":
        print(df)
