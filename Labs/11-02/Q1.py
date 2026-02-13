import seaborn as sns
import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [25000, 27000, 30000, 28000, 32000, 31000]

plt.figure(figsize=(8, 5))
plt.plot(months, sales, marker='o', linestyle='-', color='b', label='Monthly Sales')
plt.title('Monthly Sales Trend (Matplotlib)')
plt.xlabel('Months')
plt.ylabel('Sales (USD)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.savefig("Q1report1.png")
plt.show()

plt.figure(figsize=(8, 5))
sns.barplot(x=months, y=sales, hue=months, palette='viridis', legend=False)

plt.title('Monthly Sales Comparison (Seaborn)')
plt.xlabel('Months')
plt.ylabel('Sales (USD)')
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.savefig("Q1report2.png")
plt.show()
