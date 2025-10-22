import logging
from typing import Optional

from maya import cmds

try:
    from PySide6.QtWidgets import QMainWindow
except ImportError:
    from PySide2.QtWidgets import QMainWindow

from .. import utils
from ..utils import MayaPointer
from ..window import PySideTemplateWindow

logger = logging.getLogger(__name__)


def start() -> None:
    """
    起動します

    既存のウィンドウがある場合は再表示し、ない場合は新規作成します。
    """
    window_ptr: Optional[MayaPointer] = utils.get_maya_control_pointer(PySideTemplateWindow.NAME)

    if window_ptr is None:
        # 新規作成
        logger.debug(f'{start.__name__}(): 新規作成')
        window = _create()
        window.show()
    else:
        # 既存ウィンドウの再表示
        logger.debug(f'{start.__name__}(): 既存ウィンドウの再表示')
        window = utils.safe_wrap_instance(window_ptr, QMainWindow)
        window.show()  # QMainWindow の show() ではあるが、PySideTemplateWindow の内部実装により PySideTemplateWindow.show() が呼ばれる


def restart() -> None:
    """
    再起動します

    既存の WorkspaceControl を削除してから新しいウィンドウを作成します。
    主に開発中に reload したい場合に使用します。
    """
    wsc_name = PySideTemplateWindow.WORKSPACE_CONTROL_NAME
    if cmds.workspaceControl(wsc_name, q=True, exists=True):
        logger.debug(f'{restart.__name__}(): 既存の WorkspaceControl を削除します')
        cmds.deleteUI(wsc_name, control=True)

    logger.debug(f'{restart.__name__}(): 新しいウィンドウを作成します')
    window = _create()
    window.show()


def restore() -> None:
    """
    WorkspaceControl の restore 処理です

    Maya の起動時やワークスペース切り替え時に呼び出される関数です。
    新しいウィンドウインスタンスを作成し、WorkspaceControl に追加します。
    """
    logger.debug(f'{restore.__name__}(): Maya が自動で WorkspaceControl を生成しています')
    window = _create()
    PySideTemplateWindow.set_instance(window)  # GC に破棄される"可能性がある"ため保持しておく

    # restore() のコンテキストでは WorkspaceControl は Maya が自動で生成するため、
    # utils.attach_window_to_workspace_control() を使ってウィジェットを追加します
    # addWidgetToMayaLayout() は内部で show() を呼ぶため、それで表示されます
    utils.attach_window_to_workspace_control(PySideTemplateWindow.NAME, PySideTemplateWindow.WORKSPACE_CONTROL_NAME)


def _create() -> PySideTemplateWindow:
    """
    新しいウィンドウインスタンスを生成します
    """
    window = PySideTemplateWindow()
    return window
