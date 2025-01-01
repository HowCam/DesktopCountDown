import tkinter as tk
from datetime import datetime
import yaml

class CountdownApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("倒计时器")
        self.root.geometry("600x80")  # 增加高度，适应多个倒计时
        self.root.configure(bg='black')  # 设置窗口背景色为黑色
        self.root.overrideredirect(True)  # 去掉窗口边框和标题栏

        # 获取屏幕的宽度和高度
        screenWidth = self.root.winfo_screenwidth()
        screenHeight = self.root.winfo_screenheight()

        # 计算窗口位置，使其居中
        self.root.geometry(f"+{screenWidth//2 - 250}+0")

        # 读取YAML配置文件
        self.projects = self.load_config()

        # 设置窗口默认置顶
        self.root.attributes("-topmost",True)


        # 创建显示标签
        self.label = tk.Label(self.root, font=("仿宋", 24), fg='yellow', bg='black')
        self.label.pack(pady=20)

        self.update_countdown()

    def load_config(self):
        """从YAML文件加载配置"""
        with open("countdown_config.yml", "r", encoding="utf-8") as file:
            config = yaml.safe_load(file)
        # 解析配置文件
        projects = []
        for project in config.get("projects", []):
            name = project.get("name")
            end_time_str = project.get("end_time")
            end_time = datetime.strptime(end_time_str, "%Y-%m-%d %H:%M:%S")
            projects.append({"name": name, "end_time": end_time})
        return projects

    def update_countdown(self):
        current_date = datetime.now()
        countdown_text = ""
        
        for project in self.projects:
            remaining_time = project["end_time"] - current_date

            if remaining_time.total_seconds() <= 0:
                countdown_text += f"{project['name']}：时间已到！\n"
            else:
                days = remaining_time.days
                hours, remainder = divmod(remaining_time.seconds, 3600)
                minutes, seconds = divmod(remainder, 60)
                countdown_text += f"距离 {project['name']} 还有：{days}天 {hours}小时 {minutes}分钟 {seconds}秒"

        self.label.config(text=countdown_text)

        # 每秒更新倒计时
        self.root.after(1000, self.update_countdown)

def main():
    app = CountdownApp()
    app.root.mainloop()

if __name__ == "__main__":
    main()
