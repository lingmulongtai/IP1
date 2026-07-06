"""Week 13 project 4: find the largest files below a directory."""

import os
import sys


if hasattr(sys.stdout, "reconfigure"):
    # 日本語を含むパスを印刷しても、Windowsの端末で止まりにくくする。
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")


def getfiles(dirpath, pathlist):
    for name in os.listdir(dirpath):
        path = os.path.join(dirpath, name)

        if os.path.isfile(path):
            # ファイルだけをリストに入れる。ディレクトリは中身をさらに調べる。
            pathlist.append(path)
        elif os.path.isdir(path):
            getfiles(path, pathlist)

    return pathlist


def getsizes(paths):
    result = []
    for path in paths:
        # サイズを整数のまま先頭に置くと、sortした時に数値順になる。
        result.append((os.path.getsize(path), path))
    return result


def printSizes(dirname):
    paths = getfiles(dirname, [])
    for size, path in sorted(getsizes(paths)):
        # タブで区切ると、サイズとパスが少し読みやすい。
        print(size, path, sep="\t")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        dirname = sys.argv[1]
    else:
        dirname = input("Directory: ")

    printSizes(dirname)
