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
    bit_number = 7

    for bit in bits:
        if bit:
            new = 1 << bit_number
            tmp_res = tmp_res | new

        if bit_number:
            bit_number = bit_number - 1

        else:
            res_number.append(tmp_res)
            bit_number = 7
            tmp_res = 0

    if bit_number < 7:
        res_number.append(tmp_res)

    return res_number


def byte_to_bit(seq_bytes):
    bits = []

    for bt in seq_bytes:
        value = bt

        for one_more in range(8, 0, -1):
            idk_bit = one_more - 1
            next_b = 1 & (value >> idk_bit)
            bits.append(next_b)

    return bits


def bits_to_int(bits):
    num = 0
    b_in_bits = [b for b in bits]
    b_in_bits.reverse()

    for idk_bit in range(len(b_in_bits)):
        if b_in_bits[idk_bit]:
            num = num | (1 << idk_bit)

    return num


def get_bytes(filepath):
    bytes = []
    file = open(filepath, 'rb')
    data = file.read()

    for byte in data:
        bytes.append(byte)

    return bytes
