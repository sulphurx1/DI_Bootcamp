import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')
sns.catplot(data = df, x = 'Sex', y = 'Age', kind = "box")
plt.show()