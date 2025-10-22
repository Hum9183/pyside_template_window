"""
ウィンドウの復元用モジュール

Maya の WorkspaceControl 機能による自動復元処理を行います。

このモジュールは inspect.getsource() で取得して cmds.workspaceControl の uiScript に渡すことを想定しています。

実装を直接記述せず、main.restore() を呼び出すことで、開発中の変更の影響を受けないようにしています。
"""


def restore_pyside_template_window() -> None:
    """
    ウィンドウを復元します

    新しいウィンドウインスタンスを作成し、WorkspaceControl に適切に配置します。
    """
    from pyside_template_window import restore

    restore()


if __name__ == '__main__':
    restore_pyside_template_window()
