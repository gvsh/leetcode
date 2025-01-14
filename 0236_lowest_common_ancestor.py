
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




def lca(root, p, q, p_flag=False, q_flag=False, found=False, result=None):

    if not root:
        return process_empty_node()
    

    if is_leaf(root):

        if root.val == p:
            p_flag = True
        if root.val == q:
            q_flag = True

        return p_flag, q_flag, found, None
    
    else:

        if root.left:
            # left(root, result)
            p_flag, q_flag, found = lca(root.left, p, q, p_flag, q_flag, found)

        if p_flag and q_flag and not found:
            found = True
            return p_flag, q_flag, found, root

        if root.right:
            p_flag, q_flag, found = lca(root.right, p, q, p_flag, q_flag, found)
            # right(root, result)

        if p_flag and q_flag and not found:
            found = True
            return p_flag, q_flag, found, root
        # below(root, result)

    return p_flag, q_flag, found, None


def process_empty_node():

    return False, False, False


def is_leaf(node):

    if not node.left and not node.right:
        return True




    
    sample_tree = create_tree()
    # sample_tree.print_tree()

    calculate_sum_root_to_leaf(sample_tree, 0)
