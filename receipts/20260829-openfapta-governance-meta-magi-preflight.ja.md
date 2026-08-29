# OpenFAPTA 開発規約メタMAGI事前監査

監査時点: 2026-08-29T19:12:56+09:00

対象revision: `e412bb0acdf0c1a634bc2fa8d761973e1a4ebe8b`

OAE資格: 現在時点の`[INTERPRETATION]`

歴史的同時点OAE: `historical-oae-unavailable`

## 対象とsource

- OpenFAPTA: `AGENTS.md`、`README.md`、既存の哲学・理論・実験・receipt
- ZeroRoomLab-manifest公開main: `6ecc13273d9485e93ce57e8148f963723681bc6c`
- SphereOS-Atlantis `dev/m6xx.1-reincarnation-sdk`: `68e6ef167bcbbe6b551631912378b71a56b92e14`
- OpenSourcePITETO: `8fb23031d9d4b1b4ae6ac134e3d6f52194a56a9f`
- KUMA800: `5bc455ce57b463017080584b972247bdd78f9974`

固定した公開sourceは`references/source-map.json`へ記録する。ローカルの未公開Manifest差分は
公開正本として採用しない。

## Maxwell

`[INTERPRETATION]` 原初目的と未知benefit保持は既存文書に残っている。一方、外部規約が単なる名称参照で、
次の開発者が未観測枝や不採用枝を焼却しないための実行導線がない。正確なSkillリンク、`UNKNOWN`、
`REJECT`枝保持、現在解釈の非遡及を追加すべきである。

位置依存の懸念として、規約をREADME全面へ載せると公開思想の入口を埋める。READMEは導線に留め、
詳細を運用文書へ分離する。

## Uriel

`[FACT]` 既存`AGENTS.md`にはManifestの文字列参照はあるが、固定revision、MAGI Skill、resolver、
User Gate、DOS証拠段階がない。機械可読source-mapとその検証器もない。

`[INTERPRETATION]` 固定URL、構造validator、回帰test、CIを追加し、CLI存在からmergeまでを別証拠にする。
DOS runtime、自律runner、native `experiment run` adapterは`NOT IMPLEMENTED`のまま明記する。

## Raphael

`[INTERPRETATION]` Meaningを哲学、Vesselを文書・code、Bridgeを`AGENTS.md`と運用規約、Supplyを
固定source-map・検証器・receiptへ配置する。`AGENTS.md`には必須規則だけを置き、詳細と参照座標を
別fileへ分離する。ローカルgreenと公開CI greenも別層として扱う。

## 合意、相違、UNKNOWN

- 合意: 現状は思想不足ではなく運用Bridge不足であり、`REVISE`する
- 相違: 規約の集中配置か分離配置か。必須規則を`AGENTS.md`、詳細を運用文書へ置くことで両方を保持する
- `[UNKNOWN]`: OpenFAPTAを既存workspaceやManifest registryへ登録する必要性と権限。今回変更しない
- 未搭載の意味: 外部Skillへのリンクはruntime搭載、統合、変更権限を意味しない

## 判定

`REVISE -> 第1段実装可`

公開後はremote上の実treeとCIを対象に、同じ三方向を独立して再監査する。
