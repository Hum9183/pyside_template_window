"""
ウィンドウの再起動用モジュール

開発時のモジュールリロードと再起動を行います。

このモジュールは inspect.getsource() で取得して Dev メニューの Restart から実行することを想定しています。
ただしコピー&ペーストして Maya のスクリプトエディターで直接実行しても構いません。

実装を直接記述せず、main.restart() を呼び出すことで、開発中の変更の影響を受けないようにしています。
"""


def restart_pyside_template_window() -> None:
    """
    ウィンドウを再起動します

    既存の WorkspaceControl を削除してから新しいウィンドウを作成します。
    モジュールを増やした場合は importlib.reload() する処理を適宜追加してください。
    """
    import importlib
    import logging

    from pyside_template_window import window
    from pyside_template_window.app import main

    logger = logging.getLogger(__name__)

    logger.debug('モジュールをリロードしています...')
    importlib.reload(window)
    importlib.reload(main)

    logger.debug('ウィンドウを再起動しています...')
    main.restart()


if __name__ == '__main__':
    restart_pyside_template_window()
