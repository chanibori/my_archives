# 슬라이스를 사용하여 한 문자열에서 문자열 일부(substring)를 추출할 수 있다.

# 1. [:]              : 처음 ~ 끝
# 2. [start:]         : start오프셋부터 끝까지
# 3. [:end]           : 처음부터 (end-1) 오프셋까지
# 4. [start:end]      : start오프셋부터 (end-1) 오프셋까지
# 5. [start:end:step] : step만큼 문자를 건너뛰면서, start오프셋부터 (end-1)오프셋까지 추출

# >>> letter[:]
# 'abcdefghijklmnopqrstuvwxyz'
# >>> letter[0:]
# 'abcdefghijklmnopqrstuvwxyz'
# >>> letter[1:]
# 'bcdefghijklmnopqrstuvwxyz'
# >>> letter[12:15]
# 'mno'
# >>> letter[-3]
# 'x'
# >>> letter[-3:]
# 'xyz'
# >>> letter[::7]
# 'ahov'
# >>> letter[4:20:3]
# 'ehknqt'
# >>> letter[-1::-1]
# 'zyxwvutsrqponmlkjihgfedcba'

# 문자열 길이 
# >>> len(letter)
# 26

