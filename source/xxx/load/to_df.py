###############

import pandas as pd
import glob
import datetime as dt

def csv_path_to_df(path: str = "C:/data", file_name_to_exclude: str = "abc.csv"):
    all_files = glob.glob(path + "/*.csv")
    file_path_to_exclude = [s for s in all_files if file_name_to_exclude in s]
    try:
        all_files.remove(file_path_to_exclude[0])
    except Exception as e:
        print("")
    l = []
    for filename in all_files:
        df = pd.read_csv(filename, index_col=None, header=0)
        l.append(df)
    frame = pd.concat(l, axis=0, ignore_index=True)
    return frame
