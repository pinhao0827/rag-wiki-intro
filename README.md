# RAG 入門：讓 AI 查資料後再回答

線上教學與 Wiki：[開啟完整作業](https://pinhao0827.github.io/rag-wiki-intro/)。原始知識庫：[Wiki 索引](wiki/index.md)。

也可直接用 Chrome、Edge 或 Firefox 開啟 index.html。所有教學內容、Wiki、流程圖、執行紀錄均包含在單一檔案，可離線使用。

## 檔案分工

- index.html：15 頁教學簡報、互動案例、小測驗、Wiki、流程與反思。
- wiki/index.md：Markdown 版知識庫，含五個來源筆記與七個互連概念頁。
- AGENTS.md：本專案生成及檢查規則。
- content.json：已核對的來源、Wiki 與逐頁稿。
- raw/manifest.json：實際下載來源的固定版本、頁數、文字量與 SHA-256。
- drafts/slide-map.md：逐頁 Wiki／來源對應。
- records/discussion.md：真實需求討論摘要。
- records/run.json：原始執行與檢索比較紀錄。
- records/recheck.json：交付前重新執行的結構檢查。
- records/browser-check.md：Chrome 桌機與手機寬度下的檢查紀錄。
- scripts/：可重跑檢查與 HTML 生成程式。

## 可重跑的檢查

需 Python 3，檢查與渲染腳本只用標準函式庫，不需要 API key。

```text
python scripts/check.py
python scripts/rebuild.py
python scripts/check.py
```

驗證固定來源 PDF 的下載雜湊（需要網路，下載件放在 raw/downloads）：

```text
python scripts/verify_sources.py
```

修改內容請先改 content.json，再重建 HTML。原始 run.json 保留原先執行結果，不會因重建被偽裝成新測試。

## 範圍與限制

此為 LLM 協助編製的 Wiki 與教學 HTML，不是部署中的自主 RAG 服務。互動案例使用虛構資料與固定規則。檢索題組只有六題，不能當作一般效能評測。人工內容核對未使用獨立第二模型。下載的論文與原始擷取文字未重複打包，可由固定網址重取驗證。

繳交期限：2026/11/23 23:59，遲交至 11/24 16:00，以 COOL 頁面為準。繳交標題尚須補上本人學校、學號、系級及姓名。


## 如何繼續加入新資料

請後續 AI 先讀 AGENTS.md，為新文章追加永久來源 ID 與固定版本紀錄，再更新相關概念、雙向連結及 wiki/log.md，依需要修正逐頁稿與來源表，重建 HTML 並重新檢查。資料夾與命名規則見 AGENTS.md。

影片的完整音訊已做自動辨識，再與教師投影片及 COOL 說明核對。公開的 records/lecture-audit.json 保存方法、統計與概括核對結果；音訊與完整自動逐字稿未公開。自動辨識仍有誤字，不能等同逐字人工校對。
