READMEProject: ZK-Notes Merkle Root (demo)

Overview
A tiny multi-file repository that computes a Merkle root for simulated private note commitments. It is inspired by Aztec-style notes and soundness ideas from web3. The code uses SHA3-256 for simplicity (not Keccak-256) to avoid extra dependencies.

Files
- app.py — prints Merkle root for leaves from notes.json and compares with expected_root
- merkle.py — TODO implementation for merkle_root (this is your Pull Request task)
- utils/hash.py — minimal SHA3-256 helpers
- notes.json — test fixture with leaves and an expected root
- tests/test_merkle.py — failing tests until merkle_root is implemented
- requirements.txt — test dependency
- .gitignore — housekeeping

How to run (plain description, no bash)
1. Create a Python 3.10+ virtual environment.
2. Install dependencies from requirements.txt using your preferred method.
3. Run the tests with pytest; they will fail at first.
4. Implement merkle_root in merkle.py to make tests pass.
5. Run the tests again; they should pass when your implementation is correct.
6. Execute app.py to see the computed root and the expected value from notes.json.

Expected behavior
- merkle_root returns 32 bytes.
- With the provided notes.json, the computed root must match the expected_root value.

Notes
- SHA3-256 is used only to keep the project dependency-free. In real EVM tooling you would use Keccak-256 and potentially eth-hash/pysha3.
- The tree pairs nodes left-to-right; if there is an odd number of nodes at any level, the last node is duplicated before hashing parents.

