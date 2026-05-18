# 正本昇格プレイブック

## 目的

外部 vault の memory proposal や開発判断ログを、repo docs へ昇格する時の手順を決める。

ここでいう「昇格」は、review 前の作業メモを `docs/`、ADR、runbook、pitfall docs などの正本に反映すること。

## 人間がやること

人間は、次の 5 点を確認して承認する。

1. この note は正本に入れる価値があるか。
2. secrets、顧客情報、個人情報を含まないか。
3. 根拠があるか。
4. 昇格先はどこが正しいか。
5. どの文言で正本に入れるか。

承認するときは、次のように書けばよい。

```text
この proposal は昇格してよい。
昇格先は docs/ai/PROMOTION_PLAYBOOK.md。
この文言で入れて: <入れたい内容>
```

文言まで決めない場合は、次の形でよい。

```text
この proposal は昇格してよい。
昇格先は docs/pitfalls/known-failures.md。
文言は任せるが、根拠と見直す条件を残して。
```

## Agent がやること

agent は、人間の承認を受けてから正本を編集する。

1. 対象 note を読む。
2. `docs/ai/MEMORY_POLICY.md` と `docs/ai/REVIEW_CHECKLIST.md` を読む。
3. secrets や個人情報がないか確認する。
4. 既存 docs と重複または矛盾しないか確認する。
5. 指定された昇格先を編集する。
6. 対象 note にレビュー結果を追記し、`status` を `promoted`、`archived`、`rejected` のいずれかに更新する。
7. 変更後の検証コマンドを実行する。
8. どの note を、どの正本へ、どの理由で反映したか報告する。

## 昇格先の選び方

| proposal の内容 | 昇格先 |
|---|---|
| architecture、public API、data model、deployment、module boundary | `docs/adr/` |
| agent の行動ルール、memory 運用、prompt protocol | `docs/ai/` |
| build、test、lint、verification 手順 | `docs/runbooks/build-test-lint.md` |
| debugging 手順、調査の進め方 | `docs/runbooks/debugging.md` |
| 既知の失敗、回避策、flaky test | `docs/pitfalls/` |
| 軽い開発判断、好み、判断基準 | external vault の `10-projects/<project>/decisions.md` |

## 昇格しない判断も残す

昇格しない場合も、理由を対象 note に残す。

例:

```text
結論: 正本へ昇格しない。
理由: smoke test の作業記録であり、将来の agent 行動を変える知見ではない。
次の扱い: memory にだけ残す。不要になったら archive する。
```

## デモの読み方

外部 vault に、次のデモ記録がある。

- `80-promoted/2026-05/promotion-review-demo.md`: 昇格しない場合のレビュー例。
- `80-promoted/2026-05/promotion-approval-demo.md`: 昇格する場合のレビュー例。

昇格する場合は、人間の承認文、正本への反映内容、対象 note の status 更新、検証結果がそろっていることを確認する。
