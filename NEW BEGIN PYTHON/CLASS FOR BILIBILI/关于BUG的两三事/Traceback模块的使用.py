import traceback

try:
    print("=" * 30)
    print(1 / 0)
except:
    traceback.print_exc()  # 手动打印异常信息
