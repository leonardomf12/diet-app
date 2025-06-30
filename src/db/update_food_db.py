import IPython
import requests
import pandas as pd
from io import StringIO


if __name__ == "__main__":
    url = "https://docs.google.com/spreadsheets/d/1SMGnkb-xJI20_nDpeZXeAP8sfdtYadh0/edit?gid=1735492025#gid=1735492025"
    response = requests.get(url)

    df = pd.read_csv(StringIO(response.text))
    IPython.embed()
    print(df)