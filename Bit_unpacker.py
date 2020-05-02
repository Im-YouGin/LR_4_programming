from helper_functions import *
import struct


class Bit_unpacker:

    __INIT_Table_LENGTH = 256
    __NEW_POINT = 257

    def __init__(self, initial_length):
        self.__initial_length = initial_length
        self.__cods_size = initial_length
        self.__min_width = 8
        self.__passed = 0
        self.__dislocation = 0
        self.__seq_of_bit = []
        self.__unpacked = []

    @property
    def init_tb_length(self):
        return Bit_unpacker.__INIT_Table_LENGTH

    @property
    def new_point(self):
        return Bit_unpacker.__NEW_POINT

    @property
    def initial_length(self):
        return self.__initial_length

    @property
    def code_size(self):
        return self.__cods_size

    @code_size.setter
    def code_size(self, value):
        self.__cods_size = value

    @property
    def min_width(self):
        return self.__min_width

    @min_width.setter
    def min_width(self, value):
        self.__min_width = value

    @property
    def passed(self):
        return self.__passed

    def re_passed(self, value):
        self.__passed = value

    @property
    def relocate(self):
        return self.__dislocation

    def relocated(self, value):
        self.__dislocation = value

    def unpacked_val(self, value):
        self.__unpacked.append(value)

    @property
    def unpacked(self):
        return self.__unpacked

    def unpack(self, bytepoint):
        while (1 << self.min_width) < self.code_size:
            self.min_width += 1

        self.width_point = self.min_width

        for bit in byte_to_bit(bytepoint):
            self.relocated((self.relocate + 1) % 8)

            if self.passed > 0:
                self.re_passed(self.passed - 1)
                continue

            self.__seq_of_bit.append(bit)

            if len(self.__seq_of_bit) == self.width_point:
                self.code = bits_to_int(self.__seq_of_bit)
                self.__seq_of_bit = []
                self.unpacked_val(self.code)

                self.code_size += 1

                if self.code in [self.new_point, self.init_tb_length]:
                    self.code_size = self.initial_length
                    self.width_point = self.min_width

                else:
                    while self.code_size >= (2**self.width_point):
                        self.width_point += 1

                if self.code == self.new_point:
                    self.re_passed((8 - self.passed) % 8)

        return self.unpacked


decom = Bit_unpacker(300)
print(decom.unpack(b'3\x98LF#\x08\x82\x01\x02\x82\x1eM\xf0X\x08'))
