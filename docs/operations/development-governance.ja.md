# OpenFAPTA 自動開発・監査規約

状態: `ACTIVE / GOVERNANCE`

制定時点: 2026-08-29

対象: OpenFAPTA内のcode、文書、実験、公開証憑

## 1. 目的

この規約は、未知benefitを保護する哲学を、検証不能な権威語へ変えずに開発へ接続する。
Manifestは主張と言語の境界、MAGIは独立した三方向監査、SphereOS Atlantis DOS実験は
作業契約と証拠段階、OpenSourcePITETOとKUMA800は実験記録と来歴保持の参照元である。

これらへのリンクは参照関係であり、runtime依存、統合済み、変更権限を意味しない。

## 2. 開始時に固定するもの

変更前に次を記録または確認する。

- 対象リポジトリー、path、branch、base SHA、書込範囲
- 参照するsource capsuleと、そのrevision
- 実行する検査と、公開を含むUser Gate
- dirty stateの有無。既定の共有値は件数と有無だけで、pathやdiffは公開しない
- 既存tool、Skill、Schema、fixtureを再利用できるか

同一課題を複数laneで試す場合、各laneは同じbaseとsource capsuleから独立して開始し、
他laneの途中成果を暗黙入力にしない。

## 3. MAGI三方向監査

監査前に、固定参照表の必須sourceを解決する。ローカルでSphereOS-Atlantisを利用できる場合の
正準resolver例は次である。

```console
python3 -B /path/to/SphereOS-Atlantis/magi/0.2.1/resolve_sources.py \
  --slot composite \
  --profile zeroroomlab \
  --repo-root ZeroRoomLab-manifest=/path/to/ZeroRoomLab-manifest \
  --require-local
```

必須sourceが欠けた場合は`SOURCE-BLOCK`とし、代替資料による監査を正準監査へ昇格しない。

三つの観点は独立に記録する。

- Maxwell: 原初目的、倫理、未観測枝、未来価値を焼却していないか
- Uriel: 観測事実、実装、反証可能性、検査、主張強度が一致しているか
- Raphael: Meaning、Vessel、Bridge、Supplyの配置と責務境界が崩れていないか

結論は多数決や平均ではなく、合意、相違、`UNKNOWN`、未搭載の意味、位置依存の判断を残す。
監査は現在時点のInterpretation OAEであり、過去の意思決定へ遡及適用しない。

## 4. DOS由来の証拠段階

次を一つの「成功」に束ねない。

```text
CLI存在 -> provider能力 -> 呼出 -> 終了code -> artifact
        -> commit -> push -> CI -> 採用 -> merge
```

各段階は直接観測できた範囲だけを`[FACT]`または`[RESULT]`にする。ローカルgreenは公開CI greenではなく、
pushは採用やmergeではない。buddy evidence入力、他processの中断、他worktreeの変更、remote公開も別能力である。

成果候補は次で判定し、`REJECT`した枝も理由とともに保存する。

- `ADOPT`: そのまま採用候補
- `ADAPT`: 境界を直して採用候補
- `REJECT`: 今回は不採用。不存在や永久無価値とはしない
- `UNKNOWN`: 根拠不足で判断を保留

自動merge、自動公開、他processの自動中断はしない。現在のOpenFAPTAにAtlantis standalone runtime、
FAMLog永続化、自律runner、native `experiment run` adapterがあるとは扱わない。

## 5. 公開証憑

生のtranscriptや秘密を含み得る記録はlocal channelに置く。`receipts/`には公開用に浄化した次だけを置く。

- 対象、base SHA、結果SHA、時刻
- 実行したcommandと終了code
- test件数、失敗件数、artifactの有無
- push先とCI URL
- 観測できなかった事項と`UNKNOWN`

公開後はremote SHAとCIを再観測し、第2回MAGIを行う。第2回監査は第1回の意図ではなく、
実際に公開されたtreeを対象とする。

## 6. 正準リンク

Manifest、MAGI Skill、DOS実験、PITETO、KUMA800の固定URLは
[`references/source-map.json`](../../references/source-map.json)を正本とする。
構造だけを次で検査できる。

```console
python3 scripts/validate_source_map.py
```

この検査はリンク先本文の正しさ、現在性、ネットワーク到達性を証明しない。
