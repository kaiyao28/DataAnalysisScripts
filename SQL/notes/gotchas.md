# SQL Patterns & Gotchas

---

### LEFT JOIN to keep all rows from one table and match another

```sql
SELECT EmployeeUNI.unique_id, Employees.name
FROM Employees
LEFT JOIN EmployeeUNI ON Employees.id = EmployeeUNI.id;
```

---
