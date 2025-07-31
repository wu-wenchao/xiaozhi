import threading  # 导入线程模块，用于创建定时任务
import time  # 导入时间模块，用于处理时间相关操作
import streamlit as st  # 导入streamlit模块，用于创建web界面
from utils import send_request  # 从utils模块导入send_request函数，用于发送请求


# 页面标题
st.title("小智打卡工具")
st.markdown("By口")

# 使用Streamlit的文本输入组件获取token
token = st.text_input("请输入token：", type="password")

# 定义定时任务函数
def schedule_request():
    if token:  # 只有当token不为空时才执行请求
        send_request(token)
        # 2秒后再次执行
        threading.Timer(3600, schedule_request).start()

# 添加开始按钮，一开始就显示
if st.button("开始打卡", key="start_button"):
    if token:
        schedule_request()
        st.success("打卡任务已启动！每60分钟自动打卡一次。")
    else:
        st.warning("请输入token后再开始打卡！")
