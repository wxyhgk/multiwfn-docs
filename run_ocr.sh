#!/bin/bash
# 跑指定的 split 文件(传文件名), 每个最多重试3次
cd "/Users/wxyhgk/Documents/Quamtum_Chemistry_md/Multiwfn"
for f in "$@"; do
  base=$(basename "$f" .pdf)
  out="ocr_out/${base}.json"
  if [ -f "$out" ]; then echo "$base 已存在, 跳过"; continue; fi
  for try in 1 2 3; do
    echo "=== $base 尝试 $try ==="
    if paddleocr api --model_type doc_parsing --file_path "./splits/$f" \
      --output "$out" --use_doc_unwarping False \
      --use_doc_orientation_classify False 2>&1 | tail -2; then
      [ -f "$out" ] && break
    fi
    sleep 10
  done
done
echo "ALL DONE"
