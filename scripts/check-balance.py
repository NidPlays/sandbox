from algosdk.v2client import algod

# Connecting to the Algod Client on the Algorand sandbox
algod_address = "http://localhost:4001"
algod_token = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
algod_client = algod.AlgodClient(algod_token, algod_address)

# Declare your Address
my_address = "O2GOUK3YGXVVQACZCL4AV5OH72ZU52JM3XYFBLA56ZK3AZ544KCDG5ATZQ"
my_address2 = "ZUWMCE3JD5JE5Y6PPYW72WARIT4ABJDX3FIUCVYWRR3X22Y3JXUAZH6Y24"

account_info = algod_client.account_info(my_address)
print("Account balance1: {} microAlgos".format(account_info.get('amount')))

account_info2 = algod_client.account_info(my_address2)
#print(account_info)
print("Account balance2: {} microAlgos".format(account_info2.get('amount')))