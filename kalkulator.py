#kalkulator

import ast
import operator

op_map = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.USub: operator.neg
    }

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


cos = input("Podaj działanie: ")
parse = ast.parse(cos).body
print(evaluate(parse))

print(type(ast.parse(cos).body[0].value.op))
'''
print(type(ast.parse(cos).body[0].value))
print(dir(ast.parse(cos).body[0].value))
print(ast.parse(cos).body[0].value)
'''