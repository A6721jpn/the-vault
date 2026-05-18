---
type: memory-proposal
project: <project-name>
status: proposed
created: <YYYY-MM-DD>
updated: <YYYY-MM-DD>
source: ai-session
confidence: low | medium | high
sensitivity: low | medium | high
canonical_target: <repo-doc-path-or-none>
tags:
  - ai-memory
---

# メモ提案: <短いタイトル>

## 観察
<何が分かったか。自然文は日本語で書く。>

## 根拠
- 関連ファイル: `<path>`
- 実行コマンド: `<command>`
- 関連するエラー / 挙動: `<summary>`
- セッション日: `<YYYY-MM-DD>`

## 昇格先の提案
<採用する場合、どの repo doc に反映するか。反映不要ならその理由を書く。>

## なぜ重要か
<将来のミス防止や作業短縮にどう役立つか。>

## 検証状況
- [ ] テストで確認済み
- [ ] ソースコードで確認済み
- [ ] maintainer が確認済み
- [ ] 未検証

## リスク
<branch 固有、一時対応、古い情報、誤解を招く可能性があるか。>

## 判断
- [ ] 昇格する
- [ ] memory にだけ残す
- [ ] archive する
- [ ] reject する
