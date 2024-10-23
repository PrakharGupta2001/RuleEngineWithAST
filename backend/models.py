# backend/models.py

class Node:
    def __init__(self, node_type, value=None, left=None, right=None):
        self.type = node_type  # "operator" for AND/OR, "operand" for conditions
        self.value = value     # For operands, it stores the condition (e.g., "age > 30")
        self.left = left       # Left child (Node)
        self.right = right     # Right child (Node)

    def __repr__(self):
        """Returns a string representation of the node."""
        return f"Node(type={self.type}, value={self.value}, left={self.left}, right={self.right})"

    def update_value(self, new_value):
        """Updates the value of the current node."""
        self.value = new_value

    def add_subexpression(self, new_node, side="left"):
        """Adds a new subexpression (node) to the specified side."""
        if side == "left":
            self.left = new_node
        elif side == "right":
            self.right = new_node

    def remove_subexpression(self, side="left"):
        """Removes a subexpression (node) from the specified side."""
        if side == "left":
            self.left = None
        elif side == "right":
            self.right = None
