# ''' ~ '''을 사용하면 아래와 같이 긴 문자열을 입력할수 있다. 
# 해당 변수의 개행을 인터프리터는 \n으로 바꿔 출력하지만, print() 함수를 사용하면 공백을 모두 유지한채 출력하는걸 확인할 수 있다.

# >>> poem = '''There was a Young Lady of Norway,
#               Who casually sat in a doorway;
#               When the door squeezed her flat,
#               She exclaimed, "What of that?"
#               This courageous Young Lady of Norway.'''
# >>> poem
# 'There was a Young Lady of Norway,\n              Who casually sat in a doorway;\n              When the door squeezed her flat,\n              She exclaimed, "What of that?"\n              This courageous Young Lady of Norway.'
# >>> print(poem)
# There was a Young Lady of Norway,
#               Who casually sat in a doorway;
#               When the door squeezed her flat,
#               She exclaimed, "What of that?"
#               This courageous Young Lady of Norway.