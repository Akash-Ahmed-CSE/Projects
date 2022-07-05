import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
df = pd.read_csv("Survey-on-Regular-Life-Responses.csv")


plt.title('\n\nHaving trouble in all your relationships.\n')

print(df.head())
sns.set_style("dark")
sns.set_palette("RdBu")
#only change the value of X

ax = sns.countplot(x='You are having trouble in all your relationships (home as well as professional).', hue='Gender',data=df)

total = int(1)
for p in ax.patches:
    height = p.get_height()
    ax.text(p.get_x()+p.get_width()/2.,
            height + 3,
            '{:1.2f}'.format(height/total),
            ha="center",fontsize=10)
ax.set(xlabel=' ', ylabel='Number of people')


ax.set_ylabel("Number of people")

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.legend(loc='upper right')
#plt.xticks(rotation=20)

plt.show()



