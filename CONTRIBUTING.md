# Contributing Guide

Thank you for considering contributing to the Maya PySide Template Window project.

[日本語版](docs/CONTRIBUTING.ja.md)

## Development Environment

- **Maya**: 2022 or later
- **VS Code**: Recommended editor
- **Auto-formatting**: Black + isort automatically runs on save

## Basic Rules

### Branch and Commits
- Create a working branch before development
- One commit per change
- Clear and descriptive commit messages

### Code Style
- **Type Annotations**: Required for functions and methods
- **PySide Support**: `PySide6`→`PySide2` fallback pattern
- **Logging**: Use `logging` module instead of `print()`
- **Strings**: Single quotes `'...'` by default, triple double quotes `"""` for docstrings

## PR Checklist

Before submission:

- [ ] Code auto-formatted (Black + isort)
- [ ] Type annotations added
- [ ] Tested in Maya
- [ ] PR description explains the intent of code changes

## Notes

- **Version Management**: Handled by maintainers (contributors don't need to worry)
- **Documentation Updates**: Handled by maintainers (contributors don't need to worry)

---
Feel free to ask questions via Issues or PRs!
