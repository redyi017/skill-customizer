# 面向庫

> **版本 v0（2026-10-17）**：只根據目錄頁與說明頁整理，還不是完整閱讀的結果。四套來源都要經過完整收錄（見 `docs/method.md`）才能當作定立場的依據。標「待驗證」的是 Claude 的推論，尚未對照原文確認。

類別：**通用** = 換領域仍適用；**領域** = 寫程式特有。

## 總覽

來源縮寫：**Matt** = Matt Pocock skills；**pstack**；**A-skills** = Anthropic skills；**CC** = Anthropic Claude Code plugins。CC 欄只根據各 plugin 的說明整理。

| # | 面向 | 類別 | Matt | pstack | A-skills | CC | 我的立場 |
|---|---|---|---|---|---|---|---|
| 1 | 角色與決定權 | 通用 | 使用者是技術主管，agent 先追問再執行 | agent 是有原則的資深工程師，自主判斷 | agent 是帶著工具箱的專門技術者，聽目標做事 | 多種並存：`learning-output-style` 在決策點請使用者自己寫程式；`ralph-wiggum` 讓 agent 不停迴圈直到完成 | 待定 |
| 2 | 進入與觸發 | 通用 | 多個 slash command，另有 `/ask-matt` 幫忙選 | 一個常駐的 mode skill 自動分派 playbook | 各 skill 獨立，靠 description 自動觸發，沒有分派者 | slash command 為主，加上自動觸發的 hook | 待定 |
| 3 | 規劃深度 | 領域 | 重：grill → spec → tickets | 輕：不寫規劃 skill，用 plan mode | 一般不涉及；`doc-coauthoring` 有分階段的流程 | `feature-dev`：探索 → 架構設計 → 實作 → 品質審查（待驗證） | 待定 |
| 4 | 需求釐清 | 通用 | 訪談式追問（`/grilling`） | 依 playbook 的步驟走 | `skill-creator` 會先訪談意圖（待驗證） | `feature-dev` 有釐清問題的步驟（待驗證） | 待定 |
| 5 | 工作切分方式 | 領域 | 依開發**階段** | 依**任務類型**（bug、perf、refactor…） | 依**能力或產出格式**（docx、MCP、網頁測試…） | 依**單一工作環節**（commit、PR review、安全檢查） | 待定 |
| 6 | 產出物與記錄 | 通用 | spec、tickets、領域詞彙表 | todo list | 具體檔案；`skill-creator` 產出 eval 結果 | commit、PR、review 意見 | 待定 |
| 7 | 實作紀律 | 領域 | TDD、deep module | TDD、先刪再加、不寫註解、unslop | 各工具的最佳做法，附帶可執行的腳本 | `security-guidance` 在編輯時提出安全警告；`hookify` 用 hook 擋下不想要的行為 | 待定 |
| 8 | 驗證方式 | 領域 | 對照標準與 spec 做 code review | 證明它真的能跑 | `webapp-testing` 用 Playwright 實測；`skill-creator` 跑 eval | `code-review`：多個專門 agent 審查並給信心分數；`pr-review-toolkit` 分項審查（測試、錯誤處理、型別…） | 待定 |
| 9 | 委派與多 agent | 領域 | `/implement-spec` 用平行 subagent | arena、swarm 多模型協作；角色對應模型 | `skill-creator` 用 subagent 平行跑 eval（待驗證） | 大量使用專門 subagent（探索、架構、審查） | 待定 |
| 10 | Context 與交接 | 通用 | `/handoff` | 保護 context window（原則 skill） | 漸進載入：SKILL.md 之外的參考檔與腳本需要時才讀 | 把工作分給 subagent，主對話只拿結果（待驗證） | 待定 |
| 11 | 溝通風格 | 通用 | `/wait-what` 用白話重講 | 以使用者與維護者為對象；technical-writing | `doc-coauthoring` 讓讀者測試文件（待驗證）；`internal-comms` 用固定格式 | `explanatory-output-style` 解釋實作選擇；`learning-output-style` 教學模式 | 待定 |
| 12 | 自我改進 | 通用 | `/retro` | `reflect`；`automate-me` 從對話紀錄生成個人 skill | `skill-creator`：用 eval 迭代、最佳化 description | `hookify` 從對話模式產生 hook | 待定 |
| 13 | 每個 repo／組織的設定 | 通用 | `/setup-matt-pocock-skills` | `/setup-pstack`：推理預算、模型分工 | 把組織設定寫進 skill 本身（`brand-guidelines`、`internal-comms`） | 未見專門的設定 plugin（待驗證） | 待定 |
| 14 | Skill 的類型與顆粒度 | 通用 | **流程** skill（依階段）＋**參考** skill | **playbook**（依任務）＋**原則** skill（一條原則一個） | **能力** skill（一種工具或格式一個，附腳本） | **環節** plugin（一個工作環節一個） | 待定 |
| 15 | 執行載體 | 通用 | 以 skill 為主 | 以 skill 為主，另有 subagent | 只有 skill | skill、slash command、subagent、hook 混用；hook 能**強制**執行，不靠 agent 自覺 | 待定 |

## 各面向細節

各面向的詳細立場、出處和取捨，會在第 1 階段完整收錄時補上。格式如下：

```
### N. 面向名稱
- 定義：這個面向要回答的設計問題
- 類別：通用／領域
- 立場：
  - A（來源，skill，檔案路徑）：說明
  - B（…）：說明
- 取捨：
- 我的立場：待定（決定後連結到 ADR）
```
