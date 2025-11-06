# These tests intentionally fail until you implement merkle_root in merkle.py.
import json
from merkle import merkle_root

def test_merkle_root_matches_expected_fixture():
    with open("notes.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    leaves = data["leaves"]
    expected_root_hex = data["expected_root"].lower()
    root_hex = "0x" + merkle_root(leaves).hex()
    assert root_hex.lower() == expected_root_hex

def test_merkle_root_is_32_bytes():
    with open("notes.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    root = merkle_root(data["leaves"])
    assert isinstance(root, (bytes, bytearray))
    assert len(root) == 32
