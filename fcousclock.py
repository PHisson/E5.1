import time

def focus_timer(duration):
    print("专注时钟启动！")
    time.sleep(duration * 60)
    print("时间到！")

if __name__ == "__main__":
    try:
        duration = int(input("请输入专注时长（分钟）："))
        focus_timer(duration)
    except ValueError:
        print("输入无效！请输入一个整数值。")
