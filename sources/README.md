# sources/

第三方 skill 的原始檔，只存在本機，**不 commit**（見 `docs/decisions/0004-授權與第三方內容.md`）。

抓取或更新：

```
python scripts/fetch_sources.py            # 全部
python scripts/fetch_sources.py pstack     # 指定一套
```

來源、固定的 commit 與授權設定在 `scripts/sources.json`。
