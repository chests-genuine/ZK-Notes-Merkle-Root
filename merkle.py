# TODO: Implement `merkle_root` so tests pass (make a Pull Request with your fix).
# Rules for this demo:
# - Each leaf is a hex string like "0x...." (32 bytes). First hash each leaf with sha3_256.
# - Build the Merkle tree by pairing nodes left-to-right; if odd count, duplicate the last node.
# - Parent = sha3_256(left || right)
# - Return the final root as raw bytes (not hex).
from utils.hash import sha3_256_bytes

def merkle_root(leaves_hex: list[str]) -> bytes:
    # TODO: replace this stub with a working implementation.
    # Intentionally wrong so tests fail until you fix it.
    return b""
