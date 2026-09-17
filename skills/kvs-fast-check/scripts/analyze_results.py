#!/usr/bin/env python3
"""Summarize DashScope load-test JSONL correctness and encoding anomalies."""

from __future__ import annotations

import argparse
import collections
import json
import statistics
from pathlib import Path


EXPECTED = {1: "1", 2: "4", 3: "9", 4: "16", 5: "25"}
MOJIBAKE_MARKERS = ("\ufffd", "锟斤拷", "Ã", "Â", "â€", "ðŸ", "\x00")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("result_file", type=Path)
    parser.add_argument("--version", choices=("simplified", "legacy"), required=True)
    return parser.parse_args()


def anomalies(text: str) -> list[str]:
    found = [repr(marker) for marker in MOJIBAKE_MARKERS if marker in text]
    if any(ord(char) < 32 and char not in "\n\r\t" for char in text):
        found.append("unexpected-control-character")
    return found


def numeric_stats(values: list[float | int]) -> dict | None:
    if not values:
        return None
    return {
        "min": min(values),
        "mean": round(statistics.mean(values), 3),
        "max": max(values),
    }


def main() -> int:
    args = parse_args()
    try:
        raw = args.result_file.read_text(encoding="utf-8", errors="strict")
    except UnicodeDecodeError as exc:
        print(json.dumps(
            {"file": str(args.result_file), "utf8_decode_error": str(exc)},
            ensure_ascii=False,
            indent=2,
        ))
        return 2

    rows = [json.loads(line) for line in raw.splitlines() if line.strip()]
    details = []
    correct = 0
    evaluable = 0
    garbled_rows = 0
    for row in rows:
        text = row.get("response_text") or ""
        reasoning = row.get("reasoning_text") or ""
        row_anomalies = sorted(set(anomalies(text) + anomalies(reasoning)))
        if row_anomalies:
            garbled_rows += 1
        expected = EXPECTED.get(row.get("slot")) if args.version == "simplified" else None
        answer_correct = None
        if expected is not None and row.get("ok") and text:
            evaluable += 1
            answer_correct = text.strip() == expected
            correct += int(answer_correct)
        if (not row.get("ok")) or row_anomalies or answer_correct is False or not text:
            details.append({
                "round": row.get("round"),
                "slot": row.get("slot"),
                "request_id": row.get("request_id"),
                "http_status": row.get("http_status"),
                "error": row.get("error"),
                "expected_answer": expected,
                "actual_answer": text[:500] if text else None,
                "reasoning_preview": reasoning[:500] if reasoning else None,
                "encoding_anomalies": row_anomalies,
            })

    successes = [row for row in rows if row.get("ok")]
    summary = {
        "file": str(args.result_file.resolve()),
        "version": args.version,
        "total_requests": len(rows),
        "successes": len(successes),
        "failures": len(rows) - len(successes),
        "http_statuses": dict(collections.Counter(
            str(row.get("http_status")) for row in rows
        )),
        "errors": dict(collections.Counter(
            row.get("error") for row in rows if row.get("error")
        )),
        "latency_seconds": numeric_stats([
            row["elapsed_seconds"] for row in rows
            if row.get("elapsed_seconds") is not None
        ]),
        "input_tokens": numeric_stats([
            row["input_tokens"] for row in rows
            if row.get("input_tokens") is not None
        ]),
        "output_tokens": numeric_stats([
            row["output_tokens"] for row in rows
            if row.get("output_tokens") is not None
        ]),
        "empty_response_text": sum(not bool(row.get("response_text")) for row in rows),
        "empty_reasoning_text": sum(not bool(row.get("reasoning_text")) for row in rows),
        "garbled_rows": garbled_rows,
        "answer_evaluable": evaluable if args.version == "simplified" else None,
        "answer_correct": correct if args.version == "simplified" else None,
        "answer_accuracy": round(correct / evaluable, 4) if evaluable else None,
        "needs_manual_semantic_review": args.version == "legacy",
        "anomalous_or_failed_rows": details,
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    is_correct = args.version == "legacy" or correct == len(rows)
    return 0 if not summary["failures"] and not garbled_rows and is_correct else 1


if __name__ == "__main__":
    raise SystemExit(main())
