"""Maya PySide Template Window Package

Maya 用の PySide テンプレートウィンドウプロジェクトです。
WorkspaceControl を使用したドッキング可能かつ復元可能なウィンドウのテンプレートです。
"""

import logging

from ._metadata import __author__, __version__
from .app.main import restart, restore, start


def setup_logging(log_level: int = logging.INFO) -> logging.Logger:
    """パッケージ用のロギング設定を行う

    Args:
        log_level (int): ログレベル（logging.DEBUG, logging.INFO など）
                         Maya では通常 INFO レベルがデフォルトです

    Returns:
        logging.Logger: 設定されたパッケージロガー

    Examples:
        >>> # 基本的な使用方法（INFO レベル）
        >>> logger = setup_logging()

        >>> # デバッグ情報も出力したい場合
        >>> logger = setup_logging(logging.DEBUG)
    """
    # パッケージロガーのレベルを設定
    logger = logging.getLogger(__name__)  # __init__.py では __name__ が直接パッケージ名
    logger.setLevel(log_level)
    return logger


__all__ = ['start', 'restart', 'restore', 'setup_logging', '__version__', '__author__']
