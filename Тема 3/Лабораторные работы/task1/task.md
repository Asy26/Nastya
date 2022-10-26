Чему равно значение выражения?

```python
not False and True or False and not True
```

Дополнительно в виде трёх строчек комментариев привести ход упрощения выражения.
1. Упростить оператор `not`
2. Упростить оператор `and`
3. Упростить оператор `or`

Пример:
```python
src = True or False and not True  # исходное выражение

# result = True or False and False  # избавляемся от отрицаний
# result = True or False  # избавляемся от логического "И"
# result = True  # избавляемся от логического "ИЛИ"

result = True
```
