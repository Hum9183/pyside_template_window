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

    Raises:
        RuntimeError: ウィンドウの復元に失敗した場合
    """
    window_ptr: Optional[MayaPointer] = utils.get_maya_control_pointer(PySideTemplateWindow.NAME)

    if window_ptr is None:
        logger.debug(f'{PySideTemplateWindow.NAME} が存在しないため生成します')
        window = _create()
        window.show()
    else:
        logger.debug(f'すでに {PySideTemplateWindow.NAME} が存在しています')
        try:
            window = utils.safe_wrap_instance(window_ptr, QMainWindow)
            window.show()
        except RuntimeError as e:
            logger.error(f'{PySideTemplateWindow.NAME} の再表示に失敗しました: {e}')


def restart() -> None:
    """
    再起動します

    既存の WorkspaceControl を削除してから新しいウィンドウを作成します。
    主に開発中に reload したい場合に使用します。
    """
    if cmds.workspaceControl(PySideTemplateWindow.WORKSPACE_CONTROL_NAME, q=True, exists=True):
        # すでに存在している workspaceControl は削除する
        cmds.deleteUI(PySideTemplateWindow.WORKSPACE_CONTROL_NAME, control=True)

    window = _create()
    window.show()


def restore() -> None:
    """
    WorkspaceControl の restore 処理です

    Maya の起動時やワークスペース切り替え時に呼び出される関数です。
    新しいウィンドウインスタンスを作成し、WorkspaceControl に追加します。

    Raises:
        RuntimeError: 復元処理に失敗した場合
    """
    window = _create()
    PySideTemplateWindow.set_instance(window)  # GC に破棄される"可能性がある"ため保持しておく

    utils.attach_window_to_workspace_control(PySideTemplateWindow.NAME, PySideTemplateWindow.WORKSPACE_CONTROL_NAME)


def _create() -> PySideTemplateWindow:
    """
    新しいウィンドウインスタンスを生成します
    """
    window = PySideTemplateWindow()
    return window
