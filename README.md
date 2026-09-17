# skill_hub

Richard 的个人 Codex Skill Git 存档仓库。

## 目录

```text
skills/<skill-name>/   完整 Skill 存档
docs/                  设计和实施记录
```

Codex 实际加载的运行副本位于 `/Users/richard/.codex/skills/<skill-name>`。本仓库保存经过验证的镜像，不替换运行目录，也不通过软链接耦合两个位置。

## 当前存档

| Skill | 用途 |
|---|---|
| `dash-dev-server-remote` | 管理 `dash-dev-server` SSH 快捷口令 |
| `kvs-fast-check` | 快速探测并分析 KVS/DashScope 模型服务 |
| `managing-personal-skills` | 管理个人 Skill 的验证、存档、提交与推送 |
| `visualizing-code-summaries` | 用独立彩色 HTML 总结代码架构、特性或提交变更 |

## 存档规则

1. 仅存档 Richard 自己创建或明确接管维护的 Skill。
2. 不存档 `.system`、插件缓存、系统内置 Skill，以及带有外部来源标记（例如 `x-source: aone-open`）的第三方 Skill。
3. 新建或修改个人 Skill 后，先运行官方 `quick_validate.py`，再将完整目录同步到 `skills/<skill-name>`。
4. 使用递归比较确认运行副本与存档一致；提交前检查敏感信息、占位符和 `git diff --check`。
5. 只暂存当前 Skill 相关路径，创建清晰的提交并推送当前分支的上游远端。

详细操作由 `managing-personal-skills` Skill 约束。
