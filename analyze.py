"""
Shonen Manga Sales Comparison — Naruto, One Piece, Bleach
----------------------------------------------------------
Data source: publicly reported lifetime sales figures compiled from
Shueisha/Oricon-sourced reporting (as aggregated by Kaggle/Databoks, 2022
snapshot) for three long-running Shonen Jump manga series.

This script:
1. Loads total lifetime sales and serialization years for each series.
2. Computes an approximate "average copies sold per year" to normalize
   for how long each series ran.
3. Produces a bar chart comparing total sales and a second chart
   comparing sales-per-year.
"""

import pandas as pd
import matplotlib.pyplot as plt

# 1. Load data
df = pd.read_csv("manga_sales_data.csv")

# 2. Derive metrics
df["years_running"] = df["end_year"] - df["start_year"] + 1
df["avg_million_per_year"] = (df["copies_sold_million"] / df["years_running"]).round(1)
df = df.sort_values("copies_sold_million", ascending=False)

print("Total lifetime sales (million copies):")
print(df[["series", "copies_sold_million"]].to_string(index=False))

print("\nAverage sales per year of serialization (million copies/year):")
print(df.sort_values("avg_million_per_year", ascending=False)[["series", "avg_million_per_year"]].to_string(index=False))

# 3. Chart 1 - Total lifetime sales
plt.figure(figsize=(7, 4.5))
plt.bar(df["series"], df["copies_sold_million"], color="#1F4E5F")
plt.ylabel("Total copies sold (millions)")
plt.title("Lifetime Manga Sales: One Piece vs Naruto vs Bleach")
plt.tight_layout()
plt.savefig("total_sales.png", dpi=150)
plt.close()

# 4. Chart 2 - Average sales per year (normalizes for series length)
df_by_rate = df.sort_values("avg_million_per_year", ascending=False)
plt.figure(figsize=(7, 4.5))
plt.bar(df_by_rate["series"], df_by_rate["avg_million_per_year"], color="#8B1E2D")
plt.ylabel("Avg. copies sold per year (millions)")
plt.title("Sales Rate per Year of Serialization")
plt.tight_layout()
plt.savefig("sales_per_year.png", dpi=150)
plt.close()

print("\nCharts saved: total_sales.png, sales_per_year.png")
