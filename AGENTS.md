# AGENTS.md — OpenFAPTA

このリポジトリーは、FAPTA（Fold Autonomous Potential Transaction Architecture）を、
哲学実験、数理トイモデル、地域資源観測へ分けて試す公開研究棚です。

## 原初目的

- FIAT台帳へ載らない贈与、信仰実践、維持、循環、探索を不存在へしない
- 未知のriskを安全へ変換しない
- 未知のbenefitをゼロへ変換しない
- 信仰が投資、信用、探索配分を動かす作用と、物理的結果を別々に記録する
- 未探索枝を現在の価格、実績、制度、KPIだけで焼却しない

## 必読順序

1. `README.md`
2. `docs/philosophy/open-fapta-principles.ja.md`
3. `docs/theory/toy-model-boundary.ja.md`
4. `experiments/TEMPLATE.ja.md`
5. 変更対象に最も近いcode、test、source台帳

ZeroRoomLab共通の主張・言語規約は、公開正本である
`saitoomituru/ZeroRoomLab-manifest`を参照します。Manifest全文を複製しません。

## 棚

- `docs/philosophy/`: 信仰、価値、FIAT、探索目的。Layer B。
- `docs/theory/`: 既存数学・経済理論との対応と射程。Layer CまたはA/C。
- `src/`: 実行可能なトイモデル。Layer A。
- `experiments/`: 観測、結果、考察、仮説、内観、未知を分けた実験記録。
- `receipts/`: 公開可能な機械検査結果。秘密や生の個人情報を置かない。

## 不変条件

```text
unknown risk    != safe
unknown benefit != zero
belief          != physical proof
expectation     != observed result
accounting zero != physical absence
budget          != execution
responsibility  != executor
processed data  != new observation
```

- `UNPRICED_HI_Z`へ数値ゼロ、無限大、平均期待値を勝手に代入しない
- 観測前の期待、候補分布、関連周辺benefitを確定結果へ昇格しない
- 信仰が尽きた場合は`LAST_ORDER`で現在の探索経路を閉じ、価値ゼロや不存在を宣告しない
- 高riskという理由だけでbenefit候補を削除しない。隔離、損失上限、停止条件を先に検討する
- 信仰告白を病理、虚偽、科学的証拠へ自動変換しない
- 物理観測を信仰または金融モデルで上書きしない
- Shannon情報理論は経済価値の証明ではない。既知データ処理と新規観測を分ける境界として使う
- MMT、Chartalism、FIAT説明とFAPTA固有比喩を同一理論として表示しない
- 波動関数、Schrödingerの猫、Hi-Zは物理量子実装の主張へ昇格せず、情報子工学上の状態比喩と明示する
- 単一の総合価値scoreを作らない

## Python

- Python 3.11+
- 標準ライブラリーを既定とし、新規依存には理由を記録する
- 型ヒントと日本語docstringを付ける
- `print`はCLI出力だけに限定する
- testは`python3 -m unittest discover -s tests -v`

## 文書と実験

- 日本語を正本とする
- `[FACT]`、`[RESULT]`、`[INTERPRETATION]`、`[HYPOTHESIS]`、`[INNER]`、`[UNKNOWN]`を分ける
- 外部資料はURL、取得日、使った主張を記録する
- 過去資料への現在解釈を、過去時点の観測として遡及記録しない
- 新しい実験は`[DRAFT]`から開始し、自動的にREADMEへ昇格しない

## ライセンス

- code、Schema、CLI、test、機械可読fixture: Apache-2.0
- README、一般文書、哲学、実験文脈: CC-BY-4.0
- 外部引用・第三者資料: 元のライセンスと出典を保持し、本リポジトリーのライセンスへ再許諾しない

## commit

`[layer] scope: 日本語の説明`を基本とします。`layer`は`eng`、`phil`、`theory`、`docs`、`meta`です。
