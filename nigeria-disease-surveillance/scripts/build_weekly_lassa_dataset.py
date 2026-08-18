import pandas as pd

data = [
    [2026, 20, 185, 24, 0, 4, 16.7, 4, 11],
    [2026, 21, 149, 11, 0, 0, 0.0, 2, 4],
    [2026, 22, 125, 13, 0, 2, 15.4, 2, 5],
    [2026, 23, 138, 13, 0, 4, 30.8, 4, 8],
    [2026, 24, 149, 13, 0, 2, 15.4, 5, 9],
    [2026, 25, 150, 22, 1, 3, 13.6, 4, 10],
    [2026, 26, 205, 31, 0, 2, 6.5, 3, 9],
    [2026, 27, 154, 14, 0, 3, 21.4, 5, 9],
    [2026, 28, 216, 25, 0, 4, 16.0, 5, 11],
    [2026, 29, 173, 20, 0, 2, 10.0, 3, 6],
    [2026, 30, 227, 17, 0, 6, 35.3, 4, 8],
]

columns = [
    "year",
    "epi_week",
    "suspected_cases",
    "confirmed_cases",
    "probable_cases",
    "deaths",
    "weekly_cfr",
    "states_affected",
    "lgas_affected",
]

df = pd.DataFrame(data, columns=columns)

df.insert(0, "disease", "Lassa Fever")

output_path = "data/processed/lassa_weekly_national_2026.csv"

df.to_csv(output_path, index=False)

print(df)
print()
print(f"Dataset saved to: {output_path}")
print(f"Weeks included: {len(df)}")