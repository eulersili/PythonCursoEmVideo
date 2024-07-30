from math import radians, sin, cos, tan
ângulo = float(input('Digite o ângulo que voc&ê deseja: '))
seno = sin(radians(ângulo))
cosseno = cos(radians(ângulo))
tangente = tan(radians(ângulo))
print('O ângulo de {} tem como SENO {:.2f}'.format(ângulo, seno))
print('O ângulo de {} tem como COSSENO {:.2f}'.format(ângulo, cosseno))
print('O ângulo de {} tem como TANGENTE {:.2f}'.format(ângulo, tangente))
