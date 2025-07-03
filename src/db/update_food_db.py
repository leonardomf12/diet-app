import IPython
import requests
import pandas as pd
from io import StringIO
from pathlib import Path
import math
import json

def filtering_non_sense_entries(df0):
    df0 = df0.copy()
    return df0.loc[df0[['BaseQty', 'kcal', 'Protein', 'Fat', 'Carbs']].any(axis=1)]

def clean_nan(obj):
    if isinstance(obj, float) and math.isnan(obj): return None
    elif isinstance(obj, dict): return {k: clean_nan(v) for k, v in obj.items()}
    elif isinstance(obj, list): return [clean_nan(i) for i in obj]
    return obj


if __name__ == "__main__":
    csv_file = Path(__file__).parent / "Foods 2230cb28337f8095bbadc1c86d8473cf.csv"
    df = pd.read_csv(csv_file, sep=",")

    df = filtering_non_sense_entries(df).reset_index(drop=True)

    json_data = []
    for i in range(len(df)):
        json_data.append(df.iloc[i].to_dict())
    json_data_nan = clean_nan(json_data) # Replace pd.nan with None for json compatibility

    with open(Path(__file__).parent / 'food_db.json', 'w', encoding='utf-8') as f:
        json.dump(json_data_nan, f, ensure_ascii=False, indent=2)