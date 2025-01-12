

# from abc import ABC, abstractmethod

# class BinaryTreeTraversal(ABC):

#     def __init__(self, tree):
#         self.tree = tree

#     def traverse_node(self, position):

#         result = self.init_result()

#         if self.tree.is_external(position):
#             self.external(position, result)
#         else:
#             self.left(position, result)

#             result.left_result = self.traverse_node(self.tree.left_child(position))

#             self.below(position, result)

#             result.right_result = self.traverse_node(self.tree.right_child(position))

#             self.right(position, result)

#         return self.result(result)

#     @abstractmethod
#     def init_result(self):
#         pass

#     @abstractmethod
#     def external(self, position, result):
#         pass

#     @abstractmethod
#     def left(self, position, result):
#         pass

#     @abstractmethod
#     def below(self, position, result):
#         pass

#     @abstractmethod
#     def right(self, position, result):
#         pass

#     @abstractmethod
#     def result(self, result):
#         pass






def traverse_node(node):

    result = init_result()

    if is_leaf(node):

        process_leaf(node, result)
    
    else:
        left(node, result)

        result.left_result = traverse_node(node.left_child)

        below(node, result)

        result.right_result = traverse_node(node.right_child)

        right(node, result)

    return result(result)

def is_leaf():
    pass

def init_result():
    pass

def process_leaf(node, result):
    pass

def left(node, result):
    pass

def below(node, result):
    pass

def right(node, result):
    pass

def result(result):
    pass

