# Conversor de Temperatura - Celsius para Fahrenheit e Kelvin

celsius = float(input("Digite a temperatura em °C: "))
fahrenheit = (celsius * 9/5) + 32
kelvin = celsius + 273.15

print(f"{celsius}°C é igual a {fahrenheit:.2f}°F e {kelvin:.2f}K")
