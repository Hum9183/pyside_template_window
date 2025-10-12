"""
ウィンドウの復元用モジュール

Maya の WorkspaceControl 機能による自動復元処理を行います。

このモジュールは inspect.getsource() で取得して cmds.workspaceControl の uiScript に渡すことを想定しています。
"""


def restore_pyside_template_window() -> None:
    """
    ウィンドウを復元します

    新しいウィンドウインスタンスを作成し、WorkspaceControl に適切に配置します。

    処理内容:
        1. 新しいウィンドウインスタンスの生成
        2. GC 対策のためのインスタンス保持
        3. Maya ポインタの取得と検証
        4. WorkspaceControl へのウィジェット追加

    Raises:
        RuntimeError: 復元処理に失敗した場合
    """
    from pyside_template_window import restore

    restore()


if __name__ == '__main__':
    restore_pyside_template_window()
