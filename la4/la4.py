
# Uppgift 4A

def powerset(orig_set):
    powerset = [[]] # Start with a list containing the empty set
    for i in range(1, 1 + len(orig_set)):
        powerset = unordered_choose(orig_set, i, powerset)
    return powerset

def unordered_choose(list_elements, cardinality, list_chosen = [], chosen = []):
    for i in range(1 + len(list_elements) - cardinality):
        chosen.append(list_elements[i])

        if cardinality == 1:
            list_chosen.append(chosen[:])
        else:
            list_chosen = unordered_choose( list_elements[i+1:], cardinality - 1,
                                            list_chosen, chosen)
        chosen.pop()

    return list_chosen


# Uppgift 4B

def generate_height(h0, v0, t0, a):
    return (lambda t: h0 + v0*(t - t0) + 0.5*a*((t - t0)**2))


# Uppgift 4C

def smooth_square():
    smooth_square = smooth(lambda x: x*x)
    smooth_sin = smooth(lambda x: sin(x))
    twice_smoothed_square = smooth(smooth_square)
    twice_smoothed_sin = smooth(smooth_sin)

def smooth (function):
    dx = 0.001
    def finalFunction(x):
        value = (function(x-dx) + function(x) + function(x + dx))/3
        return value

    return finalFunction

def repeatedly_smoothed(function, times_smoothed):
    for x in range(times_smoothed):
        function = smooth(function)
    
    return function

    
# Uppgift 4D 

# Help functions
def is_empty_tree(tree):
    if tree == []:
        return True
    elif isinstance(tree, list) and tree[0] == tree[1] == tree[2] == []:
        return True
    else:
        return False

def is_tree(tree):
    if isinstance(tree, list) and len(tree) == 3:
        return True
    else:
        return False

def is_leaf(leaf):
    if isinstance(leaf, list) and leaf[0] == leaf[2] == []:
        if isinstance(leaf[1], int) or isinstance(leaf[1], float):
            return True
    elif isinstance(leaf, int) or isinstance(leaf, float):
        return leaf
    else:
        return False

def key(tree):
    return tree[1]

def left_subtree(tree):
    return tree[0]

def right_subtree(tree):
    return tree[2]

def create_tree(left_subtree, key, right_subtree):
    return [left_subtree, key, right_subtree]
# /Help functions


def traverse(tree, inner_node_fn, leaf_fn, empty_tree_fn):
    if is_empty_tree(tree):
        return empty_tree_fn()
    elif is_leaf(tree):
        return leaf_fn(tree)
    elif is_tree(tree):
        left_value = traverse(left_subtree(tree), inner_node_fn, leaf_fn, empty_tree_fn)
        right_value = traverse(right_subtree(tree), inner_node_fn, leaf_fn, empty_tree_fn)
        return inner_node_fn(key(tree), left_value, right_value)


def arb_sum(tree):
    def inner_node_fn1(node, left_value, right_value):
        return node + left_value

    def leaf_fn1(leaf):
        return leaf**2

    def empty_tree_fn1():
        return 0
    
    return traverse(tree, inner_node_fn1, leaf_fn1, empty_tree_fn1)

def contains_key(key, tree):
    def inner_node_fn2(node, left_value, right_value):
        if node == key or left_value or right_value:
            return True
        else: 
            return False

    def leaf_fn2(leaf):
        if leaf == key:
            return True
        else:
            return False

    def empty_tree_fn2():
        return False

    return traverse(tree, inner_node_fn2, leaf_fn2, empty_tree_fn2)

def tree_size(tree):
    def inner_node_fn3(node, left_value, right_value):
        return 1 + left_value + right_value
    def leaf_fn3(leaf):
        return 1
    def empty_tree_fn3():
        return 0

    return traverse(tree, inner_node_fn3, leaf_fn3, empty_tree_fn3)

def tree_depth(tree):
    def inner_node_fn4(node, left_value, right_value):
        return 1 + max(left_value, right_value)
    def leaf_fn4(leaf):
        return 1
    def empty_tree_fn4():
        return 0

    return traverse(tree, inner_node_fn4, leaf_fn4, empty_tree_fn4)

