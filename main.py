import requests

def get_crypto_info(crypto_identifier):
    url = 'https://api.coingecko.com/api/v3/coins/markets'
    vs_currencies = 'usd'

    params = {'vs_currency': vs_currencies, 'ids': crypto_identifier}

    try:
        response = requests.get(url, params=params)
        data = response.json()

        if data:
            crypto_info = data[0]
            crypto_price = crypto_info['current_price']

            print(f"💰 The current price of {crypto_info['name']} ({crypto_info['symbol'].upper()}) is ${crypto_price}")

            # Fetch and display categories
            crypto_id = crypto_info['id']
            get_crypto_categories(crypto_id)
        else:
            print(f"❌ No information found for {crypto_identifier}.")

    except requests.RequestException as e:
        print(f"❌ Error fetching data for {crypto_identifier}: {e}")

def get_crypto_categories(crypto_id):
    categories_url = f'https://api.coingecko.com/api/v3/coins/{crypto_id}'
    try:
        response = requests.get(categories_url)
        data = response.json()

        if 'categories' in data:
            categories = data['categories']
            print(f"📚 Categories for {crypto_id}: {categories}")
        else:
            print(f"❌ No categories found for {crypto_id}.")

    except requests.RequestException as e:
        print(f"❌ Error fetching categories: {e}")

def display_help():
    print("\n🌐 Cryptocurrency Information Tool:")
    print("1. Enter the symbol or name of the cryptocurrency to get its current price and categories.")
    print("2. Examples of valid inputs:")
    print("   - 'bitcoin'")
    print("   - 'Ethereum'")
    print("   - 'Tether'")
    print("   - 'cardano'")
    print("   - 'Solana'")
    print("   If you need help with the correct name format, visit: 🚀 https://www.coingecko.com")
    print("   For more comprehensive cryptocurrency information, visit: 🌐 https://www.coingecko.com")
    print("3. Type 'help' to display this help message.")
    print("4. Type 'exit', 'bye', or 'cancel' to end the program. 👋\n")

if __name__ == "__main__":
    display_help()

    while True:
        crypto_identifier_to_search = input("Enter the symbol or name of the cryptocurrency: ").lower()

        if crypto_identifier_to_search == 'help':
            display_help()
        elif crypto_identifier_to_search in ['exit', 'bye', 'cancel']:
            print("Exiting the program. 👋")
            break
        else:
            get_crypto_info(crypto_identifier_to_search)
