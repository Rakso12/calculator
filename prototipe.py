import ast

variable = input("Enter something")
parse = ast.parse(variable)

parsed = parse.body[0].value.left
print(dir(parsed))
print(type(parsed))
print(parsed)

parsed_1 = parse.body[0].func.id
print(dir(parsed_1))
print(type(parsed_1))
print(parsed_1)