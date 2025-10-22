import inspect
import logging
from typing import ClassVar, Optional

from maya import cmds

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


class PySideTemplateWindow(QMainWindow):
    """
    Maya 用の PySide のテンプレートウィンドウクラス

    WorkspaceControl を使用して Maya の UI にドッキング可能(Dockable)かつ復元(Restore)可能なウィンドウです。

    Implementation Note:
        このクラスは MayaQWidgetDockableMixin を使用せず、Qt の仮想メソッドのオーバーライドを利用して
        同等の機能を実現しています。setVisible() をオーバーライドすることで、wrapInstance() でラップした
        QMainWindow オブジェクトに対しても show() の動作を制御できるようにしています。
    """

    NAME: ClassVar[str] = 'PySideTemplate'
    WORKSPACE_CONTROL_NAME: ClassVar[str] = f'{NAME}WorkspaceControl'
    _TITLE: ClassVar[str] = f'PySide Template v{__version__}'
    _instance: ClassVar[Optional['PySideTemplateWindow']] = None  # GC に破棄されないように保持しておく用

    def __init__(self, parent: Optional[QWidget] = None, *args, **kwargs) -> None:
        """
        Args:
            parent: 親ウィジェット（通常は None で問題ありません）

        Note:
            一般的な PySide ウィンドウでは Maya のメインウィンドウを親に設定しますが、
            WorkspaceControl を使用する場合は親は None のままで問題ありません。
            WorkspaceControl が適切に親子関係を管理するため、Maya 終了時にウィンドウも
            正しく閉じられ、restore 機能も正常に動作します。
        """
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

        既存の WorkspaceControl がある場合は再表示し、ない場合は新規作成します。

        Note:
            このメソッドは以下のタイミングで呼ばれます：
            - 初回作成時: start() → _create() → show()
            - 再表示時: start() → QMainWindow.show() → setVisible() → show()
            - 再起動時: restart() → _create() → show()
            - 復元時: restore() → omui.MQtUtil.addWidgetToMayaLayout() → show()
        """
        wsc_name = PySideTemplateWindow.WORKSPACE_CONTROL_NAME
        wsc_exists = cmds.workspaceControl(wsc_name, q=True, exists=True)
        if wsc_exists:
            # 再表示時と復元時に通る
            # wsc もウィンドウも存在するが非表示になっている場合
            logger.debug(f'{self.show.__name__}(): WorkspaceControl が存在 → 再表示')

            # override した show() 内で self.setVisible() や super().setVisible() を呼ぶと
            # 無限ループするため、QWidget.setVisible()を直接呼び出す
            QWidget.setVisible(self, True)
            cmds.workspaceControl(wsc_name, e=True, restore=True)
        else:
            logger.debug(f'{self.show.__name__}(): WorkspaceControl が存在しない → 新規作成')
            self._create_workspace_control()
            utils.attach_window_to_workspace_control(
                PySideTemplateWindow.NAME, PySideTemplateWindow.WORKSPACE_CONTROL_NAME
            )

        # すべてのケースで最新のタイトルを設定
        # WorkspaceControl の label を設定すれば十分で、setWindowTitle() は不要
        cmds.workspaceControl(wsc_name, e=True, label=PySideTemplateWindow._TITLE)

    def setVisible(self, visible: bool) -> None:
        """
        ウィジェットの表示状態を設定します

        Qt の仮想メソッドのオーバーライドにより、C++ 側から呼ばれる setVisible() を Python で override します。
        これにより、wrapInstance() でラップした QMainWindow オブジェクトの show() を呼んでも、
        この Python メソッドが実行されます。

        実装の意図:
            QMainWindow.show() は内部で setVisible(True) を呼ぶため、setVisible() を
            オーバーライドすることで、show() の動作を制御できます。setVisible() 内で
            show() を呼ぶことで、WorkspaceControl の処理をこのクラス内部に隠蔽し、
            呼び出し側（start() 関数）に実装の詳細が漏れ出さないようにしています。
            この実装パターンは MayaQWidgetDockableMixin と同じです。

        Note:
            setVisible(True) が呼ばれると show() を呼び、show() 内で WorkspaceControl の
            再表示処理を行います。
        """
        if visible:
            logger.debug(f'{self.setVisible.__name__}(True): show() を呼びます')
            self.show()
        else:
            logger.debug(f'{self.setVisible.__name__}(False): ウィンドウを非表示にします')
            QWidget.setVisible(self, False)

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
        # メニュー
        menu_bar = self.menuBar()
        dev_menu = menu_bar.addMenu('Dev')
        restart_action = QAction('Restart', self)
        restart_action.triggered.connect(lambda *args: restart.restart_pyside_template_window())
        dev_menu.addAction(restart_action)

        # ボタン
        push_button = QPushButton('PUSH ME', self)
        push_button.clicked.connect(lambda *args: self._show_demo_message())
        self.setCentralWidget(push_button)

    def _show_demo_message(self) -> None:
        """
        ダミーのメッセージを出力します
        """
        logger.info('Hello, World!')
