# -*- coding: utf-8 -*-
# @Author: Cissoko420
# @Date:   2024-03-14 23:17:31
# @Last Modified by:   Cissoko420
# @Last Modified time: 2024-07-17 19:13:04

import requests
from solders.account import Account
from solana.rpc.api import Client
from solders.transaction import Transaction
from solders.system_program import transfer
from solana.rpc.types import TxOpts
from solana.rpc.commitment import Finalized

solana_rpc_url = "https://api.mainnet-beta.solana.com"
solana_client = Client(solana_rpc_url)

raydium_api_url = "https://api.raydium.io/v2/main/pairs"
raydium_headers = {"Content-Type": "application/json"}

def get_market_id(base_mint_address):
    pairs_url = "https://api.raydium.io/v2/main/pairs"
    market_id = None
    
    page = 1
    while True:
        params = {"page": page}
        response = requests.get(pairs_url, params=params)
        pairs_data = response.json()
        
        if not pairs_data:
            break
        
        for pair in pairs_data:
            if pair['baseMint'] == base_mint_address:
                market_id = pair['market']
                break
        
        if market_id:
            break
        
        page += 1

    return market_id

def buy_token(account, market_id, amount):
    # Construct transaction
    print("Trying to buy...\n")

    dest_pubkey = "WALLET_ADDRESS"  # CHANGE THIS ADDRESS TO THE WALLET YOU WANT THE TOKENS TO GO TO

    tx = Transaction().add(
        transfer(
            Account(account),  
            market_id,         
            int(amount * 10**9),
            dest_pubkey
        )
    )

    tx.sign([account])

    tx_hash = solana_client.send_transaction(tx, opts=TxOpts(skip_confirmation=True, preflight_commitment=Finalized))
    return tx_hash

def main():
    address = input("Enter the address: ")
    amount = float(input("Enter the amount of Solana to buy: "))

    token_a = address
    token_b = "So11111111111111111111111111111111111111112"

    market_id = get_market_id(token_a)

    if market_id:

        account = "<WALLET_PRIVATE_KEY>"                    # REPLACE PRIVATE KEY
        
        tx_hash = buy_token(account, market_id, amount)

        print("Transaction hash:", tx_hash)
    else:
        print("Market not found for the given tokens.")

if __name__ == "__main__":
    main()

