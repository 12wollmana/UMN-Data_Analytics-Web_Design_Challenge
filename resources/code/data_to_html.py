import pandas as pd

data_filepath = "../data/cities.csv"
output_filepath = "../data/cities.html"

data_df = pd.read_csv(data_filepath)
#print(data_df.head())
data_df.to_html(output_filepath, index = False)
