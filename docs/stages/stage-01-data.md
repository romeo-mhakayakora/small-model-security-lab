# Stage 1: Data (3-5 days)

## Goal
A clean, versioned, byte-reproducible dataset.

## Read first
- PrimeVul paper (splits and paired structure)
- DiverseVul paper (skim data collection and label quality)
- Data-quality papers listed in the [reading list](../reading-list.md)

## Record format
```json
{"id": "primevul_000123",
 "code": "<function source>",
 "target": "{\"vulnerable\": true, \"cwe\": \"CWE-787\"}",
 "meta": {"source": "primevul", "project": "...", "pair_id": "...", "split": "test"}}
```
`target` is a **JSON string** so Inspect AI and the local runner can both read it. The prompt is built at evaluation time from `configs/evaluation/prompt_v1.txt`.

## Steps
1. Download PrimeVul. Note its license and split design.
2. Write `src/data_pipeline/prepare_data.py` to convert records into the format above.
3. Filter to 3-5 CWEs (for example out-of-bounds write, use-after-free, null dereference). Cap length (under 512 tokens, counted with the model tokenizer).
4. Deduplicate: hash normalized code (strip whitespace and comments).
5. Check train/test overlap and remove or flag it. Keep vulnerable/patched **pairs** in the same split.
6. Balance the test set about 50/50.
7. Save `data/processed/<name>_v1_<split>.jsonl`, compute SHA-256, write `data/manifests/<name>_v1.json`:

```json
{"name": "primevul_v1_test", "sha256": "<hash>", "source": "https://github.com/DLVulDet/PrimeVul",
 "license": "<check repo>", "filters": {"cwes": ["CWE-787","CWE-416","CWE-476"], "max_tokens": 512},
 "n_examples": 200, "balance": {"vulnerable": 100, "safe": 100}, "created": "YYYY-MM-DD"}
```
8. Hand-check 30 random examples. Write a note: how many labels look wrong, which CWEs look least reliable.

## Done when
- Re-running the script produces a byte-identical file with the same hash.
- You have a written note on label quality.

## Pitfalls
- Labels from "security-related commit" do not guarantee each changed function is vulnerable.
- Near-duplicate functions across splits inflate scores.
- Do not combine all public datasets. Start with one.

**Next:** [Stage 2](stage-02-evaluation-harness.md)
