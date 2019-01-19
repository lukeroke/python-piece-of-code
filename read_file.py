def get_data_dir():
    """
    Return the data path in script.py/../data
    """
    from pathlib import Path
    DATA_DIR = Path(__file__).resolve().parents[1] / 'data'


def csv_split_by_ratio_range(ratio_range, in_csv_file, out_csv_file):
    import pandas as pd
    data = pd.read_csv(in_csv_file, encoding='latin-1').sample(frac=1).drop_duplicates()
    start, end = (int(r * len(data)) for r in ratio_range)
    data.iloc[start:end].to_csv(out_csv_file, sep='\t', index = False, header = False)
    # e.g.,:
    # csv_split_by_ratio_range((0, 0.8), 'spam.csv', 'train.csv')
    # csv_split_by_ratio_range((0.8, 0.9), 'spam.csv', 'test.csv')
    # csv_split_by_ratio_range((0.9, 1), 'spam.csv', 'dev.csv')



#
