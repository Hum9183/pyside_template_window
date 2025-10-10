# 变更日志

此项目的所有重要更改都将记录在此文件中。

格式基于 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.0.0/)，
此项目遵循 [语义化版本](https://semver.org/lang/zh-CN/)。

[日本語版](CHANGELOG.md) | [English Version](CHANGELOG_EN.md)

## [未发布]

## [1.0.0] - 2025-10-10

### 新增
- Maya PySide 模板窗口项目的初始发布
- 使用 WorkspaceControl 的可停靠和可还原窗口模板
- Maya 2022-2026 支持，自动 PySide6/PySide2 切换
- 类型安全的 Maya 指针管理系统（`MayaPointer` NewType）
- 用于高效开发的热重载功能
- 使用 `TypeVar` 和 `Type[T]` 的高级类型提示
- 使用 `_metadata.py` 的循环导入预防设计
- 使用 `inspect.getsource()` 的自动还原脚本生成
- 带垃圾回收保护的实例管理
- 强大的错误处理和上下文错误消息
- 全面的日文文档
- 英文文档支持
- 中文文档支持
- 根据 MIT 许可证发布
- 通过 `__all__` 导出完成 API 明确化
