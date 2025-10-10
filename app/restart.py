"""
ウィンドウの再起動用モジュール

開発時のモジュールリロードと再起動を行います。

このモジュールは inspect.getsource() で取得して Dev メニューの Restart から実行することを想定しています。
ただしコピー&ペーストして Maya のスクリプトエディターで直接実行しても構いません。
"""

def restart_pyside_template_window() -> None:
    """
    ウィンドウを再起動します

    既存の WorkspaceControl を削除してから新しいウィンドウを作成します。
    モジュールを増やした場合は importlib.reload() する処理を適宜追加してください。

    処理内容:
        1. 関連モジュールのリロード（window, main）
        2. 既存 WorkspaceControl の削除
        3. 新しいウィンドウインスタンスの作成・表示
    """
    import importlib

    from pyside_template_window import window
    from pyside_template_window.app import main

    importlib.reload(window)
    importlib.reload(main)
    main.restart()


if __name__ == '__main__':
    restart_pyside_template_window()
