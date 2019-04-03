# -*- coding: utf-8 -*-
from tree import TreeNode
import sys

sys.setrecursionlimit(1000000000)

# --- FUC DEF ---

def import_Tree(string):
    # importing tree (look to export function)
    # return root elem of tree
    string = string[::-1]
    root = TreeNode(string[0], string[1])
    for i in string[2:]:
        tmptreenode = TreeNode(root, i)
        root.parent = tmptreenode
        root = tmptreenode
    return root


def export_Tree(root):
    # exporting tree with given root based on that letter is on left and only last has right str
    # return str
    toret = ""
    while type(root.right) is not str:
        toret += root.left
        root = root.right
    toret += root.right
    return toret


def find_in_tree(root, letter):
    # finding path in bin tree for given letter
    # returns array of 0 and 1 based on path where (0 means right and 1 means left)
    routeArray = []
    treenode = root
    try:
        while treenode.hasBouth():
            if treenode.left == letter:
                routeArray.append(1)
                return routeArray
            elif treenode.right == letter:
                routeArray.append(0)
                return routeArray
            else:
                treenode = treenode.right
                routeArray.append(0)
    except AttributeError:
        print(AttributeError, " ", treenode, letter) # if letter is given and it not pas test in while


def alfarray(alphabet="0123456789abcdefghijklmnopqrstwvuxyzABCDEFGHIJKLMNOPQRSTWVUXYZ,. \t\n", file="file.txt"):
    # generating array of signs based on given alphabet and file which is preparation to encode and decode
    toret = []
    signgs = 0
    for sign in alphabet:
        toret.append([sign, 0])
    with open(file, 'r') as f:
        for sign in f.read():
            for val in toret:
                if val[0] == sign:
                    val[1] = val[1] + 1
                    break
        f.close()
    return sorted([val for val in toret if val[1] != 0], key=lambda v: v[1])
    # list of list of letter and number, sorted reversely by number which indicates how many occurrences has sign


def encode(tree, file="file.txt"): # function taking tree root and normal text string to encode into bite string
    toret = []
    with open(file) as f:
        for sign in f.read():
            tmp = find_in_tree(tree, sign)
            toret.extend(tmp)
    return ''.join(str(e) for e in toret)


def decode(tree, string): # function taking tree root and bit string to decode to normal text
    toret = []
    treenode = tree
    for sign in string:
        if sign == str(0):
            treenode = treenode.right
        else:
            treenode = treenode.left
        if type(treenode) is str:
            toret.append(treenode)
            treenode = tree
    return ''.join(str(item) for item in toret)


# --- END FUNC DEF ---

# --- MAIN CONTENT ---
array = alfarray()

for i in range(0, len(array) - 1):
    if isinstance(array[0], TreeNode):
        tmp2 = array[0]
        tmp = TreeNode(tmp2, array[1][0])
        tmp2.parent = tmp
        array.pop(0)
        array.pop(0)
        array.insert(0, tmp)
    else:
        root = TreeNode(array[0][0], array[1][0])
        array.pop(0)
        array.pop(0)
        array.insert(0, root)

with open("encode.txt", "w") as f:
    # print(array)
    array2 = encode(array[0])
    f.write(array2)

with open("decoded.txt", "w") as f:
    # print(array2)
    string = decode(array[0], array2)
    # print(string)
    f.write(string)

# --- END MAIN ---