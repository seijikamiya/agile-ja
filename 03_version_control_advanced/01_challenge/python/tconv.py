def convert_celsius_to_fahrenheit():
    print("Enter the temperature in Celsius:")
    celsius = input()
    celsius = int(celsius)
    fahrenheit = (celsius * 9/5) + 32
    print(f"The Celsius temperature {celsius} you entered is {fahrenheit} in Fahrenheit.")


def convert_fahrenheit_to_celsius():
    print("Enter the temperature in Fahrenheit:")
    fahrenheit = input()
    fahrenheit = float(fahrenheit)
    celsius = 5/9 * (fahrenheit - 32)
    print(f"The Celsius temperature {fahrenheit} you entered is {celsius} in Fahrenheit.")

def main():
    print("Enter c if you want to convert from Fahrenheit to Celsius")
    print("Enter f if you want to convert from Celsius to Fahrenheit")
    user_input = input()
    if user_input == "c":
        convert_fahrenheit_to_celsius()
    elif user_input == "f":
        convert_celsius_to_fahrenheit()
    else:
        print("Incorrect input. Please try again later")