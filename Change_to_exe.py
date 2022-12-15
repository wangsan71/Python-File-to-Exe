import os

# 要转换的Python程序的文件名
py_file = input("        | Python File to exe |\n \
请输入要转换的Python程序的文件名：")
if py_file.endswith(".py") or py_file.endswith(".pyw"):
    py_ch = py_file
else:
    py_ch = py_file + ".py"

if input("需要合為一個文件嗎(Yes or No): ").lower() in ["yes", "y","Yes","Y"]:
    F = "-F"
    print("確認合為一個文件")
else:
    F = ""
    print("取消合為一個文件")

# 使用pyinstaller命令来转换Python程序
# 请注意，这里使用了-F参数，表示将程序编译成单个文件
# 如果不想使用-F参数，可以将它删除
cmd = f"pyinstaller {F} {py_ch}"

# 使用os.system函数来调用系统中的命令行
try:
    os.system(cmd)
except:
    os.system("pip install pyinstaller")
    os.system(cmd)
finally:
    print("Finish")
    input("按回车键进行关闭")