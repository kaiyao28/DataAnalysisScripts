# SQL Notes

## Purpose
Keep this file simple, practical, and focused on SQL basics for data analysis. Use it for quick reference while writing queries and reviewing common interview topics.

---

## Inspect a Table First

```sql
-- preview data
SELECT * FROM mytable LIMIT 10;

-- count rows
SELECT COUNT(*) FROM mytable;

-- describe columns (MySQL)
DESCRIBE mytable;

-- describe columns (SQLite)
PRAGMA table_info(mytable);

-- describe columns (PostgreSQL)
\d mytable

-- column names and types (any DB)
SELECT column_name, data_type
FROM information_schema.columns
WHERE table_name = 'mytable';
```

---

## Query Structure

### Complete SELECT query order
```sql
SELECT DISTINCT column, AGG_FUNC(column) AS alias
FROM mytable
    JOIN another_table ON mytable.id = another_table.id
WHERE constraint_expression
GROUP BY column
HAVING constraint_expression
ORDER BY column ASC/DESC
LIMIT count OFFSET count;
```

### Select specific columns
```sql
SELECT column1, column2 FROM mytable;
```

### Aliases
```sql
SELECT column AS better_name, long_table_name AS t
FROM long_table_name AS t;
```

### Filter + sort
```sql
SELECT DISTINCT column
FROM mytable
WHERE column IS NOT NULL
  AND/OR another_condition
ORDER BY column ASC/DESC
LIMIT num OFFSET num;
```

### Join tables
```sql
SELECT a.column1, b.column2
FROM table_a AS a
INNER/LEFT/RIGHT/FULL JOIN table_b AS b
    ON a.key = b.key
WHERE condition
ORDER BY column ASC/DESC
LIMIT num OFFSET num;
```

### Self join to compare rows within the same table
```sql
SELECT w1.id
FROM Weather w1
JOIN Weather w2
  ON DATEDIFF(w1.recordDate, w2.recordDate) = 1
WHERE w1.temperature > w2.temperature;
```

---

## WHERE Operators

### Numeric
| Operator | Condition |
|---|---|
| `=, !=, <, <=, >, >=` | Standard comparisons |
| `BETWEEN a AND b` | Within range (inclusive) |
| `NOT BETWEEN a AND b` | Outside range |
| `IN (1, 2, 3)` | Exists in list |
| `NOT IN (1, 2, 3)` | Not in list |

### String
| Operator | Condition |
|---|---|
| `=` | Case-sensitive exact match |
| `!=` or `<>` | Case-sensitive inequality |
| `LIKE` | Case-insensitive match |
| `NOT LIKE` | Case-insensitive inequality |
| `LIKE "%AT%"` | `%` matches any sequence of characters |
| `LIKE "AN_"` | `_` matches a single character |
| `IN ("A","B")` | Exists in list |
| `NOT IN ("A","B")` | Not in list |

---

## Aggregate Functions

| Function | Description |
|---|---|
| `COUNT(*)` | Count all rows |
| `COUNT(column)` | Count non-NULL values |
| `MIN(column)` | Smallest value |
| `MAX(column)` | Largest value |
| `AVG(column)` | Average value |
| `SUM(column)` | Sum of values |

```sql
SELECT category, COUNT(*) AS count, AVG(value) AS avg_value
FROM mytable
GROUP BY category
HAVING COUNT(*) > 5;
```

---

## Built-in Functions

### String
| Function | Description |
|---|---|
| `LENGTH(col)` | Number of characters |
| `UPPER(col)` | Uppercase |
| `LOWER(col)` | Lowercase |
| `TRIM(col)` | Remove leading/trailing spaces |
| `SUBSTRING(col, start, length)` | Extract part of a string |
| `CONCAT(col1, col2)` | Join strings together |
| `REPLACE(col, 'from', 'to')` | Replace substring |

### Numeric
| Function | Description |
|---|---|
| `ROUND(col, 2)` | Round to decimal places |
| `ABS(col)` | Absolute value |
| `CEIL(col)` | Round up |
| `FLOOR(col)` | Round down |

### Date
| Function | Description |
|---|---|
| `NOW()` | Current date and time |
| `CURDATE()` | Current date |
| `YEAR(col)`, `MONTH(col)`, `DAY(col)` | Extract parts of a date |
| `DATEDIFF(date1, date2)` | Days between two dates |

### Conditional
```sql
-- CASE WHEN
SELECT name,
    CASE WHEN score >= 90 THEN 'A'
         WHEN score >= 75 THEN 'B'
         ELSE 'C'
    END AS grade
FROM mytable;

-- COALESCE — return first non-NULL value
SELECT COALESCE(col, 'default') FROM mytable;

-- NULLIF — return NULL if two values are equal
SELECT NULLIF(col, 0) FROM mytable;

-- IFNULL — replace NULL with a value (MySQL)
SELECT IFNULL(col, 0) FROM mytable;
```

---

## Window Functions
```sql
SELECT id, value,
    ROW_NUMBER()   OVER (PARTITION BY category ORDER BY value DESC) AS row_num,
    RANK()         OVER (PARTITION BY category ORDER BY value DESC) AS rank,
    DENSE_RANK()   OVER (PARTITION BY category ORDER BY value DESC) AS dense_rank,
    SUM(value)     OVER (PARTITION BY category) AS total_value,
    AVG(value)     OVER (PARTITION BY category) AS avg_value,
    LAG(value, 1)  OVER (ORDER BY date) AS prev_value,
    LEAD(value, 1) OVER (ORDER BY date) AS next_value
FROM mytable;
```

| Function | Description |
|---|---|
| `ROW_NUMBER()` | Unique sequential number per partition |
| `RANK()` | Rank with gaps on ties (1,1,3) |
| `DENSE_RANK()` | Rank without gaps on ties (1,1,2) |
| `LAG(col, n)` | Value from n rows before |
| `LEAD(col, n)` | Value from n rows ahead |

---

## CTE
```sql
WITH cleaned AS (
    SELECT * FROM raw_table WHERE status = 'active'
)
SELECT * FROM cleaned;
```

---

## Insert / Update / Delete

### Insert
```sql
INSERT INTO mytable (column1, column2)
VALUES (value1, value2),
       (value3, value4);
```

### Update
```sql
UPDATE mytable
SET column = value, other_column = other_value
WHERE condition;
```

### Delete
```sql
DELETE FROM mytable WHERE condition;
```

---

## Create / Alter / Drop

### Create table
```sql
CREATE TABLE movies (
    id        INTEGER PRIMARY KEY,
    title     TEXT,
    director  TEXT,
    year      INTEGER,
    length    INTEGER
);
```

### Alter table
```sql
ALTER TABLE mytable ADD column DataType DEFAULT default_value;
ALTER TABLE mytable DROP column_to_delete;
ALTER TABLE mytable RENAME TO new_name;
```

### Drop table
```sql
DROP TABLE IF EXISTS mytable;
```

---

## Data Types

| Type | Description |
|---|---|
| `INTEGER`, `BOOLEAN` | Whole numbers; boolean is often 0/1 |
| `FLOAT`, `DOUBLE`, `REAL` | Decimal / floating point numbers |
| `CHAR(n)`, `VARCHAR(n)`, `TEXT` | Strings; VARCHAR is variable-length up to n |
| `DATE`, `DATETIME` | Date and timestamp values |
| `BLOB` | Binary data |

---

## Constraints

| Constraint | Description |
|---|---|
| `PRIMARY KEY` | Unique identifier for each row |
| `AUTOINCREMENT` | Auto-increments integer on each insert |
| `UNIQUE` | Values must be unique (not necessarily a key) |
| `NOT NULL` | Value cannot be NULL |
| `CHECK (expr)` | Custom validation (e.g. `CHECK (age > 0)`) |
| `FOREIGN KEY` | References a value in another table's column |

---

## High-Frequency Interview Questions

### 1. INNER JOIN vs LEFT JOIN
- `INNER JOIN`: rows with matching keys in **both** tables.
- `LEFT JOIN`: all rows from left table + matched rows from right (NULL if no match).

### 2. WHERE vs HAVING
- `WHERE` filters rows **before** aggregation.
- `HAVING` filters **after** aggregation.

### 3. Why use window functions?
- Calculate values across related rows without collapsing them (unlike GROUP BY).
- Common uses: running totals, ranks, moving averages.

### 4. How to handle duplicates?
- `SELECT DISTINCT`
- `ROW_NUMBER() OVER (PARTITION BY ...)` then filter to keep one row.

### 5. What is a CTE?
- Common Table Expression — makes complex queries readable and reusable.

### 6. How to find NULLs?
```sql
WHERE column IS NULL
WHERE column IS NOT NULL
```

### 7. How to optimize queries?
- Index join and filter columns.
- Avoid `SELECT *` in production.
- Filter early to minimize data scanned.
