from brownie import accounts, TechLab1Token
from dotenv import load_dotenv
import os

def main():
    load_dotenv()  # loads .env file

    # Add your deployer account from private key
    acct = accounts.add(os.getenv("PRIVATE_KEY"))

    # Get latest deployed token
    token = TechLab1Token[-1]

    # Recipient address (the one you want to receive the tokens)
    recipient = "0x5c2fdea369f2bc1202f3bde13b2745b9b83dd0ae"

    # Amount to send (example: 100 tokens)
    amount = 100 * 10**18  # adjust number of tokens if needed

    # Send the tokens
    tx = token.transfer(recipient, amount, {"from": acct})
    tx.wait(1)  # wait for confirmation
    print("Tokens sent! Tx:", tx.txid)
