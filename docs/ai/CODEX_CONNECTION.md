# Codex 接続状態

## 現在の構成

この環境では、Codex の user-level 設定から Basic Memory MCP server を起動し、外部 vault を全プロジェクト共通の memory として使う。

- Codex config: `C:/Users/aokuni/.codex/config.toml`
- Global instructions: `C:/Users/aokuni/.codex/AGENTS.md`
- Basic Memory project: `codex-vault`
- Vault path: `C:/Users/aokuni/Obsidian/AI-Memory-Vault`
- MCP command: `C:/Users/aokuni/.local/bin/basic-memory.exe`
- MCP args: `mcp --project codex-vault`

## Codex から見た扱い

`~/.codex/config.toml` の MCP server は user-level 設定なので、Codex が設定を読み込めば、どの project でも同じ `codex-vault` を使える。

ただし、外部 memory を常に全文読み込みするわけではない。repo docs と code を優先し、不足するときに検索・読み取りを行う。

## 自動蓄積の方針

将来も役に立つ知見は、次の形で外部 vault に残す。

- agent が生成する提案: `00-inbox/memory-proposals/`
- session summary: `00-inbox/session-summaries/`
- 人間の開発判断: `10-projects/<project>/decisions.md`
- review 済みの横断知識: `20-global/`
- 昇格レビュー記録: `80-promoted/YYYY-MM/`

正本 docs への昇格は、人間の明示承認または承認済み review workflow がある場合だけ行う。

## 検証済み

- Basic Memory 0.21.1 を user tool として install 済み。
- `codex-vault` を default project として登録済み。
- `C:/Users/aokuni/Obsidian/AI-Memory-Vault` を reindex 済み。
- `search-notes` で既存 note を検索できる。
- `read-note` で既存 note を読み取れる。
- `write-note` で `00-inbox/memory-proposals/` に setup note を作成できる。
- Vault 全体の secret scan は通過済み。

## 未確認

- 現在の Codex セッションは起動済みのため、新しい MCP server はこの turn の tools には出ていない。
- Codex を再起動した後、`basic-memory` MCP tools が Codex UI / tool list に表示されることを確認する必要がある。

## 注意

Basic Memory CLI に PowerShell stdin で日本語本文を渡すと、環境によって文字化けすることがある。日本語 note を作るときは、Codex の file edit、MCP tool、または UTF-8 が保証された経路を使う。
