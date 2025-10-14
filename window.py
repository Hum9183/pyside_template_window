import inspect
import logging
from typing import ClassVar, Optional

from maya import cmds
from maya.app.general.mayaMixin import MayaQWidgetDockableMixin

try:
    from PySide6.QtGui import QAction
    from PySide6.QtWidgets import QMainWindow, QPushButton, QWidget
except ImportError:
    from PySide2.QtWidgets import QAction
    from PySide2.QtWidgets import QMainWindow, QPushButton, QWidget

from . import utils
from ._metadata import __version__
from .app import restart, restore

logger = logging.getLogger(__name__)


class PySideTemplateWindow(MayaQWidgetDockableMixin, QMainWindow):
    """
    Maya 用の PySide のテンプレートウィンドウクラス

    WorkspaceControl を使用して Maya の UI にドッキング可能(Dockable)かつ復元(Restore)可能なウィンドウです。
    """

    NAME: ClassVar[str] = 'PySideTemplate'
    WORKSPACE_CONTROL_NAME: ClassVar[str] = f'{NAME}WorkspaceControl'
    _TITLE: ClassVar[str] = f'PySide Template v{__version__}'
    _instance: ClassVar[Optional['PySideTemplateWindow']] = None  # GC に破棄されないように保持しておく用

    def __init__(self, parent: Optional[QWidget] = None, *args, **kwargs) -> None:
        super().__init__(parent=parent, *args, **kwargs)
        self.setObjectName(PySideTemplateWindow.NAME)
        self._init_ui()

    @classmethod
    def set_instance(cls, instance: 'PySideTemplateWindow') -> None:
        """インスタンスをクラス変数で保持して GC から保護する"""
        cls._instance = instance

    def show(self) -> None:
        """
        ウィンドウを表示します

        既存の WorkspaceControl がある場合は復元し、ない場合は新規作成します。
        """
        wsc_name = PySideTemplateWindow.WORKSPACE_CONTROL_NAME
        wsc_exists = cmds.workspaceControl(wsc_name, q=True, exists=True)
        if wsc_exists:
            # 一度ウィンドウを出して、閉じて、もう一度呼び出したときに通る
            # (つまり wsc は存在するがウィンドウとしては非表示になっている場合)

            # override した show() 内で self.setVisible() や super().setVisible() を呼ぶと
            # 無限ループするため、QWidget.setVisible()を直接呼び出す
            QWidget.setVisible(self, True)
            cmds.workspaceControl(wsc_name, e=True, restore=True)  # 再表示
            cmds.setFocus(PySideTemplateWindow.NAME)
        else:
            self._create_workspace_control()
            utils.attach_window_to_workspace_control(
                PySideTemplateWindow.NAME, PySideTemplateWindow.WORKSPACE_CONTROL_NAME
            )
            self.setWindowTitle(PySideTemplateWindow._TITLE)  # タイトルを書き換えたときに反映されるようにここでsetする

    def _create_workspace_control(self) -> None:
        """
        WorkspaceControl を作成します

        Maya の restore 機能に対応した WorkspaceControl を作成します
        """
        wsc_name = PySideTemplateWindow.WORKSPACE_CONTROL_NAME
        restore_script = inspect.getsource(restore)

        # restore_script を発火させないように uiScript は空文字列を渡す
        cmds.workspaceControl(wsc_name, label=PySideTemplateWindow._TITLE, uiScript='')
        # restore_script を発火させないように e=True で設定する
        cmds.workspaceControl(wsc_name, e=True, uiScript=restore_script)

    def _init_ui(self) -> None:
        """
        UI の初期化を行います。

        UI をカスタマイズする場合はこのメソッドを編集してください。
        """
        # ボタン
        push_button = QPushButton('PUSH ME', self)
        push_button.clicked.connect(lambda *args: self._show_demo_message())
        self.setCentralWidget(push_button)

        # メニュー
        menu_bar = self.menuBar()
        dev_menu = menu_bar.addMenu('Dev')
        restart_action = QAction('Restart', self)
        restart_action.triggered.connect(lambda *args: restart.restart_pyside_template_window())
        dev_menu.addAction(restart_action)

    def _show_demo_message(self) -> None:
        """
        ダミーのメッセージを出力します
        """
        logger.info('Hello, World!')
