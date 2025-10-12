# PySide Template Window for Maya

A PySide template window project for Maya that provides dockable and restorable windows using WorkspaceControl.

[日本語版](docs/README.ja.md) | [中文版](docs/README.zh-CN.md)

## Features

- ✅ **WorkspaceControl Integration**: Seamlessly docks to Maya's workspace
- ✅ **Auto-Restore**: Automatically restores when Maya starts
- ✅ **Hot Reload**: Quick module reloading for efficient development

## Supported Versions

- Maya 2022
- Maya 2023
- Maya 2024
- Maya 2025
- Maya 2026

## Installation

### File Placement

Place the project in Maya's scripts folder or any directory in the Python path.

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

## Usage

### Initial Launch

Copy and paste the contents of `start.py` into Maya's Script Editor and execute.

### Development Restart

Click "Restart" from the window's Dev menu, or copy and paste the contents of `restart.py` into the Script Editor and execute. This reloads the modules and restarts the window.

### Auto-Restore on Maya Startup

The window automatically restores when Maya starts. The `restore.py` script handles this functionality (it's not intended for manual execution in the Script Editor).

## Project Structure

```
pyside_template_window/
├── __init__.py             # Package initialization
├── _metadata.py            # Package metadata (version, author info)
├── window.py               # Main window class
├── utils.py                # Utility functions
├── app/
│   ├── __init__.py         # App package initialization
│   ├── main.py             # Core launch functionality (start/restart/restore)
│   ├── start.py            # Initial launch
│   ├── restart.py          # Restart
│   └── restore.py          # Restore
├── docs/
│   ├── README.ja.md        # Japanese documentation
│   ├── README.zh-CN.md     # Chinese documentation
│   ├── CHANGELOG.ja.md     # Changelog (Japanese)
│   └── CONTRIBUTING.ja.md  # Contribution guide (Japanese)
├── README.md               # This file (English documentation)
├── CHANGELOG.md            # Changelog (English)
├── CONTRIBUTING.md         # Contribution guide (English)
└── LICENSE                 # License information
```

## API Reference

### PySideTemplateWindow Class

The main window class for the template.

**Normal usage does not require direct instantiation.** The class is internally instantiated within `app/main.py`.

```python
# Usage example in app/main.py
from ..window import PySideTemplateWindow

# Create instance
window = PySideTemplateWindow()
window.show()
```

#### Key Methods

| Method | Description |
|--------|-------------|
| `show()` | Displays the window |
| `set_instance(instance)` | Protects instance from garbage collection (called during restore) |

#### Class Variables

| Variable | Description |
|----------|-------------|
| `NAME` | Window name (`'PySideTemplate'`) |
| `WORKSPACE_CONTROL_NAME` | WorkspaceControl name (`'PySideTemplateWorkspaceControl'`) |
| `_TITLE` | Window title (`f'PySide Template v{__version__}'`) |

### app.main Module

| Function | Description |
|----------|-------------|
| `start()` | Shows existing window if available, otherwise creates a new one |
| `restart()` | Deletes existing WorkspaceControl and regenerates it |
| `restore()` | Auto-executed during Maya startup or workspace switching |

### utils Module

Utility module containing Maya-related common functionality.

| Function/Type | Description |
|---------------|-------------|
| `MayaPointer` | Type-safe representation of Maya UI pointers |
| `is_valid_maya_pointer()` | Validates Maya pointer integrity |
| `get_maya_control_pointer()` | Retrieves type-safe Maya control pointers |
| `safe_wrap_instance()` | Executes type-safe wrapInstance operations |
| `add_widget_to_maya_layout()` | Safely adds widgets to Maya layouts |

### Logging Configuration

Configures logging for development purposes. Maya defaults to INFO level.

| Function | Description |
|----------|-------------|
| `setup_logging(level)` | Configures logging for the package |

```python
# To output debug information
from pyside_template_window import setup_logging
import logging

setup_logging(logging.DEBUG)  # Display debug information
```

## Customization

Guidelines for adapting this package to create production tools.

### 1. Package Name Modification

Rename the package (folder name) to match your tool's identity.

```
# Before
~/Documents/maya/scripts/
└── pyside_template_window/

# After (example)
~/Documents/maya/scripts/
└── your_custom_tool/
```

**Corresponding changes required**:
- Import statements and function names in `app/main.py`, `app/start.py`, `app/restart.py`, `app/restore.py`

### 2. Class Name Modification

Update the class name accordingly.

```python
# Before
class PySideTemplateWindow(MayaQWidgetDockableMixin, QMainWindow):
    ...

# After (example)
class YourCustomWindow(MayaQWidgetDockableMixin, QMainWindow):
    ...
```

**Corresponding changes required**:
- Class variables such as NAME and _TITLE in `window.py`
- References in `app/main.py`

### 3. UI Customization

Modify the `_init_ui()` method to implement your custom interface.

```python
# window.py
def _init_ui(self) -> None:
    # Implement your custom UI here
    ...
```

## Development Best Practices

### Recommended Workflow

1. Edit your code
2. Execute one of the following in Maya:
   - Click "Restart" from the window's Dev menu
   - Copy and paste the contents of `restart.py` into the Script Editor and execute
3. Changes are immediately reflected

This workflow enables rapid iteration and streamlined development cycles.

## Troubleshooting

### Q: Reload functionality isn't working
A: Execute "Restart" from the window's Dev menu, or copy and paste the contents of `restart.py` into the Script Editor and execute it. Note that this reload mechanism uses simple `importlib.reload()`, which may not handle complex file structures effectively.

### Q: I want to reload on initial launch
A: Execute the contents of `restart.py` instead of `start.py` in the Script Editor. There's no issue with reloading during initial launch.

### Q: Window was closed with ☓ but the instance remains
A: This is expected PySide behavior. Execute the contents of `start.py` again in the Script Editor to redisplay the window.

### Q: Restore functionality stopped working after code modifications
A: The restore mechanism is quite delicate. It's recommended to revert to the original codebase and make changes incrementally and carefully.

### Q: Encountering errors in Maya 2020
A: Maya 2020 and earlier versions are not supported by this template.

## Translation

The author of this project is a native Japanese speaker. Pull requests for improving English and Chinese translations are warmly welcomed.

Any improvements to make the text more natural, better technical terminology, grammar fixes, or any other enhancements are greatly appreciated.

## License

This project is released under the MIT License. See the [LICENSE](LICENSE) file for details.
