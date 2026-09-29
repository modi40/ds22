import pandas as pd
import matplotlib.pyplot as plt
from matplotlib_venn import venn2

data = {
    'Customer_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112],
    'Netflix': [True, True, True, False, False, True, False, True, False, True, True, False],
    'Amazon_Prime': [False, True, False, True, True, True, True, False, True, True, False, True]
}

df = pd.DataFrame(data)

only_netflix = len(df[df['Netflix'] & ~df['Amazon_Prime']])
only_prime = len(df[~df['Netflix'] & df['Amazon_Prime']])
both = len(df[df['Netflix'] & df['Amazon_Prime']])

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
venn2(subsets=(only_netflix, only_prime, both), set_labels=('Netflix', 'Amazon Prime'))
plt.title("Venn Diagram of Subscriptions")

plt.subplot(1, 2, 2)
sizes = [only_netflix, only_prime, both]
labels = ['Only Netflix', 'Only Amazon Prime', 'Both Services']
colors = ['#E50914', '#00A8E1', '#9B51E0']
plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=140)
plt.title("Pie Chart of Subscription Distribution")

plt.tight_layout()
plt.show()
