#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/9 5:48 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 158. Read N Characters Given Read4 II - Call multiple times.py
# @Software: IntelliJ IDEA

# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer


def read4(buf):
    global file_content
    i = 0
    while i < len(file_content) and i < 4:
        buf[i] = file_content[i]
        i += 1

    if len(file_content) > 4:
        file_content = file_content[4:]
    else:
        file_content = ""
    return i

"""
The read4 API is already defined for you.

    @param buf, a list of characters
    @return an integer
    def read4(buf):


# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf = [' '] * 4 # Create buffer with enough space to store characters
read4(buf) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""
class Solution:
    def __init__(self):
        self.bp = 0
        self.length = 0
        self.buffer = [" "] * 4
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        i = 0
        while i < n:
            if self.bp == self.length:
                self.bp = 0
                self.length = read4(self.buffer)
                if self.length == 0:
                    break
            buf[i] = self.buffer[self.bp]
            i += 1
            self.bp += 1
        return i


if __name__ == "__main__":
    global file_content
    buf = ['' for _ in range(100)]

    # file_content = "a"
    # print(buf[:Solution().read(buf, 9)])

    file_content = "abcde"
    sol = Solution()
    print(sol.read(buf, 4))
    print(sol.read(buf, 2))
    # print(sol.read(buf, 1))