import pandas as pd

def sum_first_last(row):
    first = row[0]
    last = row[-1]

    sum_first_last = sum(first,last)

    return sum_first_last

test_df = pd.read_csv("")

test_df["Sum of first and last"] = test_df["data"].apply(lambda x: sum_first_last(x))

