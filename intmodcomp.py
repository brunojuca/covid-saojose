# Importando os pacotes
from numpy import *
from matplotlib.pylab import *

# Definindo o numero de pontos
n = 120
print(n)

# Inicializando e calculando o vetor
x = range( n )
a = zeros( n )
a[ 0 ] = 1000
for i in x[ 1 : n ]:
  a[ i ] = 1.01 * a[ i-1]

print(x) 
print(a)

a[ 0 :: 6 ]

# Criação do gráfico tomando os valores de 6 em 6 meses
plot(x[ 0 :: 6 ] , a [ 0 :: 6 ] , 'o' , label= 'Saldo')
legend()

# Comandos opcionais para a formatação do gráfico
plot(x[ 0 :: 6 ] , a [ 0 :: 6 ] , 'o' , label= 'Saldo')
xlim( 0 , 150 )
ylim( 0 , 4000)
grid( )
legend( loc='best')
xlabel( 'Tempo ( meses )' )
ylabel( 'Reais' )

#Exibição do gráfico
show ( )
