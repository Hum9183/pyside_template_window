# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/).

[日本語版](docs/CHANGELOG.ja.md)

## [Unreleased]

## [1.0.1] - 2025-10-10

### Fixed
- Added multi-language documentation files in "Project Structure" section of README

## [1.0.0] - 2025-10-10

### Added
- Initial release of Maya PySide template window project
- Dockable and restorable window template using WorkspaceControl
- Maya 2022-2026 support (automatic PySide6/PySide2 switching)
- Type-safe Maya pointer management system (`MayaPointer` NewType)
- Hot reload functionality for development efficiency
- Advanced type hints using `TypeVar` and `Type[T]`
- Circular import avoidance design with `_metadata.py`
- Automatic restore script generation using `inspect.getsource()`
- Instance management with GC protection features
- Error handling with contextual error messages
- Comprehensive Japanese documentation
- English documentation support
- Chinese documentation support
- Published under MIT license
- Complete API clarification with `__all__` exports
