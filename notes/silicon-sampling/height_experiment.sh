#!/usr/bin/env bash
set -euo pipefail

N=${1:-50}
OUTDIR=${2:-responses}
mkdir -p "$OUTDIR"

: > "$OUTDIR/results.csv"
echo "run,sex,age,seed,height_in" > "$OUTDIR/results.csv"

for i in $(seq 1 "$N"); do
  SEED=$(openssl rand -hex 4)
  if (( RANDOM % 2 )); then SEX=male; else SEX=female; fi
  AGE=$((RANDOM % 60 + 20))

  PROMPT="Random seed: $SEED. You are a $AGE-year-old $SEX American sampled at random from the population. What is your height in inches? Respond with only a number."

  ANSWER=$(claude -p "$PROMPT" | tr -d '[:space:]')
  echo "$i,$SEX,$AGE,$SEED,$ANSWER" >> "$OUTDIR/results.csv"
  echo "run $i: $SEX age $AGE -> $ANSWER"
done

echo "Done. Results in $OUTDIR/results.csv"
