#!/usr/bin/env python3
"""Week 14 project 1: manage small persistent databases with dbm."""

# 普通の辞書と違い、dbmへ保存した内容はプログラムを終了してもファイルに残る。
import dbm


def usage():
    """Print every valid command form and terminate the program."""

    print("usage:")
    print("    database-name set key value")
    print("    database-name get key")
    print("    database-name del key")
    print("    database-name keys")
    print("    database-name values")

    # PDFの指示どおり、不正な入力の後はシェルへ戻らずプログラムを終了する。
    # SystemExitを使うと、後続処理を実行せず終了コード1で停止できる。
    raise SystemExit(1)


def perform(database, command, arguments):
    """Perform one database command using the supplied string arguments."""

    # 各commandに必要な引数の個数を辞書にしておく。
    # 先に確認することで、足りない引数を取り出してエラーになることを防ぐ。
    requiredArguments = {
        "set": 2,
        "get": 1,
        "del": 1,
        "keys": 0,
        "values": 0,
    }
    if command not in requiredArguments:
        usage()
    # 上で未知のcommandを除外したので、安全に辞書の[command]を参照できる。
    if len(arguments) != requiredArguments[command]:
        usage()

    # "c"は既存databaseを読み書き用で開き、なければ新しく作る指定。
    # withを抜ける時に必ずcloseされるので、次のcommandからも安全に開ける。
    with dbm.open(database, "c") as databaseFile:
        if command == "set":
            # 引数が2個だと確認済みなので、keyとvalueへ1個ずつ分けられる。
            key, value = arguments

            # dbmは文字列ではなくbytesとして保存するので、UTF-8へ変換する。
            databaseFile[key.encode("utf-8")] = value.encode("utf-8")
            # この代入内容はメモリだけでなくdatabaseファイルへ保存される。

        elif command == "get":
            key = arguments[0].encode("utf-8")

            # 存在しないキーを直接読むとKeyErrorになるため、先に確認する。
            # PDFの指定では、存在しない場合は何も表示しなくてよい。
            if key in databaseFile:
                print(databaseFile[key].decode("utf-8"))

        elif command == "del":
            key = arguments[0].encode("utf-8")
            if key in databaseFile:
                del databaseFile[key]

        elif command == "keys":
            # dbmから返るキーもbytesなので、表示前に文字列へdecodeする。
            # 並び順を一定にするため、decodeしたキーをアルファベット順にする。
            keys = sorted(key.decode("utf-8") for key in databaseFile.keys())
            # joinはリスト中のキーを空白でつなぎ、例と同じ1行で表示する。
            print(" ".join(keys))

        elif command == "values":
            # keysと同じ順番で、各キーに対応する値も1行ずつ表示する。
            keys = sorted(key.decode("utf-8") for key in databaseFile.keys())
            for key in keys:
                value = databaseFile[key.encode("utf-8")].decode("utf-8")
                print(key, value)


def main():
    # 1行処理した後も先頭へ戻り、空行が入力されるまで簡易シェルを続ける。
    while True:
        try:
            # stripで前後の空白を除き、splitで単語のリストへ分割する。
            words = input("? ").strip().split()
        except EOFError:
            # Ctrl+Zなどで入力が終了した場合も、空行と同じように終了する。
            break

        if not words:
            break  # 何も入力されなかった空行が、この簡易シェルの終了命令。
        if len(words) < 2:
            usage()

        # 先頭2語はdatabase名とcommandとして役割が決まっている。
        database = words[0]
        command = words[1]
        arguments = words[2:]  # 2番目より後ろに残った単語がcommandの引数。
        perform(database, command, arguments)


if __name__ == "__main__":
    main()
