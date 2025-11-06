import json
from merkle import merkle_root
from utils.display import print_banner, print_comparison
from utils.fileio import load_json
from utils.logger import log_info, log_error
from version import VERSION
from changelog import print_latest_changes

def main():
    print_banner(f"🧩 ZK-Notes Merkle Root (demo) v{VERSION}")
    log_info("Starting Merkle computation")

    data = load_json("notes.json")
    leaves = data.get("leaves", [])
    expected = data.get("expected_root", "")

    root = merkle_root(leaves)
    root_hex = "0x" + root.hex()

    print("Leaves count:", len(leaves))
    print_comparison(root_hex, expected)

    if expected.lower() != root_hex.lower():
        log_error("Root mismatch detected")
    else:
        log_info("Root verification passed")

    print_latest_changes()

if __name__ == "__main__":
    main()
