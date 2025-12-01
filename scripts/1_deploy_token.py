from brownie import TechLab1Token, accounts, config
from web3 import Web3

# Initial supply in Wei
initial_supply = Web3.to_wei(1000, "ether")  # <-- fixed

def main():
    # Load account from .env
    account = accounts.add(config["wallets"]["from_key"])
    print(f"Deploying from: {account}")

    # Deploy the token
    token = TechLab1Token.deploy(
        initial_supply,
        {"from": account},
        publish_source=True  # automatically verify on Etherscan if ETHERSCAN_TOKEN is in .env
    )

    print(f"Deployed TechLab1Token at address: {token.address}")
