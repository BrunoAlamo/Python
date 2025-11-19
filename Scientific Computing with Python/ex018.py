import math

a = float(input('digite um angulo: '))
s = math.sin(math.radians(a))
c = math.cos(math.radians(a))
t = math.tan(math.radians(a))
print('o seno é {}, o cosseno é {} e a tangente é {}'.format(s, c, t))