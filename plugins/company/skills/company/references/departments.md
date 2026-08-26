# 部署別テンプレート集

組織構築時に各部署フォルダへ配置するテンプレート。
秘書室は初期構築で自動作成。他の部署は必要に応じて追加される。

---

## 1. 秘書室

### デイリーTODO（secretary/todos/_template.md）

```markdown
---
date: "{{YYYY-MM-DD}}"
type: daily
---

# {{YYYY-MM-DD}} ({{DAY_OF_WEEK}})

## 最優先
- [ ]

## 通常
- [ ]

## 余裕があれば
- [ ]

## 完了
- [x]

## メモ・振り返り
-
```

### Inbox（secretary/inbox/_template.md）

```markdown
---
date: "{{YYYY-MM-DD}}"
type: inbox
---

# Inbox - {{YYYY-MM-DD}}

## キャプチャ

- **{{HH:MM}}** |
```

### 壁打ち・相談メモ（secretary/notes/_template.md）

```markdown
---
created: "{{YYYY-MM-DD}}"
topic: ""
type: note
tags: []
---

# [相談テーマ]

## 背景・きっかけ
何について考えたい？

## 議論・思考メモ
-

## 結論・ネクストアクション
- [ ]
```

### 意思決定ログ（secretary/notes/YYYY-MM-DD-decisions.md）

```markdown
---
date: "{{YYYY-MM-DD}}"
type: decisions
---

# 意思決定ログ - {{YYYY-MM-DD}}

## 決定事項

### [タイトル]
- **背景**: 何が起きた？
- **判断**: 何を決めた？
- **理由**: なぜ？
- **対応部署**: どこで実行？
- **フォローアップ**: [ ]
```

### 秘書室トップ（secretary/_template.md）

```markdown
---
type: department
name: 秘書室
role: 窓口・相談役・タスク管理
---

# 秘書室

何でもお気軽にどうぞ。TODO管理、壁打ち、メモ、何でも承ります。

## サブフォルダ
- `inbox/` - クイックキャプチャ。とりあえずここに
- `todos/` - 日次タスク管理
- `notes/` - 壁打ち・相談メモ・意思決定ログ
```

---

## 2. PM（プロジェクト管理）

### 部署トップ（pm/_template.md）

```markdown
---
type: department
name: PM
role: プロジェクト進捗・マイルストーン・チケット管理
---

# PM（プロジェクト管理）

プロジェクトの立ち上げから完了まで管理します。

## サブフォルダ
- `projects/` - プロジェクトごとの管理ファイル
- `tickets/` - タスクチケット
```

### プロジェクト（pm/projects/_template.md）

```markdown
---
created: "{{YYYY-MM-DD}}"
project: ""
status: planning
tags: []
---

# プロジェクト: [名前]

## 概要
このプロジェクトは何？

## ゴール
何を達成する？

## マイルストーン
| # | マイルストーン | 期限 | 状態 |
|---|-------------|------|------|
| 1 |             |      | 未着手 |

## 関連部署
-

## メモ
-
```

### チケット（pm/tickets/_template.md）

```markdown
---
created: "{{YYYY-MM-DD}}"
project: ""
assignee: ""
priority: normal
status: open
---

# [チケットタイトル]

## 内容
何をする？

## 完了条件
- [ ]

## メモ
-
```

---

## 3. リサーチ

### 部署トップ（research/_template.md）

```markdown
---
type: department
name: リサーチ
role: 市場調査・競合分析・技術調査
---

# リサーチ

調査・分析を担当します。

## サブフォルダ
- `topics/` - 調査トピックごとのファイル
```

### 調査トピック（research/topics/_template.md）

```markdown
---
created: "{{YYYY-MM-DD}}"
topic: ""
status: in-progress
tags: []
---

# 調査: [トピック]

## 目的
なぜ調査する？

## 調査内容

### 情報源 1
- URL:
- 要点:

## 結論
-

## ネクストアクション
- [ ]

## 参考リンク
-
```

---

## 4. マーケティング

### 部署トップ（marketing/_template.md）

```markdown
---
type: department
name: マーケティング
role: コンテンツ企画・SNS戦略・集客
---

# マーケティング

コンテンツ企画と集客を担当します。

## サブフォルダ
- `content-plan/` - コンテンツ企画
- `campaigns/` - キャンペーン管理
```

### コンテンツ企画（marketing/content-plan/_template.md）

```markdown
---
created: "{{YYYY-MM-DD}}"
platform: ""
status: draft
publish_date: ""
tags: []
---

# [コンテンツタイトル]

## プラットフォーム
ブログ / YouTube / SNS / その他

## ターゲット
誰に向けて？

## 構成
1.
2.
3.

## キーメッセージ


## 下書き


## ステータス
- [ ] 構成
- [ ] 下書き
- [ ] レビュー
- [ ] 公開
```

### キャンペーン（marketing/campaigns/_template.md）

```markdown
---
created: "{{YYYY-MM-DD}}"
campaign: ""
status: planning
period: ""
---

# キャンペーン: [名前]

## 目的
何を達成する？

## ターゲット
-

## チャネル
-

## 予算
-

## KPI
| 指標 | 目標 | 実績 |
|------|------|------|
|      |      |      |

## 振り返り
-
```

---

## 5. 開発

### 部署トップ（engineering/_template.md）

```markdown
---
type: department
name: 開発
role: 技術ドキュメント・設計・デバッグ
---

# 開発

技術的なドキュメントと設計を管理します。

## サブフォルダ
- `docs/` - 技術ドキュメント・設計書
- `debug-log/` - デバッグ・バグ調査ログ
```

### 技術ドキュメント（engineering/docs/_template.md）

```markdown
---
created: "{{YYYY-MM-DD}}"
topic: ""
type: technical-doc
tags: []
---

# [ドキュメントタイトル]

## 概要


## 設計・方針


## 詳細


## 参考
-
```

### デバッグログ（engineering/debug-log/_template.md）

```markdown
---
created: "{{YYYY-MM-DD}}"
status: open
tags: []
---

# [バグ・問題のタイトル]

## 症状
何が起きている？

## 期待する動作


## 再現手順
1.

## 調査

### 仮説
-

### 発見
-

## 解決策
-

## 再発防止
-
```

---

## 6. 経理

### 部署トップ（finance/_template.md）

```markdown
---
type: department
name: 経理
role: 請求書・経費・売上管理・イベント物販会計
---

# 経理

お金周りを管理します。

## サブフォルダ
- `invoices/` - 請求書
- `expenses/` - 経費
- `events/` - イベント物販会計（デザフェス等の出展収支）
```

### 請求書（finance/invoices/_template.md）

```markdown
---
date: "{{YYYY-MM-DD}}"
client: ""
amount: 0
status: unpaid
due_date: ""
---

# 請求書: [クライアント名] - {{YYYY-MM-DD}}

## 明細
| 項目 | 数量 | 単価 | 小計 |
|------|------|------|------|
|      |      |      |      |

## 合計


## 支払い状況
- [ ] 送付済み
- [ ] 入金確認済み
```

### 経費（finance/expenses/_template.md）

```markdown
---
date: "{{YYYY-MM-DD}}"
category: ""
amount: 0
---

# 経費: [概要]

## 詳細
| 日付 | 項目 | カテゴリ | 金額 | メモ |
|------|------|---------|------|------|
|      |      |         |      |      |

## 合計

```

### イベント物販会計（finance/events/_template.md）

デザフェス等の出展物販の収支を「事前・当日・事後」で管理する。
精度の肝は **在庫・売上・現金の三点突合**。3つが一致しなければ記録漏れか釣り銭ミス。

```markdown
---
date: "{{YYYY-MM-DD}}"
event: ""
booth: ""
status: planning
gross_sales: 0
net_profit: 0
---

# イベント収支: [イベント名] - {{YYYY-MM-DD}}

## 1. 事前（予算・原価）

### 固定費（出展に必要な経費）
| 項目 | 金額 | メモ |
|------|------|------|
| ブース代・出展料 |  |  |
| 設営・什器・POP |  |  |
| 交通費・宿泊費 |  |  |
| その他 |  |  |
| **固定費 合計** |  |  |

### 商品ラインナップ（SKU単位・1点あたり原価）
| 商品 | 単価 | 原価/点 | 持込数 | 想定原価 |
|------|------|---------|--------|----------|
|      |      |         |        |          |
| **合計** |  |  |  |  |

### 損益分岐点
- 必要売上 = 固定費合計 ÷ 平均粗利率
- 何個売れば黒字: （固定費 ÷ 1点あたり平均粗利）≒ ___ 個

## 2. 当日（売上）

### 商品別 実績
| 商品 | 持込数 | 残数 | 販売数 | 単価 | 売上 |
|------|--------|------|--------|------|------|
|      |        |      |        |      |      |
| **合計** |    |      |        |      |      |

### 決済手段別（現金とキャッシュレスは必ず分ける）
| 手段 | 売上 | メモ |
|------|------|------|
| 現金 |  |  |
| PayPay等QR |  | 後日入金 |
| クレジット |  | 後日入金 |
| **合計** |  |  |

### つり銭準備金（売上とは別管理）
- 開始時つり銭: ___ 円
- 終了時レジ現金: ___ 円
- 現金売上（理論）= 終了時レジ − 開始時つり銭 = ___ 円

## 3. 事後（三点突合・損益）

### 三点突合（ここが精度チェックの心臓部）
| 観点 | 数値 | 一致? |
|------|------|-------|
| A. 在庫から: 持込数 − 残数 = 販売数 |  |  |
| B. 記録から: 商品別売上の数量合計 |  |  |
| C. 現金から: 現金売上 ÷ 平均単価（参考） |  |  |
- A と B が一致するか → ズレたら記録漏れ
- 現金売上（理論）と実際のレジ現金が一致するか → ズレたら釣り銭ミス

### 損益サマリー
| 項目 | 金額 |
|------|------|
| 総売上 |  |
| − 商品原価（販売数 × 原価/点） |  |
| − 人件費 |  |
| − 固定費（ブース代・什器等） |  |
| − 流動費（交通・送料等） |  |
| **= 営業利益** |  |
| 原価率（原価 ÷ 売上） |  % |
| 営業利益率（営業利益 ÷ 売上） |  % |

> **整合性チェック（必ず一致させる）**: 総売上 = 商品別売上の合計 = 決済手段別の合計 = 営業利益 + 原価 + 人件費 + 固定費 + 流動費。1つでも合わなければ転記ミス。
> ※ ワークショップ・体験・ガチャ等のサービス型も「商品」として単価×数量で同じ表に入れる。

### 商品別 消化率
| 商品 | 持込数 | 販売数 | 消化率% |
|------|--------|--------|---------|
|      |        |        |         |

## 4. 振り返り（次回への精度向上）
- 完売・品切れした商品:
- 売れ残った商品:
- 突合のズレと原因:
- 次回の改善:
```

---

## 7. 営業

### 部署トップ（sales/_template.md）

```markdown
---
type: department
name: 営業
role: クライアント管理・提案書・案件パイプライン
---

# 営業

クライアントとの関係を管理します。

## サブフォルダ
- `clients/` - クライアント情報
- `proposals/` - 提案書
```

### クライアント（sales/clients/_template.md）

```markdown
---
client: ""
created: "{{YYYY-MM-DD}}"
status: active
---

# クライアント: [名前]

## 連絡先
- 名前:
- メール:
- 会社:

## 案件履歴
| 案件 | 期間 | 金額 | 状態 |
|------|------|------|------|
|      |      |      |      |

## コミュニケーション履歴

### {{YYYY-MM-DD}}
-

## メモ
-
```

### 提案書（sales/proposals/_template.md）

```markdown
---
created: "{{YYYY-MM-DD}}"
client: ""
status: draft
---

# 提案書: [タイトル]

## クライアント


## 課題・ニーズ


## 提案内容


## スケジュール
| フェーズ | 期間 | 内容 |
|---------|------|------|
|         |      |      |

## 見積もり
| 項目 | 金額 |
|------|------|
|      |      |

## 合計

```

---

## 8. クリエイティブ

### 部署トップ（creative/_template.md）

```markdown
---
type: department
name: クリエイティブ
role: デザインブリーフ・ブランド管理・アセット管理
---

# クリエイティブ

デザインとブランドを管理します。

## サブフォルダ
- `briefs/` - デザインブリーフ
- `assets/` - アセット管理
```

### デザインブリーフ（creative/briefs/_template.md）

```markdown
---
created: "{{YYYY-MM-DD}}"
project: ""
status: draft
---

# デザインブリーフ: [タイトル]

## 目的
何のためのデザイン？

## ターゲット


## トーン・雰囲気


## 要件
- サイズ:
- 形式:
- 納期:

## 参考イメージ
-

## フィードバック
-
```

### アセット管理（creative/assets/_template.md）

```markdown
---
created: "{{YYYY-MM-DD}}"
type: asset-list
---

# アセット管理

| アセット名 | 種類 | 場所 | 更新日 | メモ |
|-----------|------|------|-------|------|
|           |      |      |       |      |
```

---

## 9. 人事

### 部署トップ（hr/_template.md）

```markdown
---
type: department
name: 人事
role: 採用管理・オンボーディング・チーム管理
---

# 人事

チームと採用を管理します。

## サブフォルダ
- `hiring/` - 採用管理
```

### 採用（hr/hiring/_template.md）

```markdown
---
created: "{{YYYY-MM-DD}}"
position: ""
status: open
---

# 採用: [ポジション名]

## 要件
-

## 候補者
| 名前 | 応募日 | ステータス | メモ |
|------|-------|----------|------|
|      |       |          |      |

## 選考プロセス
- [ ] 書類選考
- [ ] 面接
- [ ] 最終面接
- [ ] オファー
```

---

## 10. 汎用テンプレート

ユーザーが追加するカスタム部署用のフォールバック。

```markdown
---
type: department
name: "[部署名]"
role: "[役割]"
---

# [部署名]

## 概要
この部署の役割。

## メモ
-
```

### 汎用ファイルテンプレート

```markdown
---
created: "{{YYYY-MM-DD}}"
tags: []
---

# [タイトル]

## 内容
-

## メモ
-
```

---
---

# 部署別 CLAUDE.md テンプレート

各部署フォルダに `CLAUDE.md` を配置し、部署固有のルールと振る舞いを定義する。
部署追加時に該当する CLAUDE.md を自動生成する。

---

## secretary/CLAUDE.md

```markdown
# 秘書室

## 役割
オーナーの常駐窓口。何でも相談に乗り、タスク管理・壁打ち・メモを担当する。

## 口調・キャラクター
- 丁寧だが堅すぎない。「〜ですね！」「承知しました」「いいですね！」
- 主体的に提案する。「ついでにこれもやっておきましょうか？」
- 壁打ち時はカジュアルに寄り添う
- 過去のメモや決定事項を参照して文脈を持った対話をする

## ルール
- オーナーからの入力はまず秘書が受け取る
- 秘書で完結するもの（TODO、メモ、壁打ち、雑談）は直接対応
- 部署の作業が必要な場合は該当部署のフォルダに直接書き込む
- 該当部署が未作成の場合は secretary/notes/ に保存する
- TODO形式: `- [ ] タスク | 優先度: 高/通常/低 | 期限: YYYY-MM-DD`
- 日次ファイルは `todos/YYYY-MM-DD.md`
- Inboxは `inbox/YYYY-MM-DD.md`。迷ったらまずここ
- 壁打ちの結論が出たら `notes/` に保存を提案する
- 意思決定は `notes/YYYY-MM-DD-decisions.md` に記録する
- 同じ日付のファイルがすでにある場合は追記する。新規作成しない
- ファイル操作前に必ず今日の日付を確認する

## 部署追加の提案
- 同じ領域のタスクが2回以上繰り返されたら、部署作成を提案する
- ユーザーが明示的に依頼した場合は即座に作成する

## フォルダ構成
- `inbox/` - 未整理のクイックキャプチャ
- `todos/` - 日次タスク管理（1日1ファイル）
- `notes/` - 壁打ち・相談メモ・意思決定ログ（1トピック1ファイル）
```

---

## pm/CLAUDE.md

```markdown
# PM（プロジェクト管理）

## 役割
プロジェクトの立ち上げから完了まで進捗を管理する。

## ルール
- プロジェクトファイルは `projects/project-name.md`
- チケットは `tickets/YYYY-MM-DD-title.md`
- プロジェクトのステータス: planning → in-progress → review → completed → archived
- チケットのステータス: open → in-progress → done
- チケット優先度: high / normal / low
- 新規プロジェクト作成時は必ずゴールとマイルストーンを定義
- マイルストーン完了時は秘書のTODOに報告を追記

## フォルダ構成
- `projects/` - プロジェクト管理（1プロジェクト1ファイル）
- `tickets/` - タスクチケット（1チケット1ファイル）
```

---

## research/CLAUDE.md

```markdown
# リサーチ

## 役割
市場調査、競合分析、技術調査を行い、調査結果をまとめる。

## ルール
- 調査ファイルは `topics/topic-name.md`
- ステータス: planning → in-progress → completed
- 情報源は必ずURLまたは出典を記載
- 調査結果には必ず「結論」と「ネクストアクション」を含める
- 調査完了時は秘書のTODOに報告を追記

## フォルダ構成
- `topics/` - 調査トピック（1トピック1ファイル）
```

---

## marketing/CLAUDE.md

```markdown
# マーケティング

## 役割
コンテンツ企画、SNS戦略、キャンペーン管理を担当する。

## ルール
- コンテンツ企画は `content-plan/platform-title.md`
- キャンペーンは `campaigns/campaign-name.md`
- コンテンツのステータス: draft → writing → review → published
- キャンペーンのステータス: planning → active → completed → reviewed
- 公開日（publish_date）が決まっているものは必ず秘書のTODOにもリマインダーを入れる
- KPIは数値で設定し、振り返り時に実績を記入

## フォルダ構成
- `content-plan/` - コンテンツ企画（1コンテンツ1ファイル）
- `campaigns/` - キャンペーン管理（1キャンペーン1ファイル）
```

---

## engineering/CLAUDE.md

```markdown
# 開発

## 役割
技術ドキュメント、設計書、デバッグログを管理する。

## ルール
- 技術ドキュメントは `docs/topic-name.md`
- デバッグログは `debug-log/YYYY-MM-DD-issue-name.md`
- デバッグのステータス: open → investigating → resolved → closed
- 設計書は必ず「概要」「設計・方針」「詳細」の構成にする
- バグ修正時は「再発防止」セクションを必ず記入
- 技術的な意思決定は secretary/notes/ に意思決定ログとして残す

## フォルダ構成
- `docs/` - 技術ドキュメント・設計書
- `debug-log/` - デバッグ・バグ調査ログ
```

---

## finance/CLAUDE.md

```markdown
# 経理

## 役割
請求書、経費、売上、イベント物販会計の管理を担当する。

## ルール
- 請求書は `invoices/YYYY-MM-DD-client-name.md`
- 経費は `expenses/YYYY-MM-category.md`
- イベント物販会計は `events/YYYY-MM-DD-event-name.md`
- 金額は税込・税抜を明記する（デフォルト税込）
- 請求書のステータス: draft → sent → paid → overdue
- イベント会計のステータス: planning → onsite → settled
- 未入金の請求書は秘書のTODOにリマインダーを入れる
- 月末に月次の経費集計を行う

### イベント物販会計の精度ルール（デザフェス等）
- 必ず **商品（SKU）単位** で記録する。「売上合計いくら」だけにしない
- 原価は **1点あたり** で持ち、純利益 = 総売上 − 商品原価 − 固定費 を出す
- 決済手段は **現金 / QR / クレジットを分けて** 記録する（キャッシュレスは後日入金のため当日現金と混ぜない）
- **つり銭準備金は売上と完全分離**する。現金売上 = 終了時レジ現金 − 開始時つり銭
- イベント後は必ず **三点突合** を行う:
  - 在庫: 持込数 − 残数 = 販売数（A）
  - 記録: 商品別売上の数量合計（B）→ A と B が一致するか
  - 現金: 現金売上（理論）と実際のレジ現金が一致するか
  - ズレたら settled にせず原因（記録漏れ／釣り銭ミス）を特定する
- 終了後は商品別の消化率と振り返りを記録し、次回の持込数判断に使う

## フォルダ構成
- `invoices/` - 請求書（1請求1ファイル）
- `expenses/` - 経費（月別またはカテゴリ別）
- `events/` - イベント物販会計（1イベント1ファイル）
```

---

## sales/CLAUDE.md

```markdown
# 営業

## 役割
クライアント管理、提案書作成、案件パイプラインを管理する。

## ルール
- クライアントファイルは `clients/client-name.md`
- 提案書は `proposals/YYYY-MM-DD-proposal-title.md`
- クライアントのステータス: prospect → active → inactive
- 提案書のステータス: draft → sent → accepted → rejected
- コミュニケーション履歴はクライアントファイルに日付付きで追記
- 受注時はPMにプロジェクト作成を依頼、経理に請求書作成を連携

## フォルダ構成
- `clients/` - クライアント情報（1クライアント1ファイル）
- `proposals/` - 提案書（1提案1ファイル）
```

---

## creative/CLAUDE.md

```markdown
# クリエイティブ

## 役割
デザインブリーフの作成、ブランド管理、アセット管理を担当する。

## ルール
- デザインブリーフは `briefs/project-name-brief.md`
- アセット管理は `assets/asset-list.md` に一元管理
- ブリーフには必ず「目的」「ターゲット」「トーン」「要件」を含める
- ブリーフのステータス: draft → approved → in-production → delivered
- 納品物はアセット管理に登録する
- ブランドガイドラインがある場合は `brand-guidelines.md` として保存

## フォルダ構成
- `briefs/` - デザインブリーフ（1案件1ファイル）
- `assets/` - アセット管理
```

---

## hr/CLAUDE.md

```markdown
# 人事

## 役割
採用管理、チームメンバーのオンボーディング、チーム管理を担当する。

## ルール
- 採用ポジションは `hiring/position-name.md`
- 選考ステータス: open → screening → interviewing → offered → filled → closed
- 候補者情報は個人情報に注意し、必要最小限を記録
- オンボーディングチェックリストはポジションファイル内に含める
- 採用決定時は secretary/notes/ に意思決定ログを残す

## フォルダ構成
- `hiring/` - 採用管理（1ポジション1ファイル）
```

---

## 汎用部署 CLAUDE.md

カスタム部署用のフォールバック。

```markdown
# {{DEPARTMENT_NAME}}

## 役割
{{DEPARTMENT_ROLE}}

## ルール
- ファイル命名: `kebab-case-title.md`
- 1トピック1ファイル
- 同じ日付のファイルは追記、新規作成しない

## フォルダ構成
（カスタム）
```
