# backend/rule_engine.py

import ast
from models import Node

# Define allowed attributes for validation
ALLOWED_ATTRIBUTES = ['age', 'department', 'salary', 'experience']

# Define custom functions (as an example)
custom_functions = {
    'is_high_salary': lambda salary: salary > 100000
}

def validate_attribute(attribute):
    """Check if the attribute is part of the allowed attributes."""
    if attribute not in ALLOWED_ATTRIBUTES:
        raise ValueError(f"Attribute '{attribute}' is not allowed. Allowed attributes: {ALLOWED_ATTRIBUTES}")

def parse_expression(expression):
    """Recursively parse a Python expression and build an AST."""
    if isinstance(expression, ast.BoolOp):
        # Handle AND/OR operators
        left = parse_expression(expression.values[0])
        right = parse_expression(expression.values[1])
        operator = "AND" if isinstance(expression.op, ast.And) else "OR"
        return Node(node_type="operator", value=operator, left=left, right=right)
    elif isinstance(expression, ast.Compare):
        # Handle comparison (operand)
        left = expression.left.id
        validate_attribute(left)  # Validate that the attribute is allowed
        operator = expression.ops[0].__class__.__name__
        right = expression.comparators[0].n
        condition = f"{left} {operator} {right}"
        return Node(node_type="operand", value=condition)
    elif isinstance(expression, ast.Call):
        # Handle custom functions
        func_name = expression.func.id
        if func_name not in custom_functions:
            raise ValueError(f"Undefined function: {func_name}")
        arg_value = expression.args[0].n
        return Node(node_type="operand", value=f"{func_name}({arg_value})")
    else:
        raise ValueError("Unsupported expression type")


def create_rule(rule_string):
    """Converts a string rule into an AST Node."""
    try:
        # Normalize the rule string to use lowercase logical operators
        rule_string = rule_string.replace("AND", "and").replace("OR", "or")
        # Parse the rule string into an Abstract Syntax Tree (AST)
        tree = ast.parse(rule_string, mode='eval')
        # Recursively build our custom AST from the Python AST
        return parse_expression(tree.body)
    except Exception as e:
        raise ValueError(f"Error creating rule: {e}")

def combine_rules(rules, operator="AND"):
    """Combines multiple AST nodes using a specified operator."""
    if not rules:
        return None
    root = rules[0]
    for i in range(1, len(rules)):
        root = Node(node_type="operator", value=operator, left=root, right=rules[i])
    return root

def evaluate_condition(condition, data):
    """Evaluates a single condition."""
    if '(' in condition:  # Handle custom functions
        func_name, arg = condition.split('(')
        arg = int(arg.strip(')'))
        return custom_functions[func_name](arg)

    left, operator, right = condition.split()
    right = int(right)  # Convert the right-hand side to an integer for comparison
    if operator == 'Gt':
        return data[left] > right
    elif operator == 'Lt':
        return data[left] < right
    elif operator == 'Eq':
        return data[left] == right
    else:
        raise ValueError(f"Unsupported operator: {operator}")

def evaluate_rule(node, data):
    """Recursively evaluates the AST against the provided data."""
    if node.type == "operand":
        # Evaluate the condition
        return evaluate_condition(node.value, data)
    elif node.type == "operator":
        # Evaluate the left and right sub-trees based on the operator
        left_result = evaluate_rule(node.left, data)
        right_result = evaluate_rule(node.right, data)
        if node.value == "AND":
            return left_result and right_result
        elif node.value == "OR":
            return left_result or right_result
    return False

def modify_rule(node, new_value=None, operator=None):
    """Modify an existing rule."""
    if new_value:
        node.update_value(new_value)
    if operator and node.type == "operator":
        node.value = operator
