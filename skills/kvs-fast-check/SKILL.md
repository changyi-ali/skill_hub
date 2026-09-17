---
name: kvs-fast-check
description: Use when the user says “kvs快查” or asks to quickly probe a Bailian/DashScope model service and analyze its load-test responses for correctness, timeouts, empty output, or garbled text.
---

# KVS 快查

快速验证模型服务链路，再运行指定的 30k Token 压测脚本并分析完整 JSONL。不要把 API Key 写入技能、日志或回复。

## 固定脚本

| 用户选择 | 脚本 | 内容判定 |
|---|---|---|
| 原版 | `/Users/richard/code/scripts/dashscope_30k_load_test_legacy.py` | 结合五个原始主题、实际 prompt 尾部和完整回答进行语义检查 |
| 简化版 | `/Users/richard/code/scripts/dashscope_30k_load_test.py` | 槽位 1–5 的 `response_text.strip()` 应严格等于 `1、4、9、16、25` |

## 触发后的确认

先收集并向用户复述以下四项；缺失时再询问，不要猜测：

1. 百炼接口完整 URL。
2. 模型名称。
3. API Key。可以读取用户指定的环境变量或接收本次临时值。
4. 原版或简化版。

API Key 只能显示前 6 位和后 4 位，例如 `sk-abc…1234`。列出最终配置并取得一次明确确认。该确认授权随后的一次“你好”预检和一次所选脚本压测；不要在两步之间重复索要确认。

## 执行

如果使用 `~/.zshrc` 中的配置，在同一个 zsh 进程中加载它。默认从 `DASHSCOPE_TEST_URL`、`DASHSCOPE_TEST_MODEL` 和 `DASHSCOPE_API_KEY` 读取三项配置。若用户直接提供 Key，只放入该次进程的 `DASHSCOPE_API_KEY`，不得写回配置文件。

1. 运行单并发预检：

   ```bash
   python3 ~/.codex/skills/kvs-fast-check/scripts/preflight.py \
     --endpoint "<endpoint>" --model "<model>" --timeout 30
   ```

   预检只发送一个 `你好`，使用百炼原生协议、`enable_thinking=false`、`max_tokens=32`。预检失败或超时便停止，不运行压测；报告 HTTP 层可观察到的错误，不把“没有返回内容”误报成“没有乱码”。

2. 预检成功后运行所选脚本。显式传入已确认的接口和模型，防止环境在确认后发生漂移；将带时间戳的结果写入 `/Users/richard/code/scripts/log/`。保留脚本默认的 20 轮、每轮 5 并发：

   ```bash
   python3 "<script>" --execute \
     --endpoint "<endpoint>" --model "<model>" \
     --output "/Users/richard/code/scripts/log/<result.jsonl>"
   ```

3. 分析结果：

   ```bash
   python3 ~/.codex/skills/kvs-fast-check/scripts/analyze_results.py \
     "<result.jsonl>" --version simplified
   ```

   原版将版本参数改为 `legacy`。分析器负责结构化统计；随后人工阅读所有错误和错误答案的完整 `response_text`、`reasoning_text` 与 `response_data`，确认自动规则没有误判。

## 报告要求

报告至少包含：

- 接口、模型、脚本版本和结果文件；API Key 仍只显示掩码。
- 总请求数、成功数、失败数、HTTP 状态和错误分布。
- 输入/输出 Token 与延迟范围。
- 空回答数量。thinking 关闭时 `reasoning_text` 为空是预期行为，报告数量但不要判为异常。
- 简化版逐槽位正确率及错误样本；原版逐槽位语义检查结论。
- UTF-8 解码错误、`�`、异常控制字符及常见 mojibake 模式。

若没有返回文本，乱码与回答正确性均写“不可判定”。一次执行结束后停止；未经用户要求不要自动重试。
