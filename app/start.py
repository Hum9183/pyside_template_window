"""
ウィンドウの初回起動用スクリプト

このスクリプトを Maya のスクリプトエディターで直接実行することで、
ウィンドウを起動できます。

使用方法:
    1. Maya のスクリプトエディターを開く
    2. このファイルの内容をコピー&ペーストして実行
"""


def start_pyside_template_window() -> None:
    """
    ウィンドウを起動します

    既存のウィンドウがある場合は再表示し、ない場合は新規作成します。
    """
    from pyside_template_window import start

    start()


if __name__ == '__main__':
    start_pyside_template_window()
