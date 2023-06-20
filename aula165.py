from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

data_emprestimo = datetime(2020, 12, 20)
print(data_emprestimo)
delta5 = relativedelta(years=5)
datafinal = data_emprestimo + delta5
print(type(datafinal))
print(data_emprestimo.month)
#data_emprestimo.month += 1
print(relativedelta(data_emprestimo, months=1)) 
print(data_emprestimo + relativedelta(data_emprestimo, months=1))

total = 1000000
data_parcela = data_emprestimo
data_parcelas = []
#valor_parcela = total/ len(data_parcelas)
while data_parcela < datafinal:
    data_parcelas.append(data_parcela)
    data_parcela += relativedelta(months=1)
    

valor_parcela = total/ len(data_parcelas)
for data in data_parcelas:
    print(data.strftime('%d/%m/%Y'), f'R$ {valor_parcela:,.2f}')

print()
print(
    f'Você pegou R$ {total:,.2f} para pagar '
    f'em {delta5.years} anos '
    f'({len(data_parcelas)} meses) em parcelas de '
    f'R$ {valor_parcela:,.2f}.'
)




#print(datetime(data_emprestimo+data_emprestimo.month))
#listadatas = [a + relativedelta(a, months=1) for a in range(data_emprestimo.year, datafinal.year)]
#print([a for a in range(data_emprestimo.year, datafinal.year)])
#for a in range(data_emprestimo.year, datafinal.year):
    #print(a)
    #for a in range(0,5):
 #   print(data_emprestimo)
  #  data_emprestimo+= relativedelta(data_emprestimo, years=1)

    


#print(relativedelta(data_emprestimo, datafinal))

