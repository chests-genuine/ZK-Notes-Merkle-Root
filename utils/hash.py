# Simple hashing helpers (sha3_256, not Keccak-256) to avoid extra dependencies.
# In real EVM contexts you would use Keccak-256, but for this demo SHA3-256 keeps it lightweight.
import hashlib

def sha3_256_bytes(data: bytes) -> bytes:
    return hashlib.sha3_256(data).digest()

def sha3_256_hex_from_hexstr(hexstr: str) -> bytes:
    if hexstr.startswith("0x") or hexstr.startswith("0X"):
        hexstr = hexstr[2:]
    raw = bytes.fromhex(hexstr)
    return sha3_256_bytes(raw)
