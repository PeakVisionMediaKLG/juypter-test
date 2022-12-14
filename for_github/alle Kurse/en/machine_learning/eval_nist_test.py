import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("nist_tests_20_50_100_120_150.csv", index_col=[0, 1, 2, 3], sep=" ")
data.reindex()
print(data)
data.plot(data)
plt.show()
