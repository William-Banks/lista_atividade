# Declaração de variavel
fahrenheit = input('me fale quanto esta a temperatura em fahrenheit: ')
fahrenheit = int(fahrenheit)
# Declaração da formula
celcius = (fahrenheit - 32) * 5/9
# Impressão da temperatura convertida
print(f'sua temperatura em celcius é:{celcius:.2f}')