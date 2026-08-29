# OpenFAPTA 開発規約メタMAGI公開後監査

監査時点: 2026-08-29T19:21:54+09:00

対象revision: `0c3d82fff1d4eca3d89be849ea7ac2045450f61d`

remote `main`: `0c3d82fff1d4eca3d89be849ea7ac2045450f61d`

OAE資格: 現在時点の`[INTERPRETATION]`

歴史的同時点OAE: `historical-oae-unavailable`

## 公開観測

- `[FACT]` `git ls-remote origin refs/heads/main`は対象revisionを返した
- `[FACT]` GitHub Actions `Pythonトイモデル検査` run `33247584199`は`success`
- `[FACT]` 公開前のOpenFAPTA local検査は14 test成功、source-map 20件成功、CLI終了code 0
- `[FACT]` MAGI resolverは`composite / zeroroomlab / --require-local`で必須13件中13件を解決した
- `[FACT]` resolverはnetwork accessとsecret scanを実行していない

Actions: https://github.com/saitoomituru/OpenFAPTA/actions/runs/33247584199

## Maxwell

`[INTERPRETATION]` 原初目的、未知benefit、`REJECT`枝、`UNKNOWN`、非遡及は維持された。READMEは
短い監査導線だけなので、公開思想の入口を規約で埋めていない。User Gateは探索を禁止せず、公開やmergeを
別の意思決定としている。

`[UNKNOWN]` 規約が将来の実験者に実際どう働くかは、運用事例がまだない。文書の存在を文化の定着へ昇格しない。

## Uriel

`[FACT]` 固定SHA URL、構造validator、回帰test、CIが実装され、remote treeでgreenになった。
`AGENTS.md`はCLI、artifact、commit、push、CI、採用、mergeを別証拠にした。runtimeや自律runnerを
実装済みとは表示していない。

`[ADAPT]` 第1段のsource-mapは監査入口を含む一方、resolver必須13件の下位文書を6件列挙しておらず、
PLI／CLI境界文書も未登録だった。第2段で7件を固定表へ追加する。

`[UNKNOWN]` validatorはJSON構造と固定URLの座標整合だけを検査する。将来のupstream消失、内容変更、
意味上の適合、ネットワーク到達性は保証しない。

## Raphael

`[INTERPRETATION]` Meaningは哲学文書、Vesselはcodeと実験、Bridgeは`AGENTS.md`と開発規約、Supplyは
source-map、validator、test、receiptへ分離された。公開前後の監査も別receiptとなり、意図と公開treeが
同一証拠へ潰されていない。

位置依存の相違として、すべてのURLを`AGENTS.md`へ直書きする案は入口を肥大化させる。必須の読順と
意味境界は`AGENTS.md`、固定座標は機械可読表に置く現在配置を採用する。

## 合意、相違、未搭載の意味

- 合意: 第1段のBridgeは公開treeとCIで成立し、判定は`PASS WITH ADAPTATION`
- 相違: 集中配置か分離配置かは、入口と固定表の二層構造で保持する
- 未搭載の意味: MAGI/DOSへのリンクは、Atlantis runtime、Skill自動実行、FAMLog、自律runnerの搭載ではない
- `[UNKNOWN]`: workspace登録、Manifest registry登録、第三者運用での定着。今回の変更権限と検証範囲外

## 最終措置

第2段ではsource-mapを27件へ補完し、同じvalidator、14 test、CLI、remote SHA、Actionsを再検査する。
