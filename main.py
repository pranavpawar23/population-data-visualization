import matplotlib.pyplot as plt

# Top 10 most populous countries (2024 estimates)
countries = [
    "India", "China", "United States", "Indonesia", 
    "Pakistan", "Nigeria", "Brazil", "Bangladesh",
    "Russia", "Ethiopia"
]

populations = [
    1450935791, 1419321279, 345426567, 283487932,
    251269158, 232679482, 211998564, 173562367,
    144820423, 132059770
]

# Create bar chart
plt.figure(figsize=(12, 6))
plt.bar(countries, populations, color='skyblue')

plt.xticks(rotation=45, ha='right')
plt.ylabel("Population (in billions)")
plt.title("Top 10 Most Populous Countries in the World (2024)")
plt.tight_layout()

plt.show()
