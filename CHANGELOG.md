# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/).

[日本語版](docs/CHANGELOG.ja.md)

## [Unreleased]

## [1.2.0] - 2025-10-22

### Changed
- Changed implementation to not inherit from `MayaQWidgetDockableMixin`
- Achieved equivalent functionality to the Mixin by overriding `setVisible()` to call `show()`
- Set parent widget to `None` (appropriately managed by WorkspaceControl)
- Reorganized logging output and added debug logs to key methods
- Simplified error handling (due to stabilized core functionality)
- Reorganized documentation, separating implementation details from design philosophy

### Added
- Added comments to all entry point files (start.py, restart.py, restore.py)

### Fixed
- Fixed issue where window title was not updated during restore

### Improved
- Enhanced encapsulation: WorkspaceControl processing is completely hidden within the class
- More robust implementation leveraging Qt virtual method overrides
- Improved code readability and maintainability

## [1.1.2] - 2025-10-14

### Changed
- Improved function naming
- Refactored workspace control attachment logic into reusable utility functions

### Fixed
- Fixed terminology consistency and language navigation links

## [1.1.1] - 2025-10-12

### Fixed
- Fixed broken links in multilingual README files

## [1.1.0] - 2025-10-12

### Added
- VS Code development environment auto-configuration (`.vscode/extensions.json`, `.vscode/settings.json`)
- Recommended settings for Python, Black, and isort extensions
- Package-level logging configuration functionality (`setup_logging()`)
- Systematic organization of multi-language documentation (`docs/` folder structure)
- Japanese contribution guide (`docs/CONTRIBUTING.ja.md`)
- English contribution guide (`CONTRIBUTING.md`)

### Changed
- Migration from `print()` statements to Python `logging` module
- Improved documentation structure (multi-language support in `docs/` folder)
- Auto-formatting configuration for enhanced code quality

### Improved
- Enhanced developer experience (VS Code environment auto-setup)
- Streamlined contributor guidelines
- Clarified project structure and documentation synchronization

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
