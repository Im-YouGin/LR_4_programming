import pickle
from sys import getsizeof
import struct
import io

from PIL import Image
data = open('bmp (2).bmp', 'rb').read()
# print(data)

maximum_table_size = 2**12

def compress(data):
    dictionary_size = 256
    dictionary = {bytes(chr(i), encoding='utf8'): i for i in range(dictionary_size)}
    # print(dictionary)
    string = b""
    dictionary[string] = dictionary_size
    dictionary_size += 1
    compressed_data = []

    for symbol in data:
        symbol = struct.pack('B', symbol)
        string_plus_symbol = string + symbol
        # print(string_plus_symbol)
        if string_plus_symbol in dictionary:
            string = string_plus_symbol
        else:
            try:
                compressed_data.append(dictionary[string])
                # print('get previous from dct')
            except:
                # print('-')
                dictionary[string] = dictionary_size
                dictionary_size += 1
            if(len(dictionary) <= maximum_table_size):
                dictionary[string_plus_symbol] = dictionary_size
                dictionary_size += 1
                # print('add to dct previous + new')
            string = symbol
    if string in dictionary:
        compressed_data.append(dictionary[string])
    dct_reverse = {v: k for k,v in dictionary.items()}
    return compressed_data, dictionary_size

def decompress(compressed_data, dict_size):
    next_code = 256
    decompressed_data = b""
    string = b""
    dictionary_size = dict_size
    dictionary = dict([(x, bytes(chr(x), encoding='utf8')) for x in range(dictionary_size)])
    dictionary[dictionary_size] = string
    dictionary_size += 1
    for code in compressed_data:
        if not (code in dictionary):
            dictionary[code] = string + string[0]
        decompressed_data += dictionary[code]
        if not(len(string) == 0):
            dictionary[next_code] = string + struct.pack('B', dictionary[code][0])
            next_code += 1
        string = dictionary[code]
    return decompressed_data

if __name__ == '__main__':
    print('Original:', getsizeof(data))
    print(data)
    compressed, size = compress(data)
    print(compressed)
    # s = pickle.dumps()

    print('Compressed:', getsizeof(compressed))

    decompressed = decompress(data, size)
    _bytes = bytearray(decompressed)
    image = Image.open(io.BytesIO(_bytes))
    image.show()
    print('Decompressed:', getsizeof(_bytes))

