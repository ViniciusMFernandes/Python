r1 = float(input('Digite 1ª Reta: '))
r2 = float(input('Digite 2ª Reta: '))
r3 = float(input('Digite 3ª Reta: '))
if (r1 + r2) > r2 and (r2 + r3) > r1 and (r1 + r2) > r3:
        print('1ª Reta: {:.1f}\n2ª Reta {:.1f}\n3ª Reta {:.1f}'.format(r1, r2, r3))
        print('As retas digitadas conseguem formar um triângulo!')
else:
        print('1ª Reta: {:.1f}\n2ª Reta {:.1f}\n3ª Reta {:.1f}'.format(r1, r2, r3))
        print('As retas digitadas não conseguem formar um triângulo!')

