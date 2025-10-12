# PySide Template Window for Maya

Maya用のPySideテンプレートウィンドウプロジェクトです。WorkspaceControlを使用したドッキング可能かつ復元可能なウィンドウのテンプレートです。

[English Version](../README.md) | [中文版](README.zh-CN.md)

## 特徴

- ✅ **WorkspaceControl対応**: Mayaのワークスペースにドッキング可能です
- ✅ **復元機能**: Maya起動時に自動で復元します
- ✅ **リロード機能**: 素早いリロードで開発を効率化します

## 動作環境

- Maya 2022
- Maya 2023
- Maya 2024
- Maya 2025
- Maya 2026

## インストール

### ファイル配置

Mayaのscriptsフォルダーにプロジェクトを配置してください。
パスが通っている場所ならどこでもOKです。

```
~/Documents/maya/scripts/
└── pyside_template_window/
    ├── __init__.py
    ├── _metadata.py
    ├── window.py
    ├── utils.py
    └── app/
        ├── __init__.py
        ├── main.py
        ├── start.py
        ├── restart.py
        └── restore.py
```

## 使用方法

### 初回起動

start.pyのテキストをMayaのスクリプトエディターで実行してください。

### 開発時の再起動

ウィンドウのDevメニューのRestartを押下してください。
もしくはrestart.pyのテキストをスクリプトエディターで実行してください。
これによりリロードされた状態で起動します。

### Maya起動時の自動復元

Maya起動時にウィンドウが自動的に復元されます。
restore.pyがそれにあたりますがこれはスクリプトエディターで実行するものではないため注意してください。

## プロジェクト構造

```
pyside_template_window/
├── __init__.py          # パッケージ初期化
├── _metadata.py         # パッケージメタデータ（バージョン・作者情報）
├── window.py            # メインウィンドウクラス
├── utils.py             # ユーティリティ関数
├── app/
│   ├── __init__.py      # appパッケージ初期化
│   ├── main.py          # 起動のコア機能（start/restart/restore）
│   ├── start.py         # 初回起動
│   ├── restart.py       # 再起動
│   └── restore.py       # 復元
├── README.md            # このファイル（日本語ドキュメント）
├── README.en-US.md      # 英語版ドキュメント
├── README.zh-CN.md      # 中国語版ドキュメント
├── CHANGELOG.md         # 変更ログ（日本語）
├── CHANGELOG.en-US.md   # 変更ログ（英語）
├── CHANGELOG.zh-CN.md   # 変更ログ（中国語）
└── LICENSE              # ライセンス情報
```

## API リファレンス

### PySideTemplateWindow クラス

メインのウィンドウクラスです。

**通常の使用では直接インスタンス化する必要はありません。** app/main.py内で内部的にインスタンス化するのが基本です。

```python
# app/main.py での使用例
from ..window import PySideTemplateWindow

# インスタンス作成
window = PySideTemplateWindow()
window.show()
```

#### 主要メソッド

| メソッド | 説明 |
|----------|------|
| `show()` | ウィンドウを表示します |
| `set_instance(instance)` | インスタンスを GC から保護します。restore 時に呼びます |

#### クラス変数

| 変数 | 説明 |
|------|------|
| `NAME` | ウィンドウ名 (`'PySideTemplate'`) |
| `WORKSPACE_CONTROL_NAME` | WorkspaceControl 名 (`'PySideTemplateWorkspaceControl'`) |
| `_TITLE` | ウィンドウタイトル (`'PySide Template v1.0.1'`) |

### app.main モジュール

| 関数 | 説明 |
|------|------|
| `start()` | 既存ウィンドウがある場合は再表示し、ない場合は新規作成します |
| `restart()` | 既存の WorkspaceControl を削除して再生成します |
| `restore()` | Maya 起動時やワークスペース切り替え時に自動実行されます |

### utils モジュール

Maya 関連の共通機能をまとめたユーティリティモジュールです。

| 関数/型 | 説明 |
|---------|------|
| `MayaPointer` | Maya UI ポインタの型安全な表現 |
| `is_valid_maya_pointer()` | Maya ポインタの有効性をチェックします |
| `get_maya_control_pointer()` | 型安全な Maya コントロールポインタを取得します |
| `safe_wrap_instance()` | 型安全な wrapInstance を実行します |
| `add_widget_to_maya_layout()` | 型安全な Maya レイアウト追加を行います |

### ロギング設定

開発時のロギング設定を行います。Maya では通常 INFO レベルがデフォルトです。

| 関数 | 説明 |
|------|------|
| `setup_logging(level)` | パッケージ用のロギング設定を行います |

```python
# デバッグ情報を出力したい場合
from pyside_template_window import setup_logging
import logging

setup_logging(logging.DEBUG)  # デバッグ情報を表示
```

## カスタマイズ
このパッケージを流用して実際のツールを作る場合のカスタマイズ方法について説明します。

### 1. パッケージ名の変更

ツールの名前に応じて、パッケージ名（フォルダ名）を変更してください。

```
# 変更前
~/Documents/maya/scripts/
└── pyside_template_window/

# 変更後（例）
~/Documents/maya/scripts/
└── your_custom_tool/
```

**合わせての変更箇所**:
- `app/main.py`, `app/start.py`, `app/restart.py`, `app/restore.py`内のimport文と関数名

### 2. クラス名の変更

クラス名も変更してください。

```python
# 変更前
class PySideTemplateWindow(MayaQWidgetDockableMixin, QMainWindow):
    ...

# 変更後（例）
class YourCustomWindow(MayaQWidgetDockableMixin, QMainWindow):
    ...
```

**合わせての変更箇所**:
- `window.py`の NAME、_TITLE 等のクラス変数
- `app/main.py`内の参照

### 3. UIのカスタマイズ

`_init_ui()` メソッドを編集してUIを変更してください。

```python
# window.py
def _init_ui(self) -> None:
    # ここにカスタムUIを実装
    ...
```

## 開発のベストプラクティス

### 開発ワークフロー

1. コードを編集
2. Maya内で以下のいずれかを実行:
   - ウィンドウのDevメニューの「Restart」を押下
   - `restart.py`の内容をスクリプトエディターにコピー&ペーストして実行
3. 変更が即座に反映される

このフローを取れば素早く結果を確認できスムーズに開発を進めることができます。

## よくある問題と解決法

### Q: リロードが効かない
A: ウィンドウのDevメニューから「Restart」を実行するか、`restart.py`の内容をスクリプトエディターにコピー&ペーストして実行してください。ただし、ここでのリロードはimportlib.reload()を使ったシンプルなものなので複雑なファイル構成のリロードには対応していません。

### Q: 初回起動でもリロードしたい
A: `start.py`の代わりに`restart.py`の内容をスクリプトエディターで実行してください。初回起動でリロードすること自体には全く問題はありません。

### Q: ウィンドウを☓で閉じてもインスタンスが削除されていない
A: PySideの仕様です。`start.py`の内容を再度スクリプトエディターで実行すれば再表示されます。

### Q: コードを編集していたら復元が機能しなくなった
A: 復元は非常に繊細な仕組みで動いているため一度元のコードに戻した上で慎重に編集することをおすすめします。

### Q: Maya2020でエラーが出た
A: Maya2020以前には対応していません。

## 開発環境

開発に参加される場合は、[CONTRIBUTING.md](CONTRIBUTING.md)をご覧ください。

## ライセンス

このプロジェクトはMITライセンスの下で公開されています。詳細は[LICENSE](LICENSE)ファイルをご覧ください。

