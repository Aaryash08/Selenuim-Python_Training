import pandas as pd
import numpy as np

students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 92},
    {"name": "Charlie", "score": 78},
    {"name": "David", "score": 90},
    {"name": "Eva", "score": 88}
]

df = pd.DataFrame(students)

scores = df['score'].to_numpy()

mean_score = np.mean(scores)
median_score = np.median(scores)
std_dev = np.std(scores)

print(f"Mean Score: {mean_score:.2f}")
print(f"Median Score: {median_score}")
print(f"Standard Deviation: {std_dev:.2f}")

df['above_average'] = df['score'] > mean_score

print("\nUpdated DataFrame:")
print(df)
