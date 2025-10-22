# 変更ログ

このプロジェクトの目立った変更はすべてこのファイルに記録されます。

フォーマットは[Keep a Changelog](https://keepachangelog.com/ja/1.0.0/)に準拠しており、
このプロジェクトは[Semantic Versioning](http://semver.org/)に基づいています。

[English Version](../CHANGELOG.md)

## [Unreleased]

## [1.2.0] - 2025-10-22

### Changed
- `MayaQWidgetDockableMixin` を継承しない実装に変更
- `setVisible()` をオーバーライドして `show()` を呼ぶパターンでMixinと同等の機能を実現
- 親ウィジェットを `None` に設定（WorkspaceControl が適切に管理）
- ログ出力を整理し、主要メソッドに debug ログを追加
- エラーハンドリングを簡素化（基本動作が安定したため）
- ドキュメントを整理し、実装詳細と設計思想を分離

### Added
- すべてのエントリーポイントファイル（start.py, restart.py, restore.py）にコメントを追加

### Fixed
- restore 時にウィンドウタイトルが更新されない問題を修正

### Improved
- カプセル化の向上：WorkspaceControl の処理を完全にクラス内部に隠蔽
- Qt の仮想メソッドのオーバーライドを活用した、より堅牢な実装
- コードの可読性向上とメンテナンス性の改善

## [1.1.2] - 2025-10-14

### Changed
- 関数名の改善
- WorkspaceControl アタッチロジックを再利用可能なユーティリティ関数にリファクタリング

### Fixed
- ドキュメントの用語統一と言語間リンク修正

## [1.1.1] - 2025-10-12

### Fixed
- 多言語READMEファイルのリンク切れを修正


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
