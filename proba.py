import ast
import sys

print(sys.version_info)

'''

# Input the operation and parse this operation
math_action = input("Enter a mathematical operation: ")
parse = ast.parse(math_action).body

# Return the result of the operation
print(evaluate(parse))


print(type(ast.parse(cos).body[0].value))
print(dir(ast.parse(cos).body[0].value))
print(ast.parse(cos).body[0].value)
'''