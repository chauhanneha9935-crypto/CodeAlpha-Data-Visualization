import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv("quotes_dataset.csv")

df["Tag_Count"] = df["Tags"].apply(lambda x: len(str(x).split(",")))

plt.figure()
plt.hist(df["Tag_Count"])
plt.title("Distribution of Tag Counts")
plt.xlabel("Number of Tags")
plt.ylabel("Frequency")
plt.show()

numeric_df = pd.DataFrame({
    "A": np.random.rand(10),
    "B": np.random.rand(10),
    "C": np.random.rand(10)
})

plt.figure()
sns.heatmap(numeric_df.corr(), annot=True)
plt.title("Correlation Heatmap")
plt.show()
