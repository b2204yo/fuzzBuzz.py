# これはサンプルの Python スクリプトです。

# Shift+F10 を押して実行するか、ご自身のコードに置き換えてください。
# Shift を2回押す を押すと、クラス/ファイル/ツールウィンドウ/アクション/設定を検索します。


def fb(n):
    # スクリプトをデバッグするには以下のコード行でブレークポイントを使用してください。
    if n%3==0 and n%5==0:
        return "FizzBuzz"
    elif n%3==0 :
        return "Fizz"

    elif n%5==0 :
        return "Buzz"

    else:
        return ""


# ガター内の緑色のボタンを押すとスクリプトを実行します。
if __name__ == '__main__':
    i = 1
    while i <= 20:
        print(i, fb(i))
        i = i + 1
# PyCharm のヘルプは https://www.jetbrains.com/help/pycharm/ を参照してください
