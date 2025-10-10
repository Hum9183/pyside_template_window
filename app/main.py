from typing import Optional

from maya import cmds

try:
    from PySide6.QtWidgets import QMainWindow
except ImportError:
    from PySide2.QtWidgets import QMainWindow

from .. import utils
from ..utils import MayaPointer
from ..window import PySideTemplateWindow


def start() -> None:
    """
    起動します

    既存のウィンドウがある場合は再表示し、ない場合は新規作成します。

    Raises:
        RuntimeError: ウィンドウの復元に失敗した場合
    """
    window_ptr: Optional[MayaPointer] = utils.get_maya_control_pointer(PySideTemplateWindow.NAME)

    if window_ptr is None:
        print(f'{PySideTemplateWindow.NAME} が存在しないため生成します')
        window = _generate()
        window.show()
    else:
        print(f'すでに {PySideTemplateWindow.NAME} が存在しています')
        try:
            window = utils.safe_wrap_instance(window_ptr, QMainWindow)
            window.show()
        except RuntimeError as e:
            print(f'{PySideTemplateWindow.NAME} の再表示に失敗しました: {e}')


def restart() -> None:
    """
    再起動します

    既存の WorkspaceControl を削除してから新しいウィンドウを作成します。
    主に開発中に reload したい場合に使用します。
    """
    if cmds.workspaceControl(PySideTemplateWindow.WORKSPACE_CONTROL_NAME, q=True, exists=True):
        # すでに存在している workspaceControl は削除する
        cmds.deleteUI(PySideTemplateWindow.WORKSPACE_CONTROL_NAME, control=True)

    window = _generate()
    window.show()


def restore() -> None:
    """
    WorkspaceControl の restore 処理です

    Maya の起動時やワークスペース切り替え時に呼び出される関数です。
    新しいウィンドウインスタンスを作成し、WorkspaceControl に追加します。

    Raises:
        RuntimeError: 復元処理に失敗した場合
    """
    window = _generate()
    PySideTemplateWindow.set_instance(window)  # GC に破棄される"可能性がある"ため保持しておく

    window_ptr: Optional[MayaPointer] = utils.get_maya_control_pointer(PySideTemplateWindow.NAME)
    wsc_ptr: Optional[MayaPointer] = utils.get_maya_control_pointer(PySideTemplateWindow.WORKSPACE_CONTROL_NAME)

    window_ptr_valid = window_ptr is not None
    wsc_ptr_valid = wsc_ptr is not None

    if window_ptr_valid and wsc_ptr_valid:
        utils.add_widget_to_maya_layout(window_ptr, wsc_ptr)
    else:
        if window_ptr_valid is False:
            raise RuntimeError(f'{PySideTemplateWindow.NAME} の復元用ウィンドウポインタが無効です')
        if wsc_ptr_valid is False:
            raise RuntimeError(f'{PySideTemplateWindow.WORKSPACE_CONTROL_NAME} の復元用 WorkspaceControl ポインタが無効です')


def _generate() -> PySideTemplateWindow:
    """
    新しいウィンドウインスタンスを生成します
    """
    window = PySideTemplateWindow()
    return window
