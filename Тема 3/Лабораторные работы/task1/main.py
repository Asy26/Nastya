src = not False and True or False and not True

result = True or False and not True  # TODO расписать упрощение выражения
result = True or False
result = True  # TODO подставить результат выражения

print(src == result)
