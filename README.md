# internal_transaction_parser
Transaction Parser is a Python command-line tool that allows you to parse all internal transactions for a list of addresses on the Ethereum mainnet. This tool uses the Etherscan API to retrieve transaction data, and it requires an API key to run.

Installation
Clone this repository to your local machine.

Install the required dependencies by running pip install -r requirements.txt.

Usage
To run the Transaction Parser tool, navigate to the directory where the tool is located and run the following command:


python transaction_parser.py

You will be prompted to enter the name of the file containing the addresses to investigate. If you do not specify a file name, the tool will default to addresses.txt. The file should contain one Ethereum address per line.

You will also be prompted to enter your Etherscan API key. If you do not have an API key, you can obtain one from the Etherscan website.

Once you have entered the required information, the tool will retrieve transaction data for each address in the file and print out information about each transaction, including the recipient address, the amount of ETH transferred, and the method ID and function name (if available). The tool will also calculate the total value received by all addresses.

Credits 
5m477

follow me on twitter on
twitter.com/5m477
