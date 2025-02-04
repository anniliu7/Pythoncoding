# Manage missingness in columns
# 1. Drop columns with missing values
df_clean = df.dropna(axis=1, how='any')
# how='all': drops a column only if all values are missing

df_clean = df.dropna(axis=1, how='any').copy()
# If I modify df_clean without altering df, then using .copy() is a safe practice. 
# If I only read or perform operations that don’t change df_clean, I will not need .copy().

# 2. Drop a column with missing values when the missingness proportion in this column is very high

# 3. Impute the missing values using median or mean
miss_median = lambda x: x.fillna(x.median())
df["column_name_1"].transform(miss_median)

miss_mean = lambda x: x.fillna(x.mean())
df["column_name_1"].transform(miss_mean)

# 4. Add a new column that shows the location of the imputed entries

# Manage missingness in rows
# 1. Drop rows with missing values
df_clean = df.dropna(axis=0)

