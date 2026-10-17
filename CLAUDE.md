# SkillCustomizer

這個 repo 用來建立一套**個人 workflow 的 skill-set**。第一個領域是寫程式（Python、Claude Code、GitHub Issues/PR），之後可能延伸到其他領域。

每次 session 開始時，先讀本檔，再讀 `docs/sessions/` 最新的一則紀錄。

## 互動約定

- **語言**：討論、文件、決策紀錄用繁體中文；`skills/` 裡的 skill 本體用英文（ADR 0003）。
- **一個 session 一個目標**：開始時先確認目標；結束時在 `docs/sessions/YYYY-MM-DD.md` 寫下結論、決定和下一步。
- **決定權分層**：
  - 結構性決定（方法、repo 架構、面向清單、各面向的立場、skill 架構）：Claude 提出 2–3 個選項和取捨，使用者拍板。
  - 小事（措辭、檔案細節）：Claude 直接處理，事後說明怎麼決定的。
  - 刪除或覆寫使用者的內容：一律先問。
- **使用者的四種介入**：決定、確認、核准、提供素材。各階段用哪一種，見 `docs/method.md`。
- **先討論，再動手**：先給大綱或選項，使用者同意後才寫完整內容。
- **決定要留紀錄**：結構性決定寫成 ADR，放在 `docs/decisions/NNNN-標題.md`，格式為「背景／選項／決定／原因」。

## 方法摘要

詳細內容見 `docs/method.md`。

0. 選來源 → 1. 抽面向 → 2. 定立場 → 3. 設計 skill 架構 → 4. 撰寫 → 5. 試用 → 6. 修正

- 既有的 skill set **只在收錄時完整讀一次**，整理進面向庫 `docs/dimensions.md` 之後，第 1–3 階段只用面向庫。
- 原始檔放在 `sources/`，記下固定的 commit，作為追溯用的存檔。只有在第 4 階段要借用具體寫法，或面向庫的摘要不足以做決定時，才回頭查原文。

## 目錄結構

```
CLAUDE.md            互動約定與 repo 規則（本檔）
docs/method.md       建立 workflow 的方法
docs/dimensions.md   面向庫：各面向、各來源的立場、使用者的立場
docs/sources.md      來源清單：網址、作者、授權、固定的 commit、收錄狀態
docs/decisions/      ADR
docs/sessions/       每次 session 的紀錄
sources/<來源>/      原始 skill 存檔，唯讀，不修改
skills/<領域>/       使用者自己的 skill-set
evals/               skill 的測試
```

## 規則

- `sources/` 內的檔案不修改；更新時重新抓取，並在 `docs/sources.md` 更新 commit。
- 面向庫裡的每個立場都要標出處（來源、skill 名稱、檔案路徑），讓人能追溯回原文。
- 寫進 `skills/` 的每個 skill，都要在檔案中註明參考了哪些面向和來源。
- Claude 自己的推論與來源原文要分開寫，推論需標明。

## 未決事項

- GitHub repo：使用者已決定推到 GitHub，等連結 GitHub 帳號後建立。名稱與公開／私人待確認（Claude 建議私人：`sources/` 會存放 source-available 的檔案）。
