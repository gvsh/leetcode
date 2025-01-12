

def calculate_tree_height(node):

    if not node:
        return process_empty_node()
    
    result = init_result()

    if is_leaf(node):

        return process_leaf(node, result)
    
    else:

        if node.left_child:
            left(node, result)
            result.left_result = calculate_tree_height(node.left_child)

        below(node, result)

        if node.right_child:
            result.right_result = calculate_tree_height(node.right_child)
            right(node, result)

    return result(result)


def process_empty_node():

    return 0


def is_leaf(node):

    if not node.left_child and not node.right_child:
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

