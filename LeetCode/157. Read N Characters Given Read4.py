#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/9 4:07 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 157. Read N Characters Given Read4.py
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


class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        read_bytes = 0
        buffer = [''] * 4
        for i in range(n // 4 + 1):
            size = read4(buffer)
            if size:
                # 字节流的长度 比 n 大， 可能size是4， 但最后只需要1个
                # 如果size没有读满四个， 表示数据读完了， 依然是取更小的那个
                size = min(size, n - read_bytes)
                buf[read_bytes : read_bytes + size] = buffer[ : size]
                read_bytes += size
            # 当size等于0时， 直接结束
            else:
                break
        return read_bytes

    def readn(self, buf, n):
        i = 0
        while i < n:
            buf4 = ['','','','']
            count = read4(buf4) # Read file into buf4.
            if not count: break # EOF
            count = min(count, n - i)
            buf[i:] = buf4[:count] # Copy from buf4 to buf.
            i += count
        return i


if __name__ == "__main__":
    global file_content
    buf = ['' for _ in range(100)]

    file_content = "a"
    print(buf[:Solution().read(buf, 9)])

    file_content = "abcdefghijklmnop"
    print(buf[:Solution().read(buf, 9)])