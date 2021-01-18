# strip() : ()안의 인수 제거

# >>> world = " earth "
# >>> world.strip()      
# 'earth'
# >>> world.strip(' ')
# 'earth'
# >>> world.lstrip()
# 'earth '
# >>> world.rstrip()
# ' earth'
# >>> world.strip('!')
# ' earth '

# >>> blurt = "What the...!!?"
# >>> blurt.strip('.?!') <--- . & ? & ! 모두 제거
# 'What the'