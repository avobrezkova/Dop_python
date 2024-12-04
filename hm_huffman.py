import heapq
from collections import defaultdict


class Node:  # Класс Node, представляет узел в дереве Хаффмана
    def __init__(self, char, freq):
        self.char = char  # символ
        self.freq = freq  # частота
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


def huffman_tree(freq_dict):  # построение дерева Хаффмана
    prior_queue = [Node(char, freq) for char, freq in freq_dict.items()]
    heapq.heapify(prior_queue)

    while len(prior_queue) > 1:
        left = heapq.heappop(prior_queue)
        right = heapq.heappop(prior_queue)

        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        heapq.heappush(prior_queue, merged)

    return prior_queue[0]


def huffman_codes(node, current_code, huff_codes):  # построение кодов Хаффмана для символов
    if node is None:
        return

    if node.char is not None:
        huff_codes[node.char] = current_code
        return

    huffman_codes(node.left, current_code + '0', huff_codes)
    huffman_codes(node.right, current_code + '1', huff_codes)


def huffman_encoding(text):  # кодировка текста с использованием кодов Хаффмана
    freq_dict = defaultdict(int)
    for char in text:
        freq_dict[char] += 1

    root = huffman_tree(freq_dict)

    huff_codes = {}
    huffman_codes(root, '', huff_codes)

    zak_text = ''.join(huff_codes[char] for char in text)

    return zak_text, root


def huffman_decoding(zak_text, root):  # декодировка закодированного текста
    dec_text = ''
    current_node = root

    for bit in zak_text:
        if bit == '0':
            current_node = current_node.left
        else:
            current_node = current_node.right

        if current_node.char is not None:
            dec_text += current_node.char
            current_node = root

    return dec_text

# Пример использования
text = "Буря мглою небо кроет, вихри снежные крутя."
zak_text, tree_root = huffman_encoding(text)
dec_text = huffman_decoding(zak_text, tree_root)

print("Исходный текст:", text)
print("Закодированный текст:", zak_text)
print("Декодированный текст:", dec_text)