import numpy as np
import pandas as pd

data = pd.read_csv("/Users/florianlorisch/PycharmProjects/open-discourse-dynamic-topic-model/corpus/speeches/speeches_preprocessed_grüne.csv")

data['date'] = pd.to_datetime(data['date'], format="%Y")

uniqueyears, time_slices = np.unique(data.date, return_counts=True)
print(np.asarray((uniqueyears, time_slices)).T)



