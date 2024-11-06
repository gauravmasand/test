#alpha beta

# Define a simple Node class for the game tree
class Node:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children or []

# Alpha-beta pruning algorithm
def alpha_beta(node, depth, alpha, beta, is_maximizing_player):
    if depth == 0 or not node.children:
        return node.value

    if is_maximizing_player:
        best_value = float("-inf")
        for child in node.children:
            child_value = alpha_beta(child, depth - 1, alpha, beta, False)
            best_value = max(best_value, child_value)
            alpha = max(alpha, best_value)
            if beta <= alpha:
                break  # Prune the subtree
        return best_value
    else:
        best_value = float("inf")
        for child in node.children:
            child_value = alpha_beta(child, depth - 1, alpha, beta, True)
            best_value = min(best_value, child_value)
            beta = min(beta, best_value)
            if beta <= alpha:
                break  # Prune the subtree
        return best_value

# Example usage
root = Node(None, [Node(3, [Node(5), Node(2), Node(9)]), Node(6, [Node(8), Node(4), Node(7)])])
best_value = alpha_beta(root, 3, float("-inf"), float("inf"), True)
print("Best value:", best_value)

#o(b^n/2)
