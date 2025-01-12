

class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def print_tree(self):
        

        print(f"root.val: {self.val}")

        if self.left:
            print(f"left tree of {self.val}:")
            self.left.print_tree()

        print(f"Done printing left tree of {self.val}")
        print("-" * 40)

        if self.right:
            print(f"right tree of {self.val}:")
            self.right.print_tree()

        print(f"Done printing right tree of {self.val}")
        print("-" * 40)


        print(f"Exiting call for {self.val}")
        print("=" * 80)
        print("=" * 80)


def process_empty_node():

    return 0


def is_leaf(node):

    if not node.left and not node.right:
        return True


def init_result():
    pass


def process_leaf(node, result):
    
    return 1


def left(node, result):
    pass


def below(node, result):
    pass


def right(node, result):
    pass


def result(result):
    pass

def create_tree():
    
    # root = TreeNode(3)
    # root.left = TreeNode(9)
    # root.right = TreeNode(2)
    # root.right.left = TreeNode(5)
    # root.right.right = TreeNode(7)
    
    root = TreeNode(4)
    root.left = TreeNode(9)
    root.right = TreeNode(0)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(1)
    
    return root


def print_tree_formatted(node, level=0):
    if node:
        print_tree_formatted(node.right, level + 1)
        print(' ' * 4 * level + str(node.val))
        print_tree_formatted(node.left, level + 1)


print_tree_formatted(create_tree())


class Result:
    
    def __init__(self, total_sum=0, node_num=0):
        self.total_sum = total_sum
        self.node_num = node_num

def outer():

    result = Result()
    
    sample_tree = create_tree()
    # sample_tree.print_tree()

    result = calculate_sum_root_to_leaf(sample_tree, result)

    print(f"{result=}")
    print(f"{result.total_sum=}")
    print(f"{result.node_num=}")

    
def calculate_sum_root_to_leaf(node, result):

    if not node:
        return process_empty_node()
    

    if is_leaf(node):

        print("=" * 80)
        print(f"{node.val=}")
        print("=" * 80)

        result.node_num = result.node_num * 10 + node.val
        current_sum = result.node_num

        print(f"{current_sum=}")

        print(f"{result.total_sum=}")
        result.total_sum += current_sum
        print(f"{result.total_sum=}")
        
        print("=" * 80)

        return result
    
    else:

        below(node, result)
        result.node_num = result.node_num * 10 + node.val

        if node.left:
            # left(node, result)
            result = calculate_sum_root_to_leaf(node.left, result)

        if node.right:
            result = calculate_sum_root_to_leaf(node.right, result)
            # right(node, result)

    return result


        

if __name__ == "__main__":

    result = Result()
    
    sample_tree = create_tree()
    # sample_tree.print_tree()

    result = calculate_sum_root_to_leaf(sample_tree, result)

    print(f"{result=}")
    print(f"{result.total_sum=}")
    print(f"{result.node_num=}")


# Sum Root to Leaf Numbers
# Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.
# An example is the root-to-leaf path 1->2->3 which represents the number 123.
# Find the total sum of all root-to-leaf numbers.

# A leaf is a node with no children.

# Example 1:
# Input: [1,2,3]
#     1
#    / \
#   2   3
# Output: 25
# Explanation:
# The root-to-leaf path 1->2 represents the number 12.
# The root-to-leaf path 1->3 represents the number 13.
# Therefore, sum = 12 + 13 = 25.

# Example 2:
# Input: [4,9,0,5,1]
#     4
#    / \
#   9   0
#  / \
# 5   1
# Output: 1026
# Explanation:
# The root-to-leaf path 4->9->5 represents the number 495.
# The root-to-leaf path 4->9->1 represents the number 491.
# The root-to-leaf path 4->0 represents the number 40.
# Therefore, sum = 495 + 491 + 40 = 1026.




















