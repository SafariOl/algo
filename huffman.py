from heapq import heappush, heappop, heapify
from collections import defaultdict

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(text):
    # Підрахунок частот символів
    freq = defaultdict(int)
    for char in text:
        if char != ' ':
            freq[char] += 1

    # Створення черги з вузлів
    heap = [Node(char, freq) for char, freq in freq.items()]
    heapify(heap)

    # Побудова дерева Хаффмана
    while len(heap) > 1:
        left = heappop(heap)
        right = heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heappush(heap, merged)

    return heap[0]

def build_huffman_codes(node, current_code, codes):
    if node is None:
        return

    if node.char is not None:
        codes[node.char] = current_code

    build_huffman_codes(node.left, current_code + "0", codes)
    build_huffman_codes(node.right, current_code + "1", codes)

def decode_huffman(root, encoded_str):
    decoded_output = ""
    current_node = root
    for bit in encoded_str:
        if bit == '0':
            current_node = current_node.left
        else:
            current_node = current_node.right

        if current_node.char is not None:
            decoded_output += current_node.char
            current_node = root

    return decoded_output

# Вхідні дані
text = "соли косули сосульки"
encoded_str = "11011101001"

# Побудова дерева Хаффмана
root = build_huffman_tree(text)

# Створення кодування Хаффмана
codes = {}
build_huffman_codes(root, "", codes)

# Декодування рядка
decoded_str = decode_huffman(root, encoded_str)
print(decoded_str)