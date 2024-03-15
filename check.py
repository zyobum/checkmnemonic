import sys
from mnemonic import Mnemonic
from eth_account import Account
from web3 import Web3
import bip32utils

Account.enable_unaudited_hdwallet_features()

def generate_ethereum_address(mnemonic_str):
    if Mnemonic("english").check(mnemonic_str):
        w3 = Web3()
        account = w3.eth.account.from_mnemonic(mnemonic_str, account_path="m/44'/60'/0'/0/0")
        return account.address
    return None

def generate_bitcoin_addresses(mnemonic_str):
    if Mnemonic("english").check(mnemonic_str):
        seed = Mnemonic.to_seed(mnemonic_str)
        # Generate standard Bitcoin address (P2PKH)
        bip32_root_key_obj = bip32utils.BIP32Key.fromEntropy(seed)
        bip32_child_key_obj = bip32_root_key_obj.ChildKey(
            44 + bip32utils.BIP32_HARDEN
        ).ChildKey(
            0 + bip32utils.BIP32_HARDEN
        ).ChildKey(
            0 + bip32utils.BIP32_HARDEN
        ).ChildKey(0).ChildKey(0)
        
        btc_address = bip32_child_key_obj.Address()
        segwit_address = bip32_child_key_obj.P2WPKHoP2SHAddress()

        return btc_address, segwit_address
    return None, None

def main(filename):
    try:
        with open(filename, 'r') as file:
            mnemonics = file.readlines()

        for mnemonic_str in mnemonics:
            mnemonic_str = mnemonic_str.strip()
            eth_address = generate_ethereum_address(mnemonic_str)
            btc_address, segwit_address = generate_bitcoin_addresses(mnemonic_str)
            
            if eth_address and btc_address and segwit_address:
                print(f"Valid mnemonic: {mnemonic_str}")
                print(f"  First Ethereum address: {eth_address}")
                print(f"  First Bitcoin address: {btc_address}")
                print(f"  First Bitcoin SegWit address: {segwit_address}")
            else:
                print(f"Invalid mnemonic: {mnemonic_str}")


    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <filename>")
    else:
        filename = sys.argv[1]
        main(filename)

