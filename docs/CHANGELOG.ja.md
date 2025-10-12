# 変更ログ

このプロジェクトの目立った変更はすべてこのファイルに記録されます。

フォーマットは[Keep a Changelog](https://keepachangelog.com/ja/1.0.0/)に準拠しており、
このプロジェクトは[Semantic Versioning](http://semver.org/)に基づいています。

[English Version](../CHANGELOG.md)

## [Unreleased]

## [1.1.0] - 2025-10-12

### Added
- VS Code 開発環境の自動設定（`.vscode/extensions.json`, `.vscode/settings.json`）
- Python、Black、isort 拡張機能の推奨設定
- パッケージレベルのロギング設定機能（`setup_logging()`）
- 多言語ドキュメントの体系的整理（`docs/` フォルダ構成）
- 日本語版コントリビューションガイド（`docs/CONTRIBUTING.ja.md`）
- 英語版コントリビューションガイド（`CONTRIBUTING.md`）

### Changed
- `print()` ステートメントから Python `logging` モジュールへの移行
- ドキュメント構成の改善（`docs/` フォルダでの多言語対応）
- コード品質向上のための自動フォーマット設定

### Improved
- 開発者エクスペリエンスの向上（VS Code 環境自動設定）
- コントリビューター向けガイドラインの整備
- プロジェクト構造の明確化とドキュメント同期

## [1.0.1] - 2025-10-10

### Fixed
- README の「プロジェクト構造」セクションで多言語ドキュメントファイルの記載を追加

## [1.0.0] - 2025-10-10

### Added
- Maya PySide テンプレートウィンドウプロジェクトの初回リリース
- WorkspaceControl を使用したドッキング可能・復元可能なウィンドウテンプレート
- Maya 2022-2026 対応（PySide6/PySide2 自動切り替え）
- 型安全なMayaポインタ管理システム（`MayaPointer` NewType）
- 開発効率化のためのホットリロード機能
- `TypeVar` と `Type[T]` を使用した高度な型ヒント
- `_metadata.py` による循環インポート回避設計
- `inspect.getsource()` を利用した復元スクリプト自動生成
- GC 保護機能付きインスタンス管理
- エラーハンドリングとコンテキスト付きエラーメッセージ
- 包括的な日本語ドキュメンテーション
- 英語版ドキュメンテーション対応
- 中国語版ドキュメンテーション対応
- MIT ライセンスでの公開
- 完全な `__all__` エクスポートによる API 明確化
