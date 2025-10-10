"""Maya PySide Template Window Package

Maya 用の PySide テンプレートウィンドウプロジェクトです。
WorkspaceControl を使用したドッキング可能かつ復元可能なウィンドウのテンプレートです。
"""

from ._metadata import __version__, __author__

# 主要な API をインポート可能にする
from .window import PySideTemplateWindow
from .app.main import start, restart, restore

__all__ = ['PySideTemplateWindow', 'start', 'restart', 'restore', '__version__', '__author__']
