import pandas as pd
from tqdm import tqdm
from dateutil.parser import parse

from predict.models import Node, Price

name = "SNJSEA_1_N101"

df = pd.read_csv("RTM_SNJSEA_1_N101_20200101_20230131.csv")
df = df.loc[df["LMP_TYPE"] == "LMP"]

n = Node(name=name)
n.save()

for index, row in tqdm(df.iterrows()):
    start = parse(row["INTERVALSTARTTIME_GMT"])
    end = parse(row["INTERVALENDTIME_GMT"])
    rtm = float(row["VALUE"])
    p = Price(node=n, start=start, end=end, rtm=rtm)
    p.save()
