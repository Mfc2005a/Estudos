conj1 = { 'Carlos', 'Josiel', 'Candire', 'Aline',}
conj2 = {'Aline', 'Carlos', 'Jaqueline', 'ALtair',}

união = conj1.union(conj2)
diferença = conj1.symmetric_difference(conj2)
interceção = conj1.intersection(conj2)

print (f'Pessoas presentes nos dois grupos: {interceção}')
print (f'Pessoas presentes em apenas um grupo:{diferença}')
print (f'Todas as pessoas mencionadas nos Sets: {união}')