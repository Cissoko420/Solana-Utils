import requests
import json
import time

def get_sender_address(transaction_signature):
    url = "https://api.mainnet-beta.solana.com"
    headers = {"Content-Type": "application/json"}

    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "getConfirmedTransaction",
        "params": [transaction_signature, {"commitment": "confirmed"}],
    }
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    transaction_data = response.json().get("result")

    if transaction_data:
        post_token_balances = transaction_data.get("meta", {}).get("postTokenBalances", [])
        for balance in post_token_balances:
            if balance.get("accountIndex") == 2:
                return balance.get("owner")

    return None

def process_transaction_signatures(input_file_path, output_file_path):
    print("Processing transaction signatures...")
    with open(input_file_path, 'r') as input_file:
        transaction_signatures = [line.strip() for line in input_file.readlines()]

    unique_sender_addresses = set()
    for signature in transaction_signatures:
        sender_address = get_sender_address(signature)
        if sender_address:
            unique_sender_addresses.add(sender_address)
            print(f"Address found: {sender_address}")
        else:
            print(f"No address found for signature: {signature}")

        time.sleep(1)

    print("Writing unique sender addresses to a file...")

    with open(output_file_path, 'w') as output_file:
        output_file.write("\n".join(unique_sender_addresses))

    print("Process completed.")

input_file_path = 'out.txt'  # Replace with the actual path to your transaction signatures file
output_file_path = 'sender_addresses.txt'  # Replace with the desired output file path

process_transaction_signatures(input_file_path, output_file_path)
