import json
from merkle import merkle_root

BANNER = "🧩 ZK-Notes Merkle Root (demo) — PR-friendly project"

def main():
    with open("notes.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    leaves = data.get("leaves", [])
    expected = data.get("expected_root", "")

    root = merkle_root(leaves)
    root_hex = "0x" + root.hex()

    print(BANNER)
    print("Leaves:", len(leaves))
    print("Root:  ", root_hex)

    if expected:
        print("Expected:", expected)
        print("Match:   ", "YES ✅" if expected.lower() == root_hex.lower() else "NO ❌")

if __name__ == "__main__":
    main()
