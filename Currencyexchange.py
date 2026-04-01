import datetime

#exchange rate dataset
exchange_rates = {
    "USD": 0.78,
    "THB": 24.96,
    "CNY": 5.56,
    "JPY": 114.64,
    "GBP": 0.58,
    "MYR": 3.29   
}

#sgd value dataset
sgd_values = [1,2,3,4,5,10,20,30,40,50,100,200,300,400,500,600,700,800,900,1000]

#timestamp
now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(f"\nExchange rates as of: {now}")
print("Available Currencies:", ", ".join(exchange_rates.keys()))

def show_table(currency, rate):
    print(f"\nSGD -> {currency} (Rate: {rate})")
    print("=" * 40)
    print("SGD".ljust(8) + currency.rjust(12))
    print("-" * 40)
    for amount in sgd_values:
        converted_value = amount * rate
        print(f"${amount:,.2f}".ljust(8) + f"{converted_value:,.2f}".rjust(12))

def convert_specific_amount():
    specify = input("\nEnter an SGD amount to convert or press Enter to skip: ").strip()
    if not specify:
        return
    try:
        specific_amount = float(specify)
        currency_choice = input("Enter the currency to convert to: ").strip().upper()
        if currency_choice in exchange_rates:
            rate = exchange_rates[currency_choice]
            converted = specific_amount * rate
            print(f"${specific_amount:,.2f} SGD = {converted:,.2f} {currency_choice}")
        else:
            print("Invalid currency, choose from:", ", ".join(exchange_rates.keys()))
    except ValueError:
        print("Invalid amount, please enter a number.")

#main menu
while True:
    print("\nMain Menu")
    print("1. Individual currency table")
    print("2. All currency tables")
    print("3. Convert specific SGD amount")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ").strip()
    
    if choice == "1":
        currency = input("Enter the currency to convert to: ").strip().upper()
        if currency in exchange_rates:
            show_table(currency, exchange_rates[currency])
        else:
            print("Invalid currency, choose from:", ", ".join(exchange_rates.keys()))
    elif choice == "2":
        for curr, rate in exchange_rates.items():
            show_table(curr, rate)
    elif choice == "3":
        convert_specific_amount()
    elif choice == "4":
        print("Exiting program.")
        break
    else:
        print("Invalid choice, please enter 1-4.")
