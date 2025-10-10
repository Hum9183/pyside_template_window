# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/).

[Japanese Version](CHANGELOG.md) | [中文版](CHANGELOG_CN.md)

## [Unreleased]

## [1.0.0] - 2025-10-10

### Added
- Initial release of Maya PySide template window project
- Dockable and restorable window template using WorkspaceControl
- Maya 2022-2026 support with automatic PySide6/PySide2 switching
- Type-safe Maya pointer management system (`MayaPointer` NewType)
- Hot reload functionality for efficient development
- Advanced type hints using `TypeVar` and `Type[T]`
- Circular import prevention design with `_metadata.py`
- Automatic restore script generation using `inspect.getsource()`
- Instance management with garbage collection protection
- Robust error handling with contextual error messages
- Comprehensive Japanese documentation
- English documentation support
- Chinese documentation support
- Released under MIT License
- Complete API clarification through `__all__` exports
