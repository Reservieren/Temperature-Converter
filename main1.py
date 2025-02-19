def CelsiusToFahrenheit(celsius):
    return celsius * 1.8 + 32

def FahrenheitToCelsius(fahrenheit):
    return (fahrenheit - 32) / 1.8

while True:

    print('TEMPERATURE CONVERTER. ')
    print('1. CELSIUS > FAHRENHEIT')
    print('2 FAHRENHEIT > CELSIUS')

    escolha = input('Choose conversion (1 or 2)')

    if escolha == '1':
        celsius = float(input('Enter temperature in Celsius: '))
        fahrenheit = CelsiusToFahrenheit(celsius)
        print(f'{celsius} degrees Celsius is equal to {fahrenheit:.2f} degrees Fahrenheit. ')

    elif escolha == '2':
        fahrenheit = float(input('Enter temperature in Fahrenheit: '))
        celsius = FahrenheitToCelsius(fahrenheit)
        print(f'{fahrenheit} degrees Fahrenheit is equal to {celsius:.2f} degrees Celsius. ')
    else:
        print('Invalid input. ')

    escolha = input('Do you want to perform another conversion? (y/n): ')
    if escolha.lower() != 'y':
        break