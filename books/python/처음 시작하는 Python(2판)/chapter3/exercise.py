# >>> bool(1)
# True
# >>> bool(0)
# False
# >>> bool(chan)
# Traceback (most recent call last):
#   File "<pyshell#40>", line 1, in <module>
#     bool(chan)
# NameError: name 'chan' is not defined
# >>> bool( "CHAN")
# True
# >>> million = 1000000
# >>> type(million)
# <class 'int'>
# >>> million = 1_000_000
# >>> type(million)
# <class 'int'>
# >>> million
# 1000000
# >>> 1_2_3
# 123
# >>> 7//2
# 3
# >>> 7/3
# 2.3333333333333335
# >>> 7//3
# 2
# >>> 10**2
# 100
# >>> 10**3
# 1000
# >>> 10**4
# 10000
# >>> type(9/5)
# <class 'float'>
# >>> type(9//5)
# <class 'int'>
# >>> divmod(5/6
#        )
# Traceback (most recent call last):
#   File "<pyshell#57>", line 1, in <module>
#     divmod(5/6
# TypeError: divmod expected 2 arguments, got 1
# >>> 9%5
# 4
# >>> divmod(9, 5)
# (1, 4)
# >>> 0b10
# 2
# >>> 0b11
# 3
# >>> 0b12
# SyntaxError: invalid digit '2' in binary literal
# >>> 0b20
# SyntaxError: invalid digit '2' in binary literal
# >>> 0b111
# 7
# >>> 0b101
# 5
# >>> 0b100
# 4
# >>> 0b100000000
# 256
# >>> 0o1
# 1
# >>> 0o11
# 9
# >>> 0x11
# 17
# >>> value = 65
# >>> value
# 65
# >>> bin(value)
# '0b1000001'
# >>> 0b1000001
# 65
# >>> true + 2
# Traceback (most recent call last):
#   File "<pyshell#75>", line 1, in <module>
#     true + 2
# NameError: name 'true' is not defined
# >>> True + 2
# 3
# >>> False -1
# -1
# >>> just kidding
# SyntaxError: invalid syntax
# >>> 5.
# 5.0
# >>> type(5.)
# <class 'float'>
# >>> type(43+2.)
# <class 'float'>
# >>> type(True+1)
# <class 'int'>
# >>> 