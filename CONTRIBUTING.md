# Contributing Guide

Thank you for considering contributing to the Maya PySide Template Window project.
This document defines the code style, operations, and workflow rules.

[日本語版](docs/CONTRIBUTING.ja.md)

## 0. Development Environment Setup

### Prerequisites

- Maya 2022 or later
- VS Code (recommended)

### VS Code Extensions

When you clone the project and open it in VS Code, the following extensions will be automatically recommended for installation:

- **Python** (ms-python.python) - Python language support, debugging, IntelliSense
- **Black Formatter** (ms-python.black-formatter) - Automatic code formatting
- **isort** (ms-python.isort) - Import statement organization and sorting

Please install them from the notification that appears in the bottom right.

### Auto-formatting

- **Auto-run on save**: Black + isort will run automatically with `Ctrl + S`
- **Unified style**: `.vscode/settings.json` ensures the same code style across the team
- **PEP 8 compliance**: Automatic organization following Python's standard style guide

## 1. Branch Management and Commits

### Branch Management
- Create a working branch before development
- Branch names are flexible (descriptive names are recommended)

### Commits
- Aim for one commit per change
- Write commit messages that clearly describe what was done
- Example:
  ```
  Fix UI button click handling

  Resolved issue where window wouldn't close when button was pressed
  ```

## 2. Versioning and CHANGELOG

**Note: Version management and CHANGELOG updates are handled by repository maintainers.**
Contributors don't need to worry about:

- Version number updates
- CHANGELOG entries
- Release work

Focus on code improvements and feature additions, and maintainers will handle proper versioning and documentation updates at release time.

## 3. Import Conventions

**isort handles this automatically.**
Saving with `Ctrl + S` will automatically organize imports in the proper order, so no manual attention is needed.

Reference (automatic organization by isort):
- Standard library → Third-party → Local packages order
- Alphabetical order within each group
- Appropriate blank line insertion

## 4. PySide Version Support

Due to Maya versions mixing PySide2 and PySide6, please use the following pattern:

```python
try:
    from PySide6.QtWidgets import QMainWindow
except ImportError:
    from PySide2.QtWidgets import QMainWindow
```

**Key points:**
- Try PySide6 first, then fallback to PySide2
- Catch only `ImportError` (don't use `except:` or `Exception`)
- Write only the necessary parts for both, avoiding code duplication

## 5. Type Annotations

- Add type annotations to function and method arguments and return values
- Add type annotations to local variables only when the type is unclear
- Avoid `Any` whenever possible

## 6. Docstrings

- Use triple quotes `"""`
- Write a brief summary in Japanese on the first line
- Add detailed explanations as needed
- Add explanations for unclear arguments, return values, or exceptions

## 7. Error Handling

- Use specific exception types (`RuntimeError`, `TypeError`, etc.)
- Include situational context in error messages

## 8. Logging

### Basic Policy

- Use Python's standard `logging` module for log output
- Use appropriate log levels (`DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`) instead of `print()`
- Utilize the package-provided `setup_logging()` function

### Logging Configuration Usage

**Package Level:**
```python
# Use the package's setup_logging function (recommended)
from pyside_template_window import setup_logging
import logging

# Development/debugging (DEBUG level)
debug_logger = setup_logging(logging.DEBUG)
```

**Module Level:**
```python
# Define logger as a global variable at the top of each module
import logging

logger = logging.getLogger(__name__)

# Use logger within functions or classes
def some_function():
    logger.info('Processing started')
    logger.debug('Detailed processing information')
```

**Project Examples:**
- `window.py`: Already defined with `logger = logging.getLogger(__name__)`
- `app/main.py`: Already defined with `logger = logging.getLogger(__name__)`
- `app/restart.py`: Already defined with `logger = logging.getLogger(__name__)`

**Usage Steps:**
1. **Configuration**: Set log level with package's `setup_logging()`
2. **Output**: Use each module's global `logger` variable for log output

### Log Level Usage

| Level | Purpose | Examples |
|-------|---------|----------|
| `DEBUG` | Development/debugging info | Variable values, detailed processing steps |
| `INFO` | General processing info (Maya default) | Process start/end, user operations |
| `WARNING` | Warnings (processing continues) | Deprecated feature usage, configuration issues |
| `ERROR` | Errors (processing fails) | Exception occurrence, file read failures |
| `CRITICAL` | Critical errors | Application shutdown level |

### Implementation Example

**Current project usage example:**
```python
# Actual code example from window.py
logger = logging.getLogger(__name__)

def _print_hello_world(self) -> None:
    """Output dummy message"""
    logger.info('Hello, World!')  # ← Actual log output
```

### Development Best Practices

1. **Development start**: Test with Maya's default (INFO level)
2. **When debugging needed**: Add `setup_logging(logging.DEBUG)` to enable detailed info
3. **Before production release**: Remove added `setup_logging(logging.DEBUG)` code

**Important**: Always remove debug `setup_logging(logging.DEBUG)` calls before committing.

## 9. UI Construction

- In `_init_ui()`, only perform initial widget creation and signal connections
- If it becomes complex, separate into helper methods or other modules

## 10. Reload / Development Workflow

- Hot reload uses `importlib.reload()` in `app/restart.py`
- When adding new modules, add reload lines to the same file
- Avoid maintaining long-term state at module top level (breaks on reload)

## 11. Multi-language Documentation

- Keep README/CHANGELOG structure the same across all languages
- When adding sections, update all language versions in the same commit
- Don't translate API names, only translate explanations

## 12. File Structure and Naming

- Use `snake_case` for module names, `PascalCase` for class names, `UPPER_CASE` for constants
- Keep package root simple, place extensions in `app/` or new sub-packages

## 13. Performance

- Avoid premature optimization
- When needed, profile first and make evidence-based improvements

## 14. Testing (Future Plans)

- Planning to introduce `tests/` + pytest
- Test targets: Pointer validation / WorkspaceControl lifecycle / Version and CHANGELOG consistency

## 15. License / Attribution

- Add MIT headers to new files as needed
- When referencing external code, verify and document license compatibility and attribution

## 16. Pull Request Checklist

Please verify the following before submission:

- [ ] Follows import and PySide writing conventions
- [ ] Type annotations are properly written (no unnecessary `Any`)
- [ ] Docstrings added/updated
- [ ] For user-facing changes, README/CHANGELOG (all languages) updated
- [ ] No generated files or cache included
- [ ] Basic functionality tested on supported Maya versions

**Note: Version updates are handled by maintainers, so PR authors don't need to worry about this.**

## 17. Quick Reference

| Item | Rule |
|------|------|
| Imports | Auto-organized (isort) / PySide uses try-except |
| Fallback | `try/except ImportError` only |
| Type Annotations | Add to functions/methods / NewType for opaque values |
| Logging | Standard logging module / don't use print |
| Errors | Specific exceptions + clear messages |
| UI | Keep `_init_ui()` simple / separate when complex |
| Documentation | Multi-language sync / don't translate API names |
| Versioning | Maintainer updates (contributors don't need to) |
| Reload | Add new modules to restart script |

## 18. String Quote Policy

### Basic Policy
This project uses **single quotes `'...'` as the default** for Python string literals. This follows the common practice in public Maya repositories (e.g., ryusas/maya_rotationDriver, DreamWall-Animation/dwpicker, ShikouYamaue/SIWeightEditor) and reduces escaping complexity when embedding MEL code.

### Rules
- Regular strings: `'example'`
- UI display/logs/exception messages: Use single quotes directly (English/Japanese/Chinese)
- MEL embedded strings (passed to `mel.eval()`): Required single quotes outside (minimize internal `"` escaping)
- Docstrings: Use conventional triple double quotes `"""`
- Special cases with many internal single quotes making escaping complex: Double quotes permitted (e.g., `"It's user's tool"` for better readability)

### MEL String Examples
```python
mel.eval('window -title "My Tool" myToolWin;')
mel.eval(f'window -title "{tool_title}" {tool_id}Win;')
```

When embedding user input, apply minimal sanitization:
```python
def mel_quote(s: str) -> str:
  return s.replace('\\', '\\\\').replace('"', '\\"')

title = mel_quote(user_title)
mel.eval(f'window -title "{title}" myToolWin;')
```

### Exceptional Double Quote Cases
1. Translation text or long text with heavy single quote usage affecting readability
2. Temporary Black introduction for formatting alignment during PR transition

In such cases, add a one-line "reason comment" in review:
```python
error_msg = "Using double quotes due to heavy single quote usage in user input"  # quote policy exception
```

### Automation
For future quote checking with flake8-quotes or similar:
```
inline-quotes = '
multiline-quotes = "
docstring-quotes = "
```

---
Improvement suggestions welcome. Please submit PRs to the `docs/contributing` branch or this file.
