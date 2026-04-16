import pandas as pd

file_paths = [
    "data/daily_sales_data_0.csv",
    "data/daily_sales_data_1.csv",
    "data/daily_sales_data_2.csv"
]

dataframes = [pd.read_csv(file) for file in file_paths]
combined_df = pd.concat(dataframes, ignore_index=True)

combined_df["product"] = combined_df["product"].str.strip()
combined_df = combined_df[combined_df["product"] == "Pink Morsels"]

combined_df["Sales"] = combined_df["quantity"] * combined_df["price"]

output_df = combined_df[["Sales", "date", "region"]].copy()
output_df.columns = ["Sales", "Date", "Region"]

output_df.to_csv("formatted_output.csv", index=False)

print("formatted_output.csv created successfully.")