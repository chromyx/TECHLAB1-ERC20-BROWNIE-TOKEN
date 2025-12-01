Here is a suggested GitHub repository description that explains the deployment and interaction with the TechLab1 Token (TL1) on the Sepolia testnet, incorporating the details from your images.



🚀 TechLab1 Token (TL1) - ERC-20 Deployment on Sepolia
This repository documents the successful deployment and initial transfer of the custom TechLab1 Token (TL1) on the Sepolia Testnet. TL1 is an ERC-20 standard compliant token built using Solidity and the OpenZeppelin library.

🛠️ Deployment Details
The TL1 token was deployed with a maximum total supply of 1,000 TL1. The contract details are verifiable on Etherscan.
https://sepolia.etherscan.io/token/0x22809DEa0810420289F323dA144f81141185B5eA#code
<img width="1178" height="903" alt="555" src="https://github.com/user-attachments/assets/83efa2cf-e48e-4a53-8794-f7266fdebd1b" />

Contract Overview:
Token Name: TechLab1 Token

Token Symbol: TL1

Total Supply: 1,000 TL1

Decimals: 18

Contract Address: 0x228909EA0E0810420289F323A144f9D1141185B5eA (as seen in the Etherscan data)

🏗️ Initial Token Distribution
The initial step involved deploying the contract and minting the entire supply of 1,000 TL1 to the contract creator's address.
<img width="399" height="82" alt="444" src="https://github.com/user-attachments/assets/51771c31-24d6-4e15-95e2-ba0bdf7a9541" />

The image above confirms the initial transaction where the full 1,000 TL1 supply was minted and sent from the 0x000...000 (zero address) to the initial holder's address (0x196C...5B3c).

📤 Token Transfer Demonstration
Following the successful deployment, a script was run to demonstrate the core ERC-20 functionality: transferring tokens from the initial holder to a separate recipient address.
<img width="844" height="155" alt="111" src="https://github.com/user-attachments/assets/9fbafaa8-8817-4ae6-8c9c-71f277170341" />

1. Script Execution
The above console output confirms the successful execution of the token transfer script, including gas details and the resulting transaction hash.
<img width="1196" height="888" alt="222" src="https://github.com/user-attachments/assets/94293a1c-4e73-4100-afdb-8fcdd172ab89" />

Transaction Hash (Tx): 0x5d8b474c2a2756a20d2aa1bf06a2d9079579abbe48657d344a0d4f1c588bc3d

Gas Used: 51,632 (90.22% of the limit)

Gas Price: 0.001800011 gwei

2. Etherscan Verification
The transfer transaction was immediately verified on the Sepolia Testnet Etherscan.

This Etherscan record verifies a transfer of 100 TL1 from the sender (0x196C...5B3c) to the recipient (0x5c2f...0dAE). It also shows the Gas Fees paid in ETH, confirming the on-chain cost of the operation.
<img width="1204" height="644" alt="333" src="https://github.com/user-attachments/assets/a7303bcc-63fe-422c-a77c-208b0959ee4d" />

3. Recipient Wallet Balance
The final image confirms the recipient's wallet balance after the transfer, showing they now hold the transferred tokens.
<img width="1204" height="644" alt="333" src="https://github.com/user-attachments/assets/3081c14b-5362-4b28-8ed2-e150bf0b468f" />


The recipient now holds 100 TL1, confirming the successful end-to-end token transfer on the Sepolia Testnet.
