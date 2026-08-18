import pandas as pd

data = [
    ["Lassa Fever", 2026, 27, "Ondo", 61, 8, 0, 0, 1, 1603, 282, 0, 10, 66],
    ["Lassa Fever", 2026, 27, "Bauchi", 8, 1, 0, 0, 0, 986, 238, 1, 5, 32],
    ["Lassa Fever", 2026, 27, "Taraba", 0, 0, 0, 0, 0, 364, 131, 0, 3, 43],
    ["Lassa Fever", 2026, 27, "Edo", 45, 3, 0, 0, 1, 1333, 89, 0, 0, 20],
    ["Lassa Fever", 2026, 27, "Benue", 12, 1, 0, 0, 0, 407, 58, 2, 15, 14],
    ["Lassa Fever", 2026, 27, "Plateau", 8, 0, 0, 0, 0, 166, 33, 3, 2, 11],
    ["Lassa Fever", 2026, 27, "Ebonyi", 8, 0, 0, 0, 0, 268, 24, 0, 3, 12],
    ["Lassa Fever", 2026, 27, "Nasarawa", 0, 0, 0, 0, 0, 263, 17, 0, 7, 3],
    ["Lassa Fever", 2026, 27, "Kaduna", 0, 0, 0, 0, 0, 86, 13, 0, 0, 3],
    ["Lassa Fever", 2026, 27, "Kogi", 1, 1, 0, 0, 1, 45, 11, 0, 0, 7],
    ["Lassa Fever", 2026, 27, "Kano", 0, 0, 0, 0, 0, 100, 8, 0, 3, 1],
    ["Lassa Fever", 2026, 27, "Gombe", 0, 0, 0, 0, 0, 55, 7, 0, 0, 4],
    ["Lassa Fever", 2026, 27, "Katsina", 0, 0, 0, 0, 0, 19, 5, 0, 0, 4],
    ["Lassa Fever", 2026, 27, "Oyo", 2, 0, 0, 0, 0, 119, 5, 0, 3, 1],
    ["Lassa Fever", 2026, 27, "FCT", 1, 0, 0, 0, 0, 47, 3, 0, 0, 0],
    ["Lassa Fever", 2026, 27, "Kebbi", 0, 0, 0, 0, 0, 9, 3, 0, 0, 1],
    ["Lassa Fever", 2026, 27, "Zamfara", 0, 0, 0, 0, 0, 25, 2, 0, 0, 0],
    ["Lassa Fever", 2026, 27, "Jigawa", 0, 0, 0, 0, 0, 49, 2, 0, 0, 2],
    ["Lassa Fever", 2026, 27, "Niger", 0, 0, 0, 0, 0, 12, 1, 0, 0, 0],
    ["Lassa Fever", 2026, 27, "Kwara", 1, 0, 0, 0, 0, 15, 1, 0, 0, 0],
    ["Lassa Fever", 2026, 27, "Cross River", 0, 0, 0, 0, 0, 28, 1, 0, 0, 0],
    ["Lassa Fever", 2026, 27, "Ogun", 1, 0, 0, 0, 0, 24, 1, 0, 0, 0],
    ["Lassa Fever", 2026, 27, "Enugu", 4, 0, 0, 0, 0, 59, 1, 0, 0, 0],
    ["Lassa Fever", 2026, 27, "Akwa Ibom", 0, 0, 0, 0, 0, 2, 0, 0, 0, 0],
    ["Lassa Fever", 2026, 27, "Ekiti", 1, 0, 0, 0, 0, 48, 0, 0, 0, 0],
    ["Lassa Fever", 2026, 27, "Imo", 0, 0, 0, 0, 0, 8, 0, 0, 0, 0],
    ["Lassa Fever", 2026, 27, "Sokoto", 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    ["Lassa Fever", 2026, 27, "Yobe", 0, 0, 0, 0, 0, 8, 0, 0, 0, 0],
    ["Lassa Fever", 2026, 27, "Delta", 0, 0, 0, 0, 0, 33, 0, 0, 0, 0],
    ["Lassa Fever", 2026, 27, "Rivers", 0, 0, 0, 0, 0, 8, 0, 0, 0, 0],
    ["Lassa Fever", 2026, 27, "Anambra", 0, 0, 0, 0, 0, 12, 0, 0, 0, 0],
    ["Lassa Fever", 2026, 27, "Osun", 0, 0, 0, 0, 0, 17, 0, 0, 0, 0],
    ["Lassa Fever", 2026, 27, "Bayelsa", 0, 0, 0, 0, 0, 8, 0, 0, 0, 0],
    ["Lassa Fever", 2026, 27, "Abia", 0, 0, 0, 0, 0, 9, 0, 0, 0, 0],
    ["Lassa Fever", 2026, 27, "Borno", 0, 0, 0, 0, 0, 14, 0, 0, 0, 0],
    ["Lassa Fever", 2026, 27, "Lagos", 1, 0, 0, 0, 0, 72, 0, 0, 0, 0],
    ["Lassa Fever", 2026, 27, "Adamawa", 0, 0, 0, 0, 0, 4, 0, 0, 0, 0],
]

columns = [
    "disease",
    "year",
    "epi_week",
    "state",
    "weekly_suspected",
    "weekly_confirmed",
    "weekly_probable",
    "weekly_hcw_cases",
    "weekly_deaths",
    "cumulative_suspected",
    "cumulative_confirmed",
    "cumulative_probable",
    "cumulative_hcw_cases",
    "cumulative_deaths",
]

df = pd.DataFrame(data, columns=columns)

df["cumulative_cfr"] = (
    df["cumulative_deaths"] / df["cumulative_confirmed"] * 100
).fillna(0).round(2)

df["weekly_cfr"] = (
    df["weekly_deaths"] / df["weekly_confirmed"] * 100
).fillna(0).round(2)

output_path = "data/processed/lassa_surveillance_2026.csv"

df.to_csv(output_path, index=False)

print(df.head())
print()
print(f"Dataset saved to: {output_path}")
print(f"Rows: {len(df)}")
print(f"Total confirmed cases: {df['cumulative_confirmed'].sum()}")
print(f"Total deaths: {df['cumulative_deaths'].sum()}")


