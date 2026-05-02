# SQL Patterns & Gotchas

---

### LEFT JOIN to keep all rows from one table and match another

```sql
SELECT EmployeeUNI.unique_id, Employees.name
FROM Employees
LEFT JOIN EmployeeUNI ON Employees.id = EmployeeUNI.id;
```

### LEFT JOIN with conditional SUM to calculate a rate (with IFNULL for users with no records)

```sql
SELECT s.user_id,
    ROUND(
        IFNULL(SUM(c.action = 'confirmed') / COUNT(c.user_id), 0),
        2
    ) AS confirmation_rate
FROM Signups s
LEFT JOIN Confirmations c ON s.user_id = c.user_id
GROUP BY s.user_id;
```

### CROSS JOIN to pair every row from two tables, then LEFT JOIN to count matches (including zeros)

```sql
SELECT s.student_id, s.student_name, sub.subject_name,
    COUNT(e.subject_name) AS attended_exams
FROM Students s
CROSS JOIN Subjects sub
LEFT JOIN Examinations e
    ON s.student_id = e.student_id
   AND sub.subject_name = e.subject_name
GROUP BY s.student_id, s.student_name, sub.subject_name
ORDER BY s.student_id, sub.subject_name;
```

### Self join to compute time difference between two activity types per group

```sql
SELECT a1.machine_id,
    ROUND(AVG(a2.timestamp - a1.timestamp), 3) AS processing_time
FROM Activity a1
JOIN Activity a2
    ON a1.machine_id = a2.machine_id AND a1.process_id = a2.process_id
WHERE a1.activity_type = 'start'
  AND a2.activity_type = 'end'
GROUP BY a1.machine_id;
```

### Self join to compare a row with the previous row using DATEDIFF

```sql
SELECT w1.id
FROM Weather w1
JOIN Weather w2
  ON DATEDIFF(w1.recordDate, w2.recordDate) = 1
WHERE w1.temperature > w2.temperature;
```

---
