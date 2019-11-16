#kalkulator

import ast
import operator
import sys
import  math

# A dictionary of operation
op_map = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.USub: operator.neg
    }

# A dictionary of constants
cons_dict = {
    "pi": math.pi
    "e": math.e
}

# A function that parse and calculate the content of a tree
def evaluate(parsed_content_body):
    if isinstance(parsed_content_body,list):
        return [evaluate(variable) for variable in parsed_content_body]

    if isinstance(parsed_content_body,ast.Expr):
        return evaluate(parsed_content_body.value)

    if isinstance(parsed_content_body,ast.BinOp):
        try:
            return op_map[type(parsed_content_body.op)](evaluate(parsed_content_body.left),evaluate(parsed_content_body.right))
        except KeyError:
            raise ValueError("Unsupported operator: %s" % parsed_content_body.op)

    if isinstance(parsed_content_body,ast.UnaryOp):
        try:
            return op_map[type(parsed_content_body.op)](evaluate(parsed_content_body.operand))
        except KeyError:
            raise ValueError("Unsupported operator: %s" % parsed_content_body.op)

    if isinstance(parsed_content_body,ast.Name):
        try:
            return cons_dict[parsed_content_body.id]
        except KeyError:
            raise ValueError("Unsupported constant: %s" % parsed_content_body.id)

    if ((sys.version_info[0]<=2) or (sys.version_info[0] ==3 and sys.version_info[1] <=7)) and isinstance(parsed_content_body,ast.Num):
        return parsed_content_body.n

    if ((sys.version_info[0]==3 and sys.version_info[1]>=8) or (sys.version_info[0]>3) ) and isinstance(parsed_content_body,ast.Constant):
        return  parsed_content_body.n
    raise TypeError("Unsupported type of operation {}".format(type(parsed_content_body)))


# Input the operation and parse this operation
math_action = input("Enter a mathematical operation: ")
print(math_action)
parse = ast.parse(math_action).body

# Return the result of the operation
print(evaluate(parse))

'''
print(type(ast.parse(cos).body[0].value))
print(dir(ast.parse(cos).body[0].value))
print(ast.parse(cos).body[0].value)
'''