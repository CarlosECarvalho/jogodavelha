qtdvitoriasX = 0
qtdvitoriasO = 0
qtdempates = 0
tab = ['1', '2','3','4','5','6','7','8','9']

print('_' + tab[0] +'_|_' + tab[1] +'_|_' +tab[2] +'_')
print('_' + tab[3] +'_|_' + tab[4] +'_|_' +tab[5] +'_')
print('_' + tab[6] +'_|_' + tab[7] +'_|_' +tab[8] +'_')

jogadoratual = 'X'
pos = int(input('Informe a linha e coluna que deseja marcar.'))
#primeira linha
if pos == '1' and tab[0] == '1' :
    tab[0] = jogadoratual
elif pos == '2' and tab[1] == '2' :
    tab[1] = jogadoratual
elif pos == '3' and tab[2] == '3' :
    tab[2] = jogadoratual
#segunda linha
elif pos == '4' and tab[3] == '4' :
    tab[3] = jogadoratual
elif pos == '5' and tab[4] == '5' :
    tab[4] = jogadoratual
elif pos == '6' and tab[5] == '6' :
    tab[5] = jogadoratual
#terceira linha
elif pos == '7' and tab[6] == '7' :
    tab[6] = jogadoratual
elif pos == '8' and tab[7] == '8' :
    tab[7] = jogadoratual
elif pos == '9' and tab[8] == '9' :
    tab[8] = jogadoratual
elif (pos < 1) or (pos > 9):
    print('Posição inválida, informe novamente.')