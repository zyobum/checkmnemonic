# Cryptocurrency Address Generator

This Python script processes a list of mnemonic phrases from a file and generates the corresponding first Bitcoin and Ethereum addresses. It supports both legacy Bitcoin addresses (starting with '1') and SegWit addresses (starting with '3').

## Features

- Validates mnemonic phrases for correctness.
- Generates the first Ethereum address for a valid mnemonic.
- Generates the first legacy Bitcoin address (P2PKH) for a valid mnemonic.
- Generates the first SegWit Bitcoin address (P2SH-P2WPKH) for a valid mnemonic.

## Prerequisites

Before running this script, ensure you have Python installed on your system and the following Python packages:

- `mnemonic`: For handling mnemonic phrases.
- `eth-account` and `web3`: For Ethereum address generation.
- `bip32utils` or an alternative like `bip32`: For Bitcoin address generation.

You can install all required packages using:

```bash
pip install -r requirements.txt
