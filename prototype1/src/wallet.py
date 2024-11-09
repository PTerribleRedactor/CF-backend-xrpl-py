import os
from xrpl.wallet import Wallet

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

# Get wallet seeds from environment variables
WALLET_1_SEED = os.getenv('WALLET_1_SEED', '')
WALLET_2_SEED = os.getenv('WALLET_2_SEED', '')

# Create wallets from seeds
Wallet_1 = Wallet.from_seed(WALLET_1_SEED)
Wallet_2 = Wallet.from_seed(WALLET_2_SEED)