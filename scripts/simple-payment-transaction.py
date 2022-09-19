from algosdk.future import transaction
from algosdk import constants, mnemonic
from algosdk.v2client import algod
import json
import base64

# Connect to the Algod Client on the Algorand sandbox
algod_address = "http://localhost:4001"
algod_token = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
algod_client = algod.AlgodClient(algod_token, algod_address)

# Declare your address and passphrase
my_address = "O2GOUK3YGXVVQACZCL4AV5OH72ZU52JM3XYFBLA56ZK3AZ544KCDG5ATZQ"
my_passphrase = "pattern help evoke juice pigeon stumble body win erase flip junior canvas best symptom wheat upon setup strong neck want year board taste able rural"

# Derive your private key from your passphrase
private_key = mnemonic.to_private_key(my_passphrase)

def your_first_transaction(private_key, my_address):
  params = algod_client.suggested_params()
  params.flat_fee = True
  params.fee = constants.MIN_TXN_FEE
  receiver = "ZUWMCE3JD5JE5Y6PPYW72WARIT4ABJDX3FIUCVYWRR3X22Y3JXUAZH6Y24"
  note = "NidGaming's First PythonSDK Transaction"
  amount = 1000000
  unsigned_txn = transaction.PaymentTxn(my_address, params, receiver, amount, None, note)

  # sign transaction
  signed_txn = unsigned_txn.sign(private_key)
  
  # submit transaction
  txid = algod_client.send_transaction(signed_txn)
  print("Successfully sent transaction with txID: {}".format(txid))

	# wait for confirmation
  try:
    confirmed_txn = transaction.wait_for_confirmation(algod_client, txid, 4)
  except Exception as err:
    print(err)
    return

  account_info = algod_client.account_info(my_address)

  print("Transaction information: {}".format(json.dumps(confirmed_txn, indent=4)))
  print("Decoded note: {}".format(base64.b64decode(confirmed_txn["txn"]["txn"]["note"]).decode()))
  print("Starting Account balance: {} microAlgos".format(account_info.get('amount')) )
  print("Amount transferred: {} microAlgos".format(amount) )
  print("Fee: {} microAlgos".format(params.fee) )
  print("Final Account balance: {} microAlgos".format(account_info.get('amount')))

your_first_transaction(private_key, my_address)