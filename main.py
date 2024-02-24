def main():
    
    celsius = int(input('The temperature in celsius is ')) 
    fahrenheit = (9/5) * celsius + 32

    print(f'The temperature in fahrenheit is \t{fahrenheit: .2f}')
    
    return celsius, fahrenheit


if __name__ == '__main__':
    main()
