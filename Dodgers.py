# In this project, I will be plotting some Dodger pitching stats using Seaborn's 'Scatterplot with varying point sizes and hues'
# This is playoffs only as they have qualified for the Fall Classic.
# Legend: You generally want lower WHIP, lower walks [per 9], and higher K [per 9].

import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="darkgrid")

# Load the example dataset
file_path = r"C:\Users\jra15\OneDrive\Desktop\dodgers_.csv"
mlb_data = pd.read_csv(file_path)

# Plot all pitching data
plot = sns.relplot(x="K/9", y="BB/9", hue="WHIP", size="PLAYER",
                   sizes=(40, 400), alpha=.5, palette='dark',
                   height=6, data=mlb_data)

# Add a title to the plot
plt.title('Dodgers Pitching Stats: K/9 vs BB/9 with WHIP')

# Show the plot
plt.show()
