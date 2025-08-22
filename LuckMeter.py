import tkinter as tk
from tkinter import ttk
import random


def test_luck():
    num = random.randint(-1, 100)
    result_label.config(text=f"您今天的幸运值是: {num}")

    if num == -1:
        comment = "倒了大霉 🍂（比0还惨）"
    elif num == 100:
        comment = "欧皇附体 🌟（满分好运）"
    elif num >= 80:
        comment = "运气爆棚 ✨（今天要中大奖了！）"
    elif num >= 50:
        comment = "运气不错 😎（中规中矩的好运）"
    elif num >= 20:
        comment = "有点非啊 😅（平平淡淡才是真）"
    else:
        comment = "非酋警告 ⚠️（今天最好别抽卡…）"

    comment_label.config(text=f"{comment}")


# 创建主窗口
root = tk.Tk()
root.title("幸运值测试器")
root.geometry("400x250")
root.configure(bg="#1e1e1e")  # 深色背景

# ttk 样式
style = ttk.Style()
style.theme_use("default")  # 使用默认主题，避免 macOS 强制系统主题
style.configure(
    "Dark.TButton",
    background="#2a2a2a",
    foreground="white",
    font=("Helvetica", 12),
    padding=6,
    relief="flat"
)
style.map(
    "Dark.TButton",
    background=[("active", "#3a3a3a")],
    foreground=[("active", "white")]
)

# 标题
title_label = tk.Label(
    root,
    text="幸运值测试器",
    font=("Helvetica", 18, "bold"),
    fg="white",
    bg="#1e1e1e"
)
title_label.pack(pady=10)

# 显示结果
result_label = tk.Label(
    root,
    text="",
    font=("Helvetica", 14),
    fg="lightgreen",
    bg="#1e1e1e"
)
result_label.pack(pady=10)

# 显示评价
comment_label = tk.Label(
    root,
    text="",
    font=("Helvetica", 12),
    fg="lightblue",
    bg="#1e1e1e"
)
comment_label.pack(pady=10)

# ttk 按钮
button = ttk.Button(root, text="重新测！", command=test_luck, style="Dark.TButton")
button.pack(pady=20)

# 程序启动时先测一次
test_luck()

root.mainloop()