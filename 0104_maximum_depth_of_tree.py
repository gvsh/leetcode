

# Definition for a binary tree node.

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
    
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    
    return root


def print_tree_formatted(node, level=0):
    if node:
        print_tree_formatted(node.right, level + 1)
        print(' ' * 4 * level + str(node.val))
        print_tree_formatted(node.left, level + 1)


print_tree_formatted(create_tree())



class Solution:

    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        else:
            left_height  = self.maxDepth(root.left)
            right_height = self.maxDepth(root.right)
            
            return max(left_height, right_height) + 1
        
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxDepth(create_tree()))
