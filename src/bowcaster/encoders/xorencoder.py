# Copyright (c) 2013
# - Zachary Cutlip <uid000@gmail.com>
# - Tactical Network Solutions, LLC
# 
# See LICENSE.txt for more details.
# 
class XorEncoder(object):
    """
    Base class for architecture-specific XOR encoders. Provides self.encode().
    """
    def encode(self,data,key):
        if len(data) % len(key) != 0:
            raise "Data length must be a multiple of key length"

        key_idx=0
        xor_data=""

        for x in range(len(data)):
            xor_data=xor_data+chr(ord(data[x]) ^ ord(key[key_idx]))
            key_idx=(key_idx + 1) % len(key)

        return xor_data
