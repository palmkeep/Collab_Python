#!/usr/bin env python
# -*- coding:utf-8

#
#   Uppgift 4 (A-D)
#
#   Viktor Palm och André Palmborg
#   vikpa137, andpa149
#

from math import sin


# Uppgift 4A

def merge(e, l):
    """
    Slår ihop saker.
    """
    if l:
        result = [[e]+l[0]] +  merge(e, l[1:])
        return result
    else:
        return []    

def NchooseK(l, n):
    """
    Den tar en lista och så skapar den alla delmängder av storlek n.
    """
    if len(l) == n:
        return [l]
    elif n != 0:
        return merge(l[0], NchooseK(l[1:], n-1))+ NchooseK(l[1:], n)
    else:
        return [[]]

def powerset(l, n = -1):
    """
    Den skapar powerset.
    """
    if n == -1:
        n = len(l)
    if n != 0:
        return NchooseK(l, n) + powerset(l, n-1)
    else:
        return [[]]


# Uppgift 4B

def generate_height(h0, v0, t0, a):
    """
    Returnerar en funktion som ger höjden ett föremål befinner sig på
    beroende på en variabel t. Konstanterna h0 och v0 är värdena vid
    t0; a är konstant vid alla t.
    """
    return (lambda t: h0 + v0*(t - t0) + 0.5*a*((t - t0)**2))


# Uppgift 4C

def smooth (function):
    """
    Tar en funktion och "smoothar" den och returnerar den
    nya funktionen.
    """
    dx = 0.001
    def finalFunction(x):
        value = (function(x-dx) + function(x) + function(x + dx))/3
        return value

    return finalFunction

def repeatedly_smoothed(function, times_smoothed):
    """
    Utför smooth() på en funktion givet antal gånger och returnerar 
    den nya funktionen.
    """
    for x in range(times_smoothed):
        function = smooth(function)
    
    return function

smooth_square = smooth(lambda x: x*x)
smooth_sin = smooth(lambda x: sin(x))
twice_smoothed_square = smooth(smooth_square)
twice_smoothed_sin = smooth(smooth_sin)


# Uppgift 4D 

# Help functions
def is_empty_tree(tree):
    """
    Returnerar sant/falskt beroende på om $tree är ett tomt träd.
    """
    if tree == []:
        return True
    elif isinstance(tree, list) and tree[0] == tree[1] == tree[2] == []:
        return True
    else:
        return False

def is_tree(tree):
    """
    Returnerar sant/falskt beroende på om $tree är ett träd eller inte.
    """
    if isinstance(tree, list) and len(tree) == 3:
        return True
    else:
        return False

def is_leaf(leaf):
    """
    Returnerar sant/falskt beroende på om $leaf är ett löv eller inte.
    """
    if isinstance(leaf, list) and leaf[0] == leaf[2] == []:
        if isinstance(leaf[1], int) or isinstance(leaf[1], float):
            return True
    elif isinstance(leaf, int) or isinstance(leaf, float):
        return leaf
    else:
        return False

def key(tree):
    """
    Returnerar nyckel värdet i $tree.
    """
    return tree[1]

def left_subtree(tree):
    """
    Returnerar det vänstra delträdet i $tree.
    """
    return tree[0]

def right_subtree(tree):
    """
    Returnerar det högra delträdet i $tree.
    """
    return tree[2]

def create_tree(left_subtree, key, right_subtree):
    """
    Returnerar ett träd skapat med de inmatade värdena.
    """
    return [left_subtree, key, right_subtree]
# /Help functions


def traverse(tree, inner_node_fn, leaf_fn, empty_tree_fn):
    """
    Traverserar ett träd och utför en av de tre inmatade funktionerna
    beroende på om man stötter på en inre nod, ett löv eller ett tomt träd.
    """
    if is_empty_tree(tree):
        return empty_tree_fn()
    elif is_leaf(tree):
        return leaf_fn(tree)
    elif is_tree(tree):
        left_value = traverse(left_subtree(tree), inner_node_fn, leaf_fn, empty_tree_fn)
        right_value = traverse(right_subtree(tree), inner_node_fn, leaf_fn, empty_tree_fn)
        return inner_node_fn(key(tree), left_value, right_value)


def arb_sum(tree):
    """
    Returnerar summan av alla noder i det översta trädet och alla vänstra 
    delträd och kvadraten av det vänsta lövet i det nedersta delträdet
    längst till vänster.
    """
    def inner_node_fn1(node, left_value, right_value):
        return node + left_value

    def leaf_fn1(leaf):
        return leaf**2

    def empty_tree_fn1():
        return 0
    
    return traverse(tree, inner_node_fn1, leaf_fn1, empty_tree_fn1)

def contains_key(key, tree):
    """
    Returnerar sant/falskt beroende på om traverseringen stötter på det
    inmatade $key värdet.
    """
    def inner_node_fn2(node, left_value, right_value):
        return node == key or left_value or right_value

    def leaf_fn2(leaf):
        if leaf == key:
            return True
        else:
            return False

    def empty_tree_fn2():
        return False

    return traverse(tree, inner_node_fn2, leaf_fn2, empty_tree_fn2)

def tree_size(tree):
    """
    Returnerar antalet noder och löv.
    """
    def inner_node_fn3(node, left_value, right_value):
        return 1 + left_value + right_value
    def leaf_fn3(leaf):
        return 1
    def empty_tree_fn3():
        return 0

    return traverse(tree, inner_node_fn3, leaf_fn3, empty_tree_fn3)

def tree_depth(tree):
    """
    Returnerar hur många nivåer det finns i trädet. Översta noden räknas som
    en nivå sedan räknas varje nod eller löv som en nivå.
    """
    def inner_node_fn4(node, left_value, right_value):
        return 1 + max(left_value, right_value)
    def leaf_fn4(leaf):
        return 1
    def empty_tree_fn4():
        return 0

    return traverse(tree, inner_node_fn4, leaf_fn4, empty_tree_fn4)

