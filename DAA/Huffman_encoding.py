import heapq

print("HUFFMAN ENCODING USING GREEDY ALGORITHM")

# Function to generate Huffman codes
def huffman_encoding(characters, frequencies):

    heap = []

    # Insert characters and frequencies into the min heap
    for i in range(len(characters)):
        heapq.heappush(heap, (frequencies[i], i, characters[i]))

    print("\nInitial Character Frequencies:")
    for i in range(len(characters)):
        print(characters[i], ":", frequencies[i])

    # Build Huffman Tree
    while len(heap) > 1:

        # Remove two nodes with minimum frequencies
        freq1, id1, left = heapq.heappop(heap)
        freq2, id2, right = heapq.heappop(heap)

        print("\nCombining:", left, "(", freq1, ") and",
              right, "(", freq2, ")")

        # Create a new internal node
        new_node = (left, right)

        heapq.heappush(heap, (freq1 + freq2, min(id1, id2), new_node))

    # Generate Huffman codes
    root = heap[0][2]
    codes = {}

    def generate_codes(node, code):

        if isinstance(node, str):
            codes[node] = code if code != "" else "0"
            return

        left, right = node

        generate_codes(left, code + "0")
        generate_codes(right, code + "1")

    generate_codes(root, "")

    return codes


# Main Program
n = int(input("Enter number of characters: "))

characters = []
frequencies = []

for i in range(n):
    ch = input("\nEnter character: ")
    freq = int(input("Enter frequency: "))

    characters.append(ch)
    frequencies.append(freq)

# Generate Huffman codes
codes = huffman_encoding(characters, frequencies)

print("\nHuffman Codes:")
for ch in characters:
    print(ch, ":", codes[ch])