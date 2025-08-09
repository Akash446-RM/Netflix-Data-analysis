import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("netflix_titles.csv")


type_counts = df['type'].value_counts()

# Plot
plt.figure(figsize=(6,6))
plt.pie(type_counts, labels=type_counts.index, autopct='%1.1f%%', startangle=140)
plt.title("Overall Distribution: Movies vs TV Shows")
plt.show()
