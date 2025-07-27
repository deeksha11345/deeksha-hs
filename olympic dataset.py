import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("C:/Users/deeks/Downloads/athlete_events.csv.zip")
plt.figure(figsize=(10, 6))
plt.hist(df['Age'].dropna(), bins=20, color='skyblue', edgecolor='black')
plt.title('Age Distribution of Olympic Athletes')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()