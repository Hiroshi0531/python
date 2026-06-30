# Python Scripts Collection

業務自動化・セキュリティ監視・情報収集を目的とした Python スクリプト集です。

## ディレクトリ構成

```
python/
├── azure functions/
│   └── send_auto_vulnerability/   # 脆弱性情報の自動メール通知 (Azure Functions)
├── send_gmail_auto/               # Gmail による一括メール送信
└── supermarket_info_get/          # スーパーマーケット店舗情報の収集
```

---

## 1. send_auto_vulnerability (Azure Functions)

JVN (Japan Vulnerability Notes) の API を定期的にポーリングし、指定製品の脆弱性情報を SendGrid 経由でメール通知する Azure Functions タイマートリガー関数です。

### 機能

- `product.txt` に列挙した製品名をもとに JVN API で製品 ID を検索
- 指定した深刻度 (low / middle / high) 以上の脆弱性情報を取得
- 指定した収集間隔 (daily / weekly / monthly) でフィルタリング
- CVSS スコア・脆弱性詳細・参照 URL を含むメールを SendGrid で送信

### 設定パラメータ (`__init__.py`)

| 変数 | 説明 | デフォルト |
|------|------|-----------|
| `SEVERITY` | 深刻度の最低閾値 (`low` / `middle` / `high`) | `middle` |
| `INTERVAL` | 収集期間 (`daily` / `weekly` / `monthly`) | `weekly` |
| `NOTIFY_SUBJECT` | メール件名 | `[CAUTION] Found Vulnerability Information` |

### 監視対象製品 (`product.txt`)

Microsoft Office 製品群・Windows・Edge・Visual Studio Code・Adobe Acrobat/Reader・kintone・7-Zip・Android など主要ソフトウェアを対象としています。

### 必要ライブラリ

```
azure-functions
python-dateutil==2.8.2
pytz==2021.3
six==1.16.0
urllib3==1.26.7
```

### デプロイ

Azure Functions (Python) としてデプロイし、`function.json` でタイマースケジュールを設定します。SendGrid の出力バインディングを使用するため、Azure Portal で SendGrid API キーの設定が必要です。

---

## 2. send_gmail_auto

`address.csv` に記載された宛先リストに対して、Gmail SMTP を使って HTML メールを一括送信するスクリプトです。

### 機能

- CSV ファイルから宛先メールアドレスと URL を読み込む
- 各宛先に URL を含む HTML メールを送信
- 送信間隔 1 秒のスロットリング

### CSV フォーマット (`address.csv`)

```csv
メールアドレス,URL
xxx@example.com,https://example.com/...
```

### 必要ライブラリ

```
pandas
```

### 使い方

```bash
pip install pandas
python gmail_send.py
```

> **注意:** スクリプト内の `gmail_account` と `gmail_password` を実際の認証情報に変更してください。パスワードは Gmail のアプリパスワードを使用することを推奨します。

---

## 3. supermarket_info_get

スーパーマーケットチェーンの店舗情報を自動収集するスクリプト群です。

### webscraping.py

`requests` + `BeautifulSoup` を使って店舗一覧ページから各店舗の情報を取得するウェブスクレイピングスクリプトです。

**必要ライブラリ**

```
requests
beautifulsoup4
```

### RPA.py

`pyautogui` を使ってブラウザを GUI 操作し、イオンの店舗一覧ページから店舗名・住所などの情報をマウス操作でコピーして CSV に書き出す RPA スクリプトです。

**必要ライブラリ**

```
pyautogui
pyperclip
```

**使い方**

```bash
pip install pyautogui pyperclip
python RPA.py
```

> **注意:** 実行環境に合わせて `mouse_b` / `mouse_a` の座標値を調整してください。

---

## 動作環境

- Python 3.8 以上
- Azure Functions (send_auto_vulnerability のみ)
- Windows 推奨 (RPA.py はウィンドウ操作を含むため)
