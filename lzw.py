import pickle

with open('14284907446_733a076fab_n.jpg', 'rb') as f:
    data = str(f.read())


dictionary_size = 256
dictionary = {chr(i): i for i in range(dictionary_size)}
string = ""             # String is null.
compressed_data = []    # variable to store the compressed data.
maximum_table_size = 2**12
# iterating through the input symbols.
# LZW Compression algorithm
for symbol in data:
    string_plus_symbol = string + symbol  # get input symbol.
    if string_plus_symbol in dictionary:
        string = string_plus_symbol
    else:
        compressed_data.append(dictionary[string])
        if(len(dictionary) <= maximum_table_size):
            dictionary[string_plus_symbol] = dictionary_size
            dictionary_size += 1
        string = symbol

if string in dictionary:
    compressed_data.append(dictionary[string])

c = pickle.dumps(compressed_data)
with open('file1.txt', 'wb') as f:
    f.write(c)


with open('file1.txt', 'rb') as f:
    compressed_data = pickle.loads(f.read())

next_code = 256
decompressed_data = ""
string = ""

# Reading the compressed file.

# Building and initializing the dictionary.
dictionary_size = 256
dictionary = dict([(x, chr(x)) for x in range(dictionary_size)])

# iterating through the codes.
# LZW Decompression algorithm
for code in compressed_data:
    if not (code in dictionary):
        dictionary[code] = string + (string[0])
    decompressed_data += dictionary[code]
    if not(len(string) == 0):
        dictionary[next_code] = string + (dictionary[code][0])
        next_code += 1
    string = dictionary[code]


with open('file1.txt', 'w') as f:
    f.write(str(decompressed_data))
