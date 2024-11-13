import re

def detect_solana_token_address(message):
    # Solana addresses are Base58 encoded strings, typically 32-44 chars long
    pattern = r'[1-9A-HJ-NP-Za-km-z]{32,44}'
    
    # Find all matches in the message
    matches = re.findall(pattern, message)
    
    # Filter out matches that are definitely not Solana addresses
    # (optional: you can add more validation if needed)
    return [match for match in matches if len(match) >= 32 and len(match) <= 44]
