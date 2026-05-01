# Gotchas & Common Mistakes

---

## Pandas

### Create a DataFrame from a list of lists

```python
pd.DataFrame([[1, 15], [2, 11]], columns=["student_id", "age"])
```

### Assign column names when creating a DataFrame from a parameter

```python
pd.DataFrame(student_data, columns=["student_id", "age"])
```

### Return a value from a function — don't just call it

```python
return [df.shape[0], df.shape[1]]  # not print(...)
return df.head(3)                  # not df.head(3) alone
return df.tail(3)                  # not df.tail(3) alone
```

### Drop duplicates by column

```python
return df.drop_duplicates(subset=["email"])
```

### Modify a column then return — can't do both in one line

```python
df["salary"] = df["salary"] * 2  # modify column in place
df["grade"] = df["grade"].astype(int)  # change dtype
return df
```

### Rename columns

```python
df = df.rename(columns={"id": "student_id", "first": "first_name", "age": "age_in_years"})
return df
```

### Round floats to decimal places

```python
df["col"].round(2)             # pandas column — 2 decimal places
round(3.14159, 2)              # Python built-in — 3.14
f"{3.14159:.2f}"               # f-string — "3.14"
```

### Melt wide to long — name both the variable and value columns

```python
df.melt(id_vars=["product"], value_vars=["q1","q2","q3","q4"],
        var_name="quarter", value_name="sales")
```

### Sort DataFrame then select column — not sort on a Series

```python
df[df["weight"] > 100].sort_values("weight", ascending=False)[["name"]]
```

### `["col"]` returns a Series — `[["col"]]` returns a DataFrame

```python
df["name"]    # Series
df[["name"]]  # DataFrame (single column)
```

### Filter rows and select columns in one step

```python
df.loc[df["student_id"] == 101, ["name", "age"]]
```

---
