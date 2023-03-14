import requests, os 
import colorama
import pyfiglet

colorama.init()

def get_input(prompt, default=None):
    if default:
        prompt += f" (default: {default})"
    prompt += ": "
    result = input(prompt)
    if not result:
        result = default
    return result

def get_addresses_from_file(filename):
    with open(filename) as f:
        return [line.strip() for line in f]

def main():
    print(pyfiglet.figlet_format("Transaction Parser"))
    print("This program will parse all internal transactions for a list of addresses on the Ethereum mainnet.")

    filename = get_input("Enter the name of the file containing the addresses to investigate", "addresses.txt")
    addresses = get_addresses_from_file(filename)

    api_key = get_input("Enter your Etherscan API key")

    total_value_received = 0 

    for target_address in addresses:
        value_in_address = 0

        etherscan_params = (
            ('module', 'account'),
            ('action', 'txlistinternal'),
            ('address', target_address),
            ('sort', 'asc'),
            ('apikey', api_key)
        )

        response = requests.get("https://api.etherscan.io/api", params=etherscan_params)
        data = response.json().get("result")

        for transaction in data:
            current_value = int(transaction.get("value"))/10**18
            print(f'Sending TO: {transaction.get("to")}')
            print(f'    - Amount: {current_value}')
            print(f'MethodID:{transaction.get("methodId")} == {transaction.get("functionName")}')
            total_value_received += current_value
            value_in_address += current_value

        print(f'{colorama.Fore.WHITE}Value in: {colorama.Fore.RED}{target_address} is {colorama.Fore.GREEN}{value_in_address}')

    print(f'{colorama.Fore.YELLOW} Total Contract Value Received:{colorama.Fore.GREEN}{total_value_received}')

if __name__ == "__main__":
    main()
