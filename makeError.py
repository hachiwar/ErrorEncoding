from pathlib import Path

path = Path("test.cpp")

# 原本是 UTF-8 正常文本
text = path.read_text(encoding="utf-8")

# 模拟错误操作：
# 1. 原本 UTF-8 的字节
# 2. 被错误地当成 GBK 解码
# 3. 得到乱码文本
mojibake = text.encode("utf-8").decode("gbk", errors="ignore")

# 再把乱码文本保存成 UTF-8
# 这一步就相当于“乱码已经被真正写入文件”
path.write_text(mojibake, encoding="utf-8")

print("已经把 test.cpp 故意保存成乱码")