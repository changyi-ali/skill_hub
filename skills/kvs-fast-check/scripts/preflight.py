#!/usr/bin/env python3
"""Send one small native DashScope request without exposing the API key."""

from __future__ import annotations

import argparse
import json
import os
import time
import urllib.error
import urllib.request


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--endpoint", required=True)
    parser.add_argument("--model", required=True)
    parser.add_argument("--timeout", type=float, default=30)
    return parser.parse_args()


def extract_message(data: dict) -> tuple[str | None, str | None]:
    try:
        message = data["output"]["choices"][0]["message"]
    except (KeyError, IndexError, TypeError):
        return None, None
    content = message.get("content")
    if isinstance(content, list):
        content = "".join(
            str(part.get("text", "")) for part in content if isinstance(part, dict)
        )
    reasoning = message.get("reasoning_content")
    if isinstance(reasoning, list):
        reasoning = "".join(
            str(part.get("text", "")) for part in reasoning if isinstance(part, dict)
        )
    return (
        content if isinstance(content, str) else None,
        reasoning if isinstance(reasoning, str) else None,
    )


def main() -> int:
    args = parse_args()
    api_key = os.environ.get("DASHSCOPE_API_KEY")
    if not api_key:
        raise SystemExit("DASHSCOPE_API_KEY is not set")
    payload = {
        "model": args.model,
        "input": {"messages": [{"role": "user", "content": "你好"}]},
        "parameters": {
            "result_format": "message",
            "enable_thinking": False,
            "max_tokens": 32,
        },
    }
    request = urllib.request.Request(
        args.endpoint,
        data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
        method="POST",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
    )
    started = time.monotonic()
    result = {
        "ok": False,
        "http_status": None,
        "elapsed_seconds": None,
        "request_id": None,
        "response_text": None,
        "reasoning_text": None,
        "error": None,
    }
    try:
        with urllib.request.urlopen(request, timeout=args.timeout) as response:
            result["http_status"] = response.status
            raw = response.read().decode("utf-8", errors="strict")
        data = json.loads(raw)
        result["request_id"] = data.get("request_id")
        result["response_text"], result["reasoning_text"] = extract_message(data)
        result["ok"] = 200 <= int(result["http_status"]) < 300
    except urllib.error.HTTPError as exc:
        result["http_status"] = exc.code
        raw = exc.read().decode("utf-8", errors="replace")
        try:
            data = json.loads(raw)
            result["request_id"] = data.get("request_id") or (data.get("error") or {}).get("request_id")
            result["error"] = data.get("message") or (data.get("error") or {}).get("message") or raw[:500]
        except json.JSONDecodeError:
            result["error"] = raw[:500]
    except Exception as exc:
        result["error"] = f"{type(exc).__name__}: {exc}"
    result["elapsed_seconds"] = round(time.monotonic() - started, 3)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
