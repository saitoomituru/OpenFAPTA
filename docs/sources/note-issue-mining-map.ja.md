# 公開NoteとOpenFAPTA Issueのマイニング対応表

観測時点: 2026-08-29

対象: [ふさもふ公開Note](https://note.com/fusamofu326)とOpenFAPTA Issue #1〜#6

## この文書の証拠資格

`[FACT]` 公開プロフィール一覧APIを9ページ巡回し、公開記事51件を観測した。そのうちIssue #1〜#6と
関係が強い14件は、記事ページの要約表示ではなく公開本文APIの`body`まで取得して読んだ。

この文書はNote本文の複製ではない。原稿の入口を失わないための要約、正準URL、公開日時、
取得時fingerprintを保存する索引バックアップである。fingerprintは
[`references/note-mining-index.json`](../../references/note-mining-index.json)に置く。

次の三段を混ぜない。

- `直接`: 原稿本文に対応する命題や事例がある
- `合成推論`: 複数原稿の命題を接続するとIssueへ到達できる
- `Issue固有`: 型、enum、数式、fixture、受入条件としてGitHub上で初めて工学化された

Noteは著者の思想・提案・実験談を確認する一次資料だが、記事内の科学・歴史・経済上の全主張を
外部検証済みにするものではない。

## Issue対応

### [Issue #1 ActivationStateをBarrier診断へ分解する](https://github.com/saitoomituru/OpenFAPTA/issues/1)

- `直接`: 「ガラクタ」PCが物理的には存在し、再接続後にAI研究設備として動く実例は、物理不存在と
  transformer・維持・用途の欠落を同一視できないことを示す。
- `合成推論`: FAPTAの多様性資源論と、マリオカート論の物理法則・制度・再参加経路の区別から、
  単一`BLOCKED`では停止位置を失うと読める。
- `Issue固有`: `ActivationBarrier`集合、各enum名、後方互換方針、unit testはIssueで新設された。

### [Issue #2 access_permissionを物理・法・制度・経済アクセスへ分離する](https://github.com/saitoomituru/OpenFAPTA/issues/2)

- `直接`: 地方に残る機材・知識・土地性と、都市・クラウド・制度側のアクセス経路が別であること、
  投資規制や信用配分が新規参加者の障壁になり得ることが複数原稿にある。
- `合成推論`: 「資源がない」と「権利・制度・価格回路から到達できない」を分けるIssue命題は導ける。
- `Issue固有`: `physical / legal / institutional / economic`の四分割と三値型はGitHub側の工学化である。

### [Issue #3 ExplorationCapacityを資源としてモデル化する](https://github.com/saitoomituru/OpenFAPTA/issues/3)

- `直接`: マリオカート論は競争結果より再試行機会の供給を重視する。DOS記事はtoken、時間、共有文脈、
  既存資源探索が到達可能な仕事を変える実働例を扱う。旧機材記事は保有機材とlocal knowledgeを示す。
- `合成推論`: FIAT所得だけでなく、未知へ試行を飛ばせる回数と観測channelも資源だと導ける。
- `Issue固有`: `ExplorationCapacity`のfield群と`RESOURCE_WAIT`判定はIssueで新設された。

### [Issue #4 ResourceCandidateをUseContext依存で評価する](https://github.com/saitoomituru/OpenFAPTA/issues/4)

- `直接`: 同じ旧式PCが廃棄候補にもlocal AI研究設備にもなる記事は、対象単体に資源価値が固定されない
  反例になっている。FAPTA原稿も評価軸・実装を政治主体へ委ね、単一scoreを前提にしない。
- `合成推論`: エッジとSaaSを優劣ではなく役割配置として読む原稿も、Worldごとの戻り値を支持する。
- `Issue固有`: `ResourceCandidate × UseContext` API、空き家fixture、必要fieldはIssueで新設された。

### [Issue #5 循環資源・再利用サイクルのトイモデル](https://github.com/saitoomituru/OpenFAPTA/issues/5)

- `直接`: 旧機材を再利用して研究設備へ戻した実例、贈与・循環・非蓄積の経済、狩場・農作の
  回復周期と周回管理が原稿にある。
- `合成推論`: 初期stockだけではlifetimeの利用可能量を表せず、回収・変換・周期を別に観測すべきと導ける。
- `Issue固有`: `RAW_RESOURCE -> ... -> SECONDARY_RESOURCE`、等比級数、回収率・損失・最大cycleの
  決定論モデルはIssueで新設された。原稿が100%循環や無限資源を実証したわけではない。

### [Issue #6 Commodity ValueとAgency-Embedded Valueを分離する](https://github.com/saitoomituru/OpenFAPTA/issues/6)

- `直接`: creditとvalueの非同一、名前を持つ人のcommit、意味・意図・文脈・Agency、工学の人間接続、
  数値へ還元できない体験・意味、複数主体の文脈を扱う原稿群がある。
- `合成推論`: commodity機能が代替されても、信頼・関係・美意識・土地性・継続理由まで消えたとは
  判定できない。意味が継続行動を介して後段結果へ影響する経路も仮説として組める。
- `Issue固有`: 医療・美容・農業・製造・ITの具体例、Value scope一覧、`ContinuationEffect`、
  `Q(ψ, ∇φ, λ, Agency, World)`はIssueで明示された工学拡張である。

## 関連Note要約

### 経済設計三部作

- [第1回「この地球、いつの間にPvPになってね？」](https://note.com/fusamofu326/n/nbc4d3e3d266d)
  有限資源と希少性を対人奪取へ接続した貨幣設計を、PvEからPvPへの変質として読む。未来potentialを測る
  別の価値系が必要だという入口。
- [第2回「貨幣は情報の死体である」](https://note.com/fusamofu326/n/na0f3f8a3bd2d)
  FIATを過去の因果記録、Mind Pointを未観測の未来potential・共鳴・流動を扱う提案として分ける。
  地方知や未商品化の着想が会計上ゼロでも価値不存在ではないとする。
- [第3回「たった一行でSDGsを半分殴り倒す」](https://note.com/fusamofu326/n/nc5bd7119cf8e)
  FAPTAを価値発生前のfactor設計として提示し、多様性・探索余地・地域文化をcostではなくresource候補へ
  置き直す。共通protocolと多様な実装、単一指標最適化のSPOFを論じる。

### 資源、循環、競争機会

- [12年前のガラクタで、AI研究所を作った話](https://note.com/fusamofu326/n/n9698c6259109)
  廃棄候補に見える旧式PCをlocal AI基盤へ再接続した実験談。同じ物理対象の価値がtransformer、用途、
  場所、privacy要件によって変わるため、Issue #1、#4、#5の最も直接的な反例資料になる。
- [マリオカートツアーのゲーム理論で見る競争社会と福祉講座](https://note.com/fusamofu326/n/n355d83cfd36f)
  結果平等ではなく、再試行・再参加・アイテム取得機会を供給し続ける設計を論じる。競争機会、資源総量、
  制度的封鎖、リスポーン能力を別々に見る入口。
- [天岩戸が毎日起きる家から見る世界史](https://note.com/fusamofu326/n/n1bda68a016e2)
  贈与・循環・非蓄積を現代OSSへ写像し、閉じた市場、信用、契約、制度維持costを扱う。循環を貧困や
  無価値へ還元しない文化・関係面の資料。
- [第1講「数とは何か——宇宙記述言語の系譜」](https://note.com/fusamofu326/n/nfc160cfbd0d2)
  狩場・農作・季節の周期管理、身体知、土地との関係を、現代数理との翻訳可能性を保ちながら扱う。
  記述されていない知識を不存在とせず、周期資源の観測候補を出す。

### 探索capacityと役割配置

- [SphereOS-Atlantis DOSが引き出すAIエンジニアリング](https://note.com/fusamofu326/n/na6f83c902df2)
  token予算、作業時間、共有文脈、checkpoint、既存資源探索を通じ、同じ財布でも到達可能な仕事を変える
  実験報告。実装状態の正確な資格はAtlantis側receiptを優先する。
- [投資を煽るな、が生む沼](https://note.com/fusamofu326/n/nd35d4e542c0f)
  未知riskを消す装置としてのpoolを焼くと、riskが弱い末端へ濃縮するという仮説。資本、信用、制度能力、
  退出可能性が探索参加条件を変える資料。
- [エッジAI時代のSaaS AIの優位性について](https://note.com/fusamofu326/n/n7909c6ad3d27)
  edgeとSaaSを勝敗ではなく異なる責務・観測規模・責任routingとして配置する。同一技術の価値が
  UseContextと主体配置で変わる例。

### Agency、意味、人間接続

- [creditとvalueと無限責任から見る「人間とは？」](https://note.com/fusamofu326/n/ne5c253d54c90)
  creditとvalue、主体と観測者、個人のcommitと抽象構造を分ける。意味・意図・文脈・Agencyを別主体が
  展開するFoldとして扱い、人格や来歴を匿名commodityへ潰さない。
- [言霊と形而上学を軽視する工学コミュニケーション](https://note.com/fusamofu326/n/ne6a6c69179b9)
  工学は人間へ接続した時点で、言葉、UI、誤読、体験、責任配置まで射程に入るとする。機能達成だけを
  total valueとしないIssue #6の直接資料。
- [最強単一モデルでクソUXより](https://note.com/fusamofu326/n/n480909aaedfc)
  単一AIではなく、人間・複数agent・身体・環境・actuatorの相互作用と文脈保持を単位にする。
  一人称やAgencyを組織riskの一般論へ誤変換する危険を扱う。
- [「量子」という言葉は盗まれた](https://note.com/fusamofu326/n/nccf10b72d6a0)
  物理量子、量子inspired、情報子を分け、形而上学的な意味や主観を物理実証へ偽装せず工学対象として
  保持する境界を提案する。

## バックアップ方針

現在実装したのは`Level 1: metadata + summary + fingerprint`である。

```text
Level 0  元URLだけ                         脆い
Level 1  metadata + summary + fingerprint  今回実装
Level 2  著者export原稿 + media台帳         NOT IMPLEMENTED
Level 3  render snapshot + provenance       NOT IMPLEMENTED
```

全文を保存するなら、scraping結果より著者本人のexport原稿を優先する。原稿本文、画像、埋込、コメント、
公開後更新を別artifactにし、取得日時、原URL、hash、公開可否、CC-BY適用範囲を明示する必要がある。
Note上の公開がOpenFAPTAへのCC-BY再許諾を自動的に意味するとは扱わない。

## UNKNOWN

- 公開51件すべてをOpenFAPTAへ保存すべきか。今回の選定はIssue #1〜#6向け14件に限定した
- Noteの将来API仕様とURL永続性
- 著者exportに本文・画像・埋込がどの形式で含まれるか
- 記事更新後にfingerprint差分をどうレビューし、要約へ反映するか
