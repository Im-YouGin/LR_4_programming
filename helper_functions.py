def int_to_bit(intnumber, bin_length=None):
    """
    Converts integer number to bit sequence. Also padds the result to the specified length.
    :param intnumber:
    :param bin_length:
    :return:
    """
    tmp_number = intnumber
    res_reversed = []
    while tmp_number:
        res_reversed.append(tmp_number & 1)
        tmp_number = tmp_number >> 1

    res_reversed.reverse()
    res = res_reversed

    if bin_length != None:
        padded_res = [0] * (bin_length - len(res)) + res

    return padded_res

def bit_to_byte(bits):
    """
    WILL BE CHANGED to convert bit sequences to bytes taking max sequence width into account.
    :param bits:
    :return:
    """
    res_number = []
    tmp_res = 0
    bit_number = len(bits) - 1

    for bit in bits:
        if bit:
            a = 1 << bit_number
            tmp_res = tmp_res | a

        if bit_number:
            bit_number = bit_number - 1

        else:
            res_number.append(tmp_res)
            bit_number = len(bits)
            tmp_res = 0

    if bit_number < len(bits):
        res_number.append(tmp_res)

    return res_number

def get_bytes(filepath):
    bytes = []
    file = open(filepath, 'rb')
    data = file.read()

    for byte in data:
        bytes.append(byte)

    return bytes




print(bit_to_byte([1,0,1,1,1,0,0,1,1]))