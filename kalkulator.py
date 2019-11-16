#kalkulator

import ast
import operator

# A dictionary of operation
op_map = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.USub: operator.neg
    }

# A function that parse and calculate the content of a tree
def evaluate(parsed_content_body):
    if isinstance(parsed_content_body,list):
        return [evaluate(variable) for variable in parsed_content_body]
    if isinstance(parsed_content_body,ast.Expr):
        return evaluate(parsed_content_body.value)
    if isinstance(parsed_content_body,ast.BinOp):
        return op_map[type(parsed_content_body.op)](evaluate(parsed_content_body.left),evaluate(parsed_content_body.right))
    if isinstance(parsed_content_body,ast.UnaryOp):
        return op_map[type(parsed_content_body.op)](evaluate(parsed_content_body.operand))
    if isinstance(parsed_content_body,ast.Num):
        return parsed_content_body.n

# Input the operation and parse this operation
math_action = input("Enter a mathematical operation: ")
parse = ast.parse(math_action).body

# Return the result of the operation
print(evaluate(parse))

'''
print(type(ast.parse(cos).body[0].value))
print(dir(ast.parse(cos).body[0].value))
print(ast.parse(cos).body[0].value)
'''