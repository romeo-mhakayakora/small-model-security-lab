# Juliet Extraction

The Juliet suite (NIST SARD) is clean and synthetic, good for a sanity check. It is **not** plug-and-play.

## Why it needs work

- Test cases spread across many files with shared helper code.
- Good and bad versions are distinguished by function names (for example `..._bad`, `..._good...`).
- Flow variants add control-flow noise.
- Directory names encode the CWE.

## Plan

1. Download the C/C++ suite; note version and license.
2. Pick **one CWE directory** for the smoke test.
3. Write `src/data_pipeline/extract_juliet.py` to:
   - walk `.c`/`.cpp` files;
   - extract `_bad` functions (vulnerable) and matching `good` functions (safe);
   - read the CWE from the directory name;
   - strip comments that reveal the answer (such as FLAW/FIX markers);
   - rename functions to neutral names so the label is not visible.
4. Cap length with the model's tokenizer.
5. Balance 50/50. **Split by test-case family** so near-identical variants never land on both sides.
6. Hash the output and write a manifest.

## Leakage checks

- Search final code for `bad`, `good`, `FLAW`, `FIX`, `CWE`. None should remain.
- Variants of one base case stay in one split.

## Done when

Re-running gives a byte-identical file, no label-revealing strings remain, and you hand-checked 20 examples.
