class Node:
    def __init__(self, name, children):
        self.name = name
        self.children = children

def build_tree():
    childs_of_six = [
        Node('8', []),
        Node('9', [])
    ]

    chils_of_five = [
        Node('10', [])
    ]

    childs_of_two = [
        Node('5', chils_of_five),
        Node('6', childs_of_six)
    ]

    childs_of_three = [
        Node('7', [])
    ]

    childs = [
        Node('2', childs_of_two),
        Node('3', childs_of_three),
        Node('4', [])
    ]

    return Node('1', childs)

def contains(node, search):
    for child in node.children:
        if child.name == search:
            return True
    return False

def path_to_node(root, node):
    if contains(root, node):
        return [root.name]
    else:
        for child in root.children:
            path = path_to_node(child, node)
            if path != []:
                path.insert(0, root.name)
                return path
        return []

def get_common_parent(path_to_first, path_to_second):
    i = min(len(path_to_first), len(path_to_second)) - 1
    while i >= 0:
        if path_to_first[i] == path_to_second[i]:
            return path_to_first[i]
        else:
            i -= 1

if __name__ == "__main__":

    first = input('Give me the first node: ')
    second = input('Give me the second node: ')

    root = build_tree()
    path_to_first = path_to_node(root, first)
    if path_to_first == []:
        raise Exception(f'node {first} not found')
    path_to_second = path_to_node(root, second)
    if path_to_first == []:
        raise Exception(f'node {second} not found')

    common_parent = get_common_parent(path_to_first, path_to_second)
    print(f'the common parent between {first} and {second} is {common_parent}')