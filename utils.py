"""
Maya UI 操作のためのユーティリティ関数集

このモジュールには、Maya のポインタ操作、型安全性、UI 関連の
共通機能をまとめています。
"""

from typing import NewType, Optional, Type, TypeVar

from maya import OpenMayaUI as omui

try:
    from shiboken6 import wrapInstance  # type: ignore
except ImportError:
    from shiboken2 import wrapInstance  # type: ignore

# Maya 専用型の定義
MayaPointer = NewType('MayaPointer', int)

T = TypeVar('T')


def get_maya_control_pointer(control_name: str) -> Optional[MayaPointer]:
    """型安全な Maya コントロールのポインタを取得する

    指定されたコントロール名から Maya の UI ポインタを安全に取得します。
    無効なポインタの場合は None を返します。

    Args:
        control_name (str): Maya コントロール名

    Returns:
        Optional[MayaPointer]: 有効なポインタまたは None
    """
    ptr = omui.MQtUtil.findControl(control_name)
    if _is_valid_maya_pointer(ptr):
        return MayaPointer(int(ptr))
    return None


def safe_wrap_instance(ptr: MayaPointer, widget_type: Type[T]) -> T:
    """型安全な wrapInstance 実行

    Maya ポインタから PySide ウィジェットへの安全な変換を行います。
    変換に失敗した場合は詳細なエラー情報と共に例外を発生させます。

    Args:
        ptr (MayaPointer): 有効な Maya ポインタ
        widget_type (Type[T]): ラップするウィジェットタイプ

    Returns:
        T: ラップされたウィジェットインスタンス

    Raises:
        RuntimeError: ラッピングに失敗した場合
        TypeError: widget_type が不正な型の場合
    """
    if isinstance(widget_type, type) is False:
        raise TypeError(f'widget_type はクラスである必要があります。{type(widget_type).__name__} が渡されました')

    try:
        return wrapInstance(ptr, widget_type)
    except Exception as e:
        raise RuntimeError(f'Maya ウィジェットのラップに失敗しました: {e}') from e


def attach_window_to_workspace_control(window_name: str, workspace_control_name: str) -> None:
    """ウィンドウを WorkspaceControl にアタッチする（名前版）

    指定されたウィンドウと WorkspaceControl のポインタを取得し、
    検証した上でウィンドウを WorkspaceControl にアタッチします。

    Args:
        window_name (str): ウィンドウの名前
        workspace_control_name (str): WorkspaceControl の名前

    Raises:
        RuntimeError: ポインタの取得またはアタッチに失敗した場合
    """
    window_ptr: Optional[MayaPointer] = get_maya_control_pointer(window_name)
    wsc_ptr: Optional[MayaPointer] = get_maya_control_pointer(workspace_control_name)

    window_ptr_valid = window_ptr is not None
    wsc_ptr_valid = wsc_ptr is not None

    if window_ptr_valid and wsc_ptr_valid:
        _add_widget_to_workspace_control(window_ptr, wsc_ptr)
    else:
        if window_ptr_valid is False:
            raise RuntimeError(f'{window_name} のポインタの取得に失敗しました')
        if wsc_ptr_valid is False:
            raise RuntimeError(f'{workspace_control_name} のポインタの取得に失敗しました')


def _add_widget_to_workspace_control(window_ptr: MayaPointer, workspace_ptr: MayaPointer) -> None:
    """ウィジェットを WorkspaceControl に追加する（ポインタ版）

    指定されたウィンドウポインタを WorkspaceControl レイアウトに直接追加します。
    追加に失敗した場合は詳細なエラー情報と共に例外を発生させます。

    Args:
        window_ptr (MayaPointer): ウィンドウポインタ
        workspace_ptr (MayaPointer): WorkspaceControl ポインタ

    Raises:
        RuntimeError: レイアウト追加に失敗した場合
    """
    try:
        omui.MQtUtil.addWidgetToMayaLayout(window_ptr, workspace_ptr)
    except Exception as e:
        raise RuntimeError(f'WorkspaceControl への追加に失敗: {e}') from e


def _is_valid_maya_pointer(ptr: object) -> bool:
    """Maya ポインタの有効性をチェックする

    Maya から取得したポインタ値が有効かどうかを判定します。
    None、負の値、変換不可能な値は無効として扱います。

    Args:
        ptr (object): チェック対象のオブジェクト

    Returns:
        bool: ポインタが有効な場合 True、無効な場合 False
    """
    if ptr is None:
        return False

    try:
        # 正の整数に変換してチェック
        int_ptr = int(ptr)
        return int_ptr > 0
    except (ValueError, TypeError):
        return False
