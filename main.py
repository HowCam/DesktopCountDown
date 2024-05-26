import tkinter as tk
from datetime import datetime, timedelta

class CountdownApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("倒计时器")
        self.root.geometry("600x160")  # 设置窗口大小
        self.root.configure(bg='black')  # 设置窗口背景色为黑色
        self.root.overrideredirect(True)  # 去掉窗口边框和标题栏

        # # 设置窗口默认置顶
        # self.root.attributes("-topmost",True)

        # 获取屏幕的宽度和高度
        screenWidth = self.root.winfo_screenwidth()
        screenHeight = self.root.winfo_screenheight()

        # 计算窗口位置，使其居中
        self.root.geometry(f"+{screenWidth//2 - 250}+0")

        self.label = tk.Label(self.root, font=("仿宋", 24), fg='yellow', bg='black')
        self.label.pack(pady=20)

        # 读取时间文件
        with open("time.txt", "r") as file:
            self.end_date = datetime.strptime(file.read().strip(), "%Y-%m-%d %H:%M:%S")

        self.update_countdown()

    def update_countdown(self):
        current_date = datetime.now()
        remaining_time = self.end_date - current_date

        if remaining_time.total_seconds() <= 0:
            self.label.config(text="时间已到！")
        else:
            days = remaining_time.days
            hours, remainder = divmod(remaining_time.seconds, 3600)
            minutes, seconds = divmod(remainder, 60)
            self.label.config(text=f"距离中考还有：{days}天 {hours}小时 {minutes}分钟 {seconds}秒\n距离二模还有：{days-8}天 {hours}小时 {minutes}分钟 {seconds}秒")

        self.root.after(1000, self.update_countdown)

def main():
    app = CountdownApp()
    app.root.mainloop()

if __name__ == "__main__":
    main()