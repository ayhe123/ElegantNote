# 一些工具
在同时处理多个 $\LaTeX$ 文件时可能需要用到的工具，可以用于原版的 ElegantNote。

## 文件说明

`change_style.py`：自动修改使用 ElegantNote 的 `.tex` 文件的样式

`auto_build.sh`：自动编译、删除临时文件

## 使用方法

### 修改样式

查看帮助
```bash
python change_style.py -h
```

将 `test1.tex` 转换为 green 主题、hazy 背景，并保存为 `test2.tex`
```bash
python change_style.py --fsrc test1.tex --fdst test2.tex -c green -b hazy
```

将 `test1.tex` 转换为 cyan 主题、pc 设备，并保存为 `test1.tex`
```bash
python change_style.py --fsrc test1.tex -c cyan -d pc
```

将当前目录下所有使用 ElegantNote 的 `.tex` 文件转换为 black 主题、geye 背景，就地保存
```bash
python change_style.py -c black -b geye
```

### 自动编译

**建议使用[这个程序](https://github.com/ayhe123/LaTeX-batch-builder)，这个脚本不会再更新了**

将 `auto_build.sh` 与要操作的 `.tex` 文件放在同一目录下。执行
```bash
./auto_build.sh
```
