"""class Node:
    def __init__(self, freq,data):
        self.freq= freq
        self.data=data
        self.left = None
        self.right = None
"""


def decodeHuff(root, s):
    """Decodes/Prints a huffman string.
    Solution to Hackerrank challenge: https://www.hackerrank.com/challenges/tree-huffman-decoding/problem

    Args:
        root (Node): The root of the huffman tree.
        s (str): The binary huffman string to be decoded.

    Returns:
        None.
    """

    decoded_str = ""
    my_node = root

    for char in s:
        if char == '0':
            my_node = my_node.left
        elif char == '1':
            my_node = my_node.right

        # check if node is leaf
        if (my_node.left == None) and (my_node.right == None):
            decoded_str += my_node.data
            my_node = root

    print(decoded_str)
