import pandas as pd

file_paths = [
    "data/daily_sales_data_0.csv",
    "data/daily_sales_data_1.csv",
    "data/daily_sales_data_2.csv"
]

dataframes = [pd.read_csv(file) for file in file_paths]
combined_df = pd.concat(dataframes, ignore_index=True)

combined_df["product"] = combined_df["product"].astype(str).str.strip().str.lower()
combined_df = combined_df[combined_df["product"] == "pink morsel"].copy()

combined_df["quantity"] = pd.to_numeric(combined_df["quantity"], errors="coerce")

combined_df["price"] = (
    combined_df["price"]
    .astype(str)
    .str.replace("$", "", regex=False)
    .str.replace(",", "", regex=False)
)
combined_df["price"] = pd.to_numeric(combined_df["price"], errors="coerce")

combined_df["Sales"] = combined_df["quantity"] * combined_df["price"]

combined_df["date"] = pd.to_datetime(combined_df["date"], errors="coerce")

output_df = combined_df[["Sales", "date", "region"]].copy()
output_df.columns = ["Sales", "Date", "Region"]

output_df = output_df.dropna().sort_values("Date")

output_df.to_csv("formatted_output.csv", index=False)

print(output_df.head())
print(output_df.shape)
print("formatted_output.csv created successfully.")