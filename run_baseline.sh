#!/usr/bin/env bash
# One command for the Stage 3 baseline. Edit DATA/MODEL/OUT, then: bash run_baseline.sh
set -euo pipefail
DATA=${DATA:-data/processed/primevul_v1_test.jsonl}
MODEL=${MODEL:-Qwen/Qwen2.5-Coder-1.5B-Instruct}
OUT=${OUT:-reports/baseline_v1}
mkdir -p "$OUT"
python -m src.evaluation.run_local --data "$DATA" --model "$MODEL" --load-4bit \
  --out "$OUT/results.jsonl"
python -m src.evaluation.metrics --results "$OUT/results.jsonl" --out "$OUT/summary.json" \
  | tee "$OUT/summary.txt"
