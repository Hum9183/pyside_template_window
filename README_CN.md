# Maya PySide 模板窗口

基于 WorkspaceControl 的 Maya PySide 模板窗口项目，提供可停靠和可还原的窗口功能。

[日本語版](README.md) | [English Version](README_EN.md)

## 特性

- ✅ **WorkspaceControl 集成**：无缝对接 Maya 工作区
- ✅ **自动还原**：Maya 启动时自动还原
- ✅ **热重载**：快速模块重载，提高开发效率

## 支持版本

- Maya 2022
- Maya 2023
- Maya 2024
- Maya 2025
- Maya 2026

## 安装

### 文件放置

将项目放置在 Maya 的 scripts 文件夹或任何在 Python 路径中的目录。

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

### 初次启动

将 `start.py` 的内容复制粘贴到 Maya 脚本编辑器中并执行。

### 开发时重启

点击窗口Dev菜单中的"Restart"，或将 `restart.py` 的内容复制粘贴到脚本编辑器中并执行。这将重载模块并重启窗口。

### Maya 启动时自动还原

Maya 启动时窗口会自动还原。`restore.py` 脚本处理此功能（不用于在脚本编辑器中手动执行）。

## 项目结构

```
pyside_template_window/
├── __init__.py          # 包初始化
├── _metadata.py         # 包元数据（版本、作者信息）
├── window.py            # 主窗口类
├── utils.py             # 实用工具函数
├── app/
│   ├── __init__.py      # 应用包初始化
│   ├── main.py          # 核心启动功能（start/restart/restore）
│   ├── start.py         # 初次启动
│   ├── restart.py       # 重启
│   └── restore.py       # 还原
├── README.md            # 日文文档
├── README_EN.md         # 英文文档
├── README_CN.md         # 本文件（中文文档）
├── CHANGELOG.md         # 变更日志（日文）
├── CHANGELOG_EN.md      # 变更日志（英文）
├── CHANGELOG_CN.md      # 变更日志（中文）
└── LICENSE              # 许可证信息
```

## API 参考

### PySideTemplateWindow 类

模板的主窗口类。

**正常使用时无需直接实例化。** 该类在 `app/main.py` 内部进行实例化。

```python
# app/main.py 中的使用示例
from ..window import PySideTemplateWindow

# 创建实例
window = PySideTemplateWindow()
window.show()
```

#### 主要方法

| 方法 | 说明 |
|------|------|
| `show()` | 显示窗口 |
| `set_instance(instance)` | 保护实例免受垃圾回收（在还原期间调用） |

#### 类变量

| 变量 | 说明 |
|------|------|
| `NAME` | 窗口名称 (`'PySideTemplate'`) |
| `WORKSPACE_CONTROL_NAME` | WorkspaceControl 名称 (`'PySideTemplateWorkspaceControl'`) |
| `_TITLE` | 窗口标题 (`'PySide Template v1.0.0'`) |

### app.main 模块

| 函数 | 说明 |
|------|------|
| `start()` | 如果存在则显示现有窗口，否则创建新窗口 |
| `restart()` | 删除现有 WorkspaceControl 并重新生成 |
| `restore()` | 在 Maya 启动或工作区切换期间自动执行 |

### utils 模块

包含 Maya 相关通用功能的实用工具模块。

| 函数/类型 | 说明 |
|-----------|------|
| `MayaPointer` | Maya UI 指针的类型安全表示 |
| `is_valid_maya_pointer()` | 验证 Maya 指针完整性 |
| `get_maya_control_pointer()` | 获取类型安全的 Maya 控件指针 |
| `safe_wrap_instance()` | 执行类型安全的 wrapInstance 操作 |
| `add_widget_to_maya_layout()` | 安全地将组件添加到 Maya 布局 |

## 自定义

适配此包以创建生产工具的指南。

### 1. 包名修改

根据工具的身份重命名包（文件夹名）。

```
# 修改前
~/Documents/maya/scripts/
└── pyside_template_window/

# 修改后（示例）
~/Documents/maya/scripts/
└── your_custom_tool/
```

**需要相应修改**：
- `app/main.py`、`app/start.py`、`app/restart.py`、`app/restore.py` 中的导入语句和函数名

### 2. 类名修改

相应地更新类名。

```python
# 修改前
class PySideTemplateWindow(MayaQWidgetDockableMixin, QMainWindow):
    ...

# 修改后（示例）
class YourCustomWindow(MayaQWidgetDockableMixin, QMainWindow):
    ...
```

**需要相应修改**：
- `window.py` 中的 NAME、_TITLE 等类变量
- `app/main.py` 中的引用

### 3. UI 自定义

修改 `_init_ui()` 方法以实现自定义界面。

```python
# window.py
def _init_ui(self) -> None:
    # 在此实现自定义 UI
    ...
```

## 开发最佳实践

### 推荐工作流程

1. 编辑代码
2. 在 Maya 中执行以下操作之一：
   - 点击窗口Dev菜单中的"Restart"
   - 将 `restart.py` 的内容复制粘贴到脚本编辑器中并执行
3. 更改立即生效

此工作流程可实现快速迭代和流畅的开发周期。

## 疑难解答

### Q: 重载功能无效
A: 从窗口的Dev菜单执行"Restart"，或将 `restart.py` 的内容复制粘贴到脚本编辑器中并执行。注意此重载机制使用简单的 `importlib.reload()`，可能无法有效处理复杂的文件结构。

### Q: 希望在初次启动时重载
A: 在脚本编辑器中执行 `restart.py` 的内容而非 `start.py`。初次启动时重载没有任何问题。

### Q: 窗口被 ☓ 关闭但实例仍然存在
A: 这是预期的 PySide 行为。在脚本编辑器中再次执行 `start.py` 的内容以重新显示窗口。

### Q: 代码修改后还原功能停止工作
A: 还原机制相当脆弱。建议恢复到原始代码库并逐步谨慎地进行更改。

### Q: 在 Maya 2020 中遇到错误
A: 此模板不支持 Maya 2020 及更早版本。

## 许可证

此项目根据 MIT 许可证发布。详情请参见 [LICENSE](LICENSE) 文件。
