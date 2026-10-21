# Openファプタ / OpenFAPTA

> 数字へ載らないから、存在しないことにするな。  
> 未知で危ないから、未来のbenefitまで焼くな。  
> 信じたから物理的に成功したことにもするな。掘りに行った記録を残せ。

**OpenFAPTAは、回収可能性と未知コモンズの探索余地を発見・試行・再評価する、オープン信用創造・汎用マーチャントエンジンです。**

通貨発行母体や信用供与主体が、どのFoldをどう接続し、どんな面積測度・評価単位で未来の回収可能性を組むかを設計します。未知コモンズ、探索フロンティア、ボラティリティ、他Foldの資源関係をM次元ポートフォリオとして扱う構想です。個人・組織・共同体・発行母体へ同じ構成原理を展開するフラクタル設計を目指します。

日本語正本 / [English reference manuscript](README.en-US.md)

FAPTAは **Fold Autonomous Potential Transaction Architecture** の略です。
現在のcodeは`EXPERIMENTAL / TOY MODEL`。資源の利用条件、未知benefit、期待・試行・観測・Last Orderを動かすPythonモデルがあります。汎用M次元チャート、永続的なリトライ管理、外部通貨adapterは設計・実装課題です。

## 発見して、試して、探索余地を更新する

回収候補を発見・登録し、実際に試し、条件を変えてリトライする。未知を埋めるだけでなく、新しい未知や探索フロンティアを発見し、次の与信判断へ戻します。未来予測だけでなく、どの未来を試せるかを扱うポートフォリオ管理です。

- 広いフロンティアと大きいボラ、安定回収と薄い髭を別々に読む。
- 他Foldの資源消耗による増加と、評価scope全体のプラスサム候補を区別する。
- 利用者が政治思想・通貨発行思想に応じてFold、トポロジー、面積測度、単位、配分policyを選ぶ。
- 交換単位、通貨発行・残高、決済、帳簿は外部実装へ接続する。暗号通貨、ステーブルコイン、商品券、ポイント等の選択をengineへ固定しない。

面積の評価単位と交換単位は別です。`ledger` CLIは台帳可視性のtoyであり、分散台帳engineではありません。
定義、構成例、現在の実装対応、次の比較実験は[マーチャントエンジン設計](docs/theory/merchant-engine.ja.md) / [en-US](docs/theory/merchant-engine.en-US.md)を参照してください。

## 問題設定

税金で委託された清掃には予算、契約、領収、労務時間が残ります。信仰から神社のゴミを拾った民にも
物理的な清掃結果はありますが、FIAT台帳には同じ強度では残りません。

この差から、次を別々に観測します。

```text
FIAT・令呪       誰が単位、債務、予算、命令可能性を発行したか
民・実行         誰が実際に拾い、直し、育て、維持したか
信仰・期待       何を信じたため、信用、投資、贈与、探索配分が動いたか
Hi-Z探索         まだ価格も確率も定まらない領域へ、誰が観測路を開いたか
物理結果         実際に何が起き、何が起きなかったか
```

会計上のゼロは物理的不在ではありません。一方、信じたという事実も物理的成功の証明ではありません。
ただし信仰や期待が資源配分を動かしたなら、それは金融工学・景気論側で無視できない入力です。

## 信仰が点火し、工学が観測する

このリポジトリーを始めた「benefitをマイニングできるはずだから掘ろう」は、齋藤みつるの信仰・期待であり、
探索を発動したInitiatorの事実です。その依頼を受けてCodexがモデルを実装し、Pythonがfixtureを演算し、
test runnerが結果を返したことは、記録された条件内の工学事実です。

```text
探索を始めた理由     = 信仰・期待
誰が何を実行したか   = 工学的な実行事実
toy fixtureの出力    = 条件付きの観測事実
現実社会での効果     = まだ未検証
```

信仰から始まったという理由で、後続の機械観測まで信仰へ格下げしません。反対に、toy内の工学事実を
現実経済、神社、空き家、地球資源の実証結果へ拡張もしません。起動動機と証拠資格を分離します。

## 中核不変条件

```text
unknown risk    != safe
unknown benefit != zero
belief          != physical proof
accounting zero != physical absence
processed data  != new observation
```

`UNPRICED_HI_Z`は「無限の価値」ではありません。現在の価格回路に接続されておらず、ゼロにも有限額にも
確定できない状態です。未知benefitを保持しながら、損失上限、隔離、停止条件を付けて探索します。

## 最初のトイモデル

標準ライブラリーだけで四つの境界を動かします。

```console
PYTHONPATH=src python3 -m openfapta.cli --model all
```

- `ledger`: 同じ物理清掃でもFIAT台帳の可視性が異なる例
- `activation`: 物理在庫、利用許可、維持者、変換路、時期の交差
- `information`: 決定的な加工だけでは対象世界との相互情報量が増えない例
- `exploration`: 未知benefitをゼロとせず、損失上限内で探索する例

探索状態は次のように分けます。

```text
EXPECTATION_HI_Z -> MINING -> OBSERVED
         |
         +-------------> LAST_ORDER
```

観測前の期待を結果として扱いません。信仰が尽きた場合も価値ゼロとは確定せず、その探索経路だけを
`LAST_ORDER`で閉じ、未観測枝を保存します。波動関数やSchrödingerの猫は物理量子の主張ではなく、
候補分布と確定観測を混ぜないための比喩です。

このモデルは経済予測器ではありません。FAPTAの主張を小さな反例、境界、状態遷移へ落とすための器です。

## 実行

```console
PYTHONPATH=src python3 -m unittest discover -s tests -v
PYTHONPATH=src python3 -m openfapta.cli --model all
```

## 棚

- [`docs/philosophy/`](docs/philosophy/): 信仰・FIAT・探索の原初命題
- [`docs/theory/`](docs/theory/): Shannon、MMT、数理モデルとの境界
- [`experiments/`](experiments/): OpenSourcePITETO式の実験ノート
- [`src/openfapta/`](src/openfapta/): Pythonトイモデル
- [`docs/sources/`](docs/sources/): Note、Manifest、実装の出典と来歴

公開NoteとIssue #1〜#6の根拠対応は
[`docs/sources/note-issue-mining-map.ja.md`](docs/sources/note-issue-mining-map.ja.md)にあります。
本文を転載せず、要約・正準URL・取得時fingerprintを索引バックアップとして保持します。

## 系譜

実験記録の型はOpenSourcePITETO、未知と来歴の保持はKUMA800、Meaning／Vessel／Bridge／Supplyと
検証証憑はSphereOS-Atlantis DOS、哲学・主張境界はZeroRoomLab-manifestを参照しています。
これらのリポジトリーをruntime依存として取り込みません。

## 開発・監査導線

自動開発、User Gate、MAGI三方向監査、DOS由来の証拠段階は
[`docs/operations/development-governance.ja.md`](docs/operations/development-governance.ja.md)を参照してください。
Manifest、MAGI Skill、SphereOS Atlantis DOS、OpenSourcePITETO、KUMA800の固定revisionは
[`references/source-map.json`](references/source-map.json)にあり、CIで構造を検査します。

## ライセンス

- code、Schema、CLI、test: [Apache License 2.0](LICENSE)
- README、文書、哲学、実験文脈: [CC BY 4.0](LICENSE-CONTEXT.md)
- 第三者資料: 出典元の条件を維持。本リポジトリーのライセンスへ自動再許諾しません

Copyright 2026 齋藤みつるSaitooMituru-Fusamofu-ふさもふ
