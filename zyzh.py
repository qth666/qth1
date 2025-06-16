import streamlit as st
from datetime import datetime, time
import pandas as pd

col1, col2 = st.columns([1, 3])
with col1:
    
    st.image("http://www.xuexili.com/uploads/allimg/2304/3-2304301HA5521.jpg")
with col2:
    st.markdown('# ***:blue[广西职业师范学院]***')
    st.markdown(':blue[Guangxi Vocational Normal University]')
    
    

tab1, tab2, tab3 = st.tabs(["数字档案", "南宁美食数据", "个人简历生成器"])

with tab1:
    st.title("🕶科比-职业生涯") #主标题
    st.header("🔑基础信息") #第一章节
    st.text("球衣号码：24")# 第一个普通文本展示元素

    st.markdown('''
注册时间：  :green[2005.08.05] 
| 精神状态:✅ 正常 ''')#展示文本，对部分文字着色
    st.markdown('''
当前位置:  :green[直升机]
| 安全等级: :green[漏风] ''')#展示文本，对部分文字着色

    st.header("📊技能矩阵")#第二章节
    c1, c2, c3 = st.columns(3)# 定义列布局，分成3列
    c1.metric(label="c语言", value="95%", delta="2%")#第一列文本信息
    c2.metric(label="python", value="87%", delta="-1%")#第二列文本信息
    c3.metric(label="java", value="68%", delta="10%")#第三列文本信息


    st.header("Streamlit课程进度")#第三章节
    st.progress(value=25,text="streamlit课程进度")#进度条显示


    st.header("📝任务日志 ")#第四章节

    import pandas as pd   # 导入Pandas并用pd代替

# 定义数据,以便创建数据框
    data = {
    '日期':['2023-10-01','2023-10-05','2023-10-012'],
    '任务':['学生数字档案', '课程管理系统', '数据图表展示'],
    '状态':['✅完成 ', '🕒进行中 ', '❌未完成'],
    '难度':[' ★★☆☆☆',  '★☆☆☆☆',  '★★★☆☆'],
}
# 定义数据框所用的索引
    index = pd.Series(['1', '2', '3'])
# 根据上面创建的data和index，创建数据框
    df = pd.DataFrame(data, index=index)

    st.table(df)#显示表格

    st.header(" 🔐 最新代码成果 ")#第五章节

# 创建要显示的Python代码块的内容
    python_code='''def matrix_breach():
   while True:
      if detect_vulnerability():
          exploit()
          return "ACCESS GRANTED"
      else:
          stealth_evade()'''
# 创建一个代码块，用于展示python_code的内容
    st.code(python_code)
#分割线
    st.markdown('***')

    st.markdown(''':green[>> SYSTEM MESSAGE:]   下一个任务目标已解锁...''')#展示文本，对部分文字着色
    st.markdown(''':green[>> TARGET:]   课程管理系统''')#展示文本，对部分文字着色
    st.markdown(''':green[>> GOUNTDOWN:]   2025-06-03 15:24:58''')#展示文本，对部分文字着色
    st.text("系统状态:在线 连接状态: 已加密")#展示普通文本

with tab2:
    data = {
    'latitude':[22.853838, 22.965046, 22.812200, 22.809105, 22.839699,22.790446],
    'longitude':[108.222177, 108.353921, 108.266629, 108.378664, 108.245804,108.312107],
    "评分": [4.2, 4.5, 4.0, 4.7, 4.3,4.6],
    "餐厅": ["星艺会尝不忘", "高峰柠檬鸭", "复记老友粉", "好友缘", "西冷牛排店",'三品王(南宁江南万达店)'],
    "人均消费": [15, 20, 25, 35, 50,12],
}
    data1={"月份":['01月', '02月', '03月','04月', '05月', '06月','07月', '08月', '09月','10月', '11月', '12月'],
       "星艺会尝不忘":[10,11,12,11,10,9,8,15,13,11,10,9],
       "高峰柠檬鸭":[58,68,66,55,75,88,78,72,68,62,58,55],
       "复记老友粉":[7,6,8,7,6,8,9,9,10,6,8,7],
       "好友缘":[40,35,36,38,39,37,32,30,28,40,41,35],
       "西冷牛排店":[50,52,56,58,60,49,48,68,66,60,58,50],
       '三品王(南宁江南万达店)':[13,14,12,15,16,17,13,12,14,15,12,14]}
    data2={"时间":[11.0,11.5,12.0,12.5,13.0,13.5,14.0,14.5,15.0,15.5,16.0,16.5,17.0,17.5,18.0,18.5,19.0],
       "高峰柠檬鸭":[35,40,80,75,70,65,60,55,50,45,40,33,35,75,60,40,30],
       "复记老友粉":[38,30,60,75,75,63,50,54,50,49,50,52,65,70,80,49,60],
       "好友缘":[30,35,40,42,30,65,80,85,80,45,40,33,40,45,60,80,30],
       "西冷牛排店":[40,50,60,75,80,85,50,55,60,45,40,63,75,65,60,40,50],
       '三品王(南宁江南万达店)':[35,36,30,65,70,85,60,55,46,45,30,33,55,85,70,60,60]}
    index=pd.Series([1,2,3,4,5,6],name="序号")

    df=pd.DataFrame(data)
    df1=pd.DataFrame(data1)
    df2=pd.DataFrame(data2)
#df.index=index
#st.dataframe(df)
#st.dataframe(df1)

    st.map(df)
    st.header("⭐餐厅评分")
    st.bar_chart(df,x="餐厅",y="评分")
    st.header("💰️不同餐厅价格变化")
    st.line_chart(df1,x="月份")
    st.header("🍽用餐高峰时段")
    st.area_chart(df2,x="时间")

with tab3:
   
#标题文本
    st.title("个人简历生成器")
#创建1：2的c1,c2方块
    c1, c2 = st.columns([1,2])
    with c1:
   # 创建一个子章节
       st.subheader("个人信息表单")
   # 分割线
       st.markdown('***')
   #简单文本框输入
       position= st.text_input('职位：',autocomplete='position')
#简单文本框输入
       name = st.text_input('姓名', autocomplete='name')
#简单文本框输入
       phone = st.text_input('电话', autocomplete='phone')
#简单文本框输入
       mailbox = st.text_input('邮箱', autocomplete='mailbox')
# value参数默认为None，初始状态为今天
       date = st.date_input("出生日期", value=None)
# 设置水平排列
       st.write('性别')
   #单选按钮
       gende = st.radio(
       '性别',
       ['男', '女', '其他'],
       horizontal=True,
       # 设置水平排列
       # 设置标签为“hidden”
       label_visibility='hidden'
)
   #下拉单选框用selectbox函数
       st.write('学历')
       degrees = st.selectbox(
       '学历',
       ['小学', '初中', '高中', '本科', '专科' '研究生', '硕士'],
       label_visibility='collapsed'
)
   #下拉多选框用multiselect
       st.write('语言能力')
       language = st.multiselect(
       '语言能力',
       ['英语', '西班牙语', '德语', '日语'],
#最大选择数量
       max_selections=4
       )
   #下拉多选框用multiselect
       options_2 = st.multiselect(
    '技能（可多选）',
    ['钢琴', '吉他', '篮球', '足球', '羽毛球'],
#最大选择数量
    max_selections=5)
   #数值滑块组件用slider函数
       age = st.slider('工作经验', 0, 30, 0)
   
#数值滑块组件用slider函数
       values = st.slider(
    '期望薪资',
    0.0, 50000.0, (10000.0, 20000.0))
#多行文本输入框
       a=st.text_area(label='个人简历：', placeholder='请简要介绍您的专业背景、职业目标和个人特点...')
   #日期选择
       w3 = st.time_input("最佳联系时间", datetime(2019, 7, 6, 21, 15))
   #照片上传文件
       uploaded_file = st.file_uploader('上传个人图片')
       if uploaded_file is not None:
          bytes_data =uploaded_file.getvalue()
          st.subheader('789')
          st.write(bytes_data)
   

    
  
    with c2:
   # 创建一个子章节
       st.subheader("简历实时预览")
    # 分割线
       st.markdown('***')
   
 #在c2里创建1：1的c1，c2方块
       c1, c2 = st.columns(2)
       with c1:
#普通输出文本
          st.write('职位：', position)
          st.write('电话：', phone)
          st.write('邮箱：', mailbox)
          st.write("出生日期:", date)

       with c2:
#普通输出文本
           st.write(f'性别：{gende}')
           st.write(f'学历：{degrees}')
           st.write("工作经验", age, '年')
           st.write('期望薪资：', values,'元')
           st.write("最佳联系时间:", w3)
#判断language变量是否为空
           if language is not None:
               
               st.text("语言能力："+",".join(language))

   # 分割线
       st.markdown('***')

   # 创建一个子章节
       st.subheader("个人简历")
   
       st.text(a)

    # 分割线
       st.markdown('***')
       st.write("专业技能")
   
#判断options_2变量是否为空
       if options_2 is not None:
#使用循环函数输出
          for i in options_2:
             st.write(i)
