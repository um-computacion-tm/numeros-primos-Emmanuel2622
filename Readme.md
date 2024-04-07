# README

## Autor

Carlos Emmanuel Denis

## Descripción

Este script de Python define una función `is_primo(value)` que determina si un número dado es primo o no. Un número primo es aquel que solo es divisible por 1 y por sí mismo, teniendo exactamente dos divisores distintos. Por definición, el 1 no se considera un número primo.

## Cómo Funciona

La función `is_primo(value)` recibe como argumento un entero (`value`). Retorna `True` si el número es primo y `False` en caso contrario.

El algoritmo funciona de la siguiente manera:

1. Se inicializa una variable `div` en 2, que se utilizará para dividir el número de entrada `value`.
2. Si `value` es igual a 1, la función retorna `False` directamente, ya que 1 no es un número primo.
3. Se entra en un bucle `while` que se ejecuta mientras `div` sea menor que `value`.
   - Dentro del bucle, si `value` es divisible por `div` (es decir, `value % div == 0`), se retorna `False`, ya que se ha encontrado un divisor diferente de 1 y `value`, indicando que no es primo.
   - Si `value` no es divisible por `div`, se incrementa `div` en 1 y se continúa con la siguiente iteración del bucle.
4. Si el bucle termina sin retornar `False`, significa que no se encontraron divisores distintos de 1 y `value`, por lo que el número es primo y la función retorna `True`.

## Uso
Aquí hay un ejemplo de cómo usar la función `is_primo`:

```python
numero = 11
if is_primo(numero):
	print(f"{numero} es un número primo.")
else:
	print(f"{numero} no es un número primo.")
```

>Este código verificará si el numero 11 es primo y, como resultado, imprimirá que 11 es un número primo.
requisitos

## Requisitos
	Python 3.11.2
