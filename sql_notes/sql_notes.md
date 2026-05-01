# SQL Notes

## Purpose
Keep this file simple, practical, and focused on SQL basics for data analysis. Use it for quick reference while writing queries and reviewing common interview topics.

## Quick SQL Script Patterns

### Select + Filter
```sql
SELECT column1, column2
FROM table_name
WHERE condition;
```

### Join Tables
```sql
SELECT a.column1, b.column2
FROM table_a AS a
JOIN table_b AS b
  ON a.key = b.key;
```

### Aggregate + Group
```sql
SELECT category, COUNT(*) AS count, AVG(value) AS avg_value
FROM table_name
GROUP BY category;
```

### Window Functions
```sql
SELECT
  id,
  value,
  ROW_NUMBER() OVER (PARTITION BY category ORDER BY value DESC) AS row_num,
  SUM(value) OVER (PARTITION BY category) AS total_value
FROM table_name;
```

### Common CTE Pattern
```sql
WITH cleaned AS (
  SELECT *
  FROM raw_table
  WHERE status = 'active'
)
SELECT *
FROM cleaned;
```

## Useful SQL Concepts
- `JOIN` types: `INNER`, `LEFT`, `RIGHT`, `FULL OUTER`
- Use `CASE WHEN` for conditional logic
- `DISTINCT` removes duplicates
- `ORDER BY` sorts results
- `LIMIT` or `FETCH` restricts row output
- Prefer `CTE` for readability in complex queries

## High-Frequency Data Science Interview Questions

### 1. What is the difference between `INNER JOIN` and `LEFT JOIN`?
- `INNER JOIN`: returns rows with matching keys in both tables.
- `LEFT JOIN`: returns all rows from the left table and matched rows from the right table.

### 2. Why use window functions?
- Window functions calculate values across rows related to the current row without collapsing rows.
- Common use cases: running totals, ranks, and moving averages.

### 3. How do you handle duplicates in SQL?
- Use `SELECT DISTINCT`.
- Use `ROW_NUMBER()` with a partition and filter to keep one row.

### 4. What is a CTE and why is it useful?
- CTE = Common Table Expression.
- It makes complex queries easier to read and reuse.

### 5. How do you find missing values or nulls?
- Use `WHERE column IS NULL` or `WHERE column IS NOT NULL`.

### 6. How do you optimize SQL queries?
- Use indexes on join and filter columns.
- Avoid `SELECT *` in production queries.
- Filter early and minimize data scanned.

### 7. What is the difference between `WHERE` and `HAVING`?
- `WHERE` filters rows before aggregation.
- `HAVING` filters after aggregation.

## Notes
- Keep examples short and test in the database engine you use.
- Update this file with new patterns or common interview concepts as you learn them.
