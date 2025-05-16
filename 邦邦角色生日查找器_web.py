import streamlit as st

bands = {
    "Poppin Party": ["户山香澄", "花园多惠", "牛达里美", "市谷有咲", "山吹沙绫"],
    "Afterglow": ["美竹兰", "青叶摩卡", "宇田川巴", "上原绯玛丽", "羽泽鸫"],
    "Pastel Palettes": ["丸山彩", "若宫伊芙", "白鹭千圣", "大和麻弥", "冰川日菜"],
}

birthdays = {
    "户山香澄": "7月14日", "花园多惠": "12月4日", "牛达里美": "3月23日", "市谷有咲": "10月27日", "山吹沙绫": "5月19日",
    "美竹兰": "4月10日", "青叶摩卡": "9月3日", "宇田川巴": "4月15日", "上原绯玛丽": "10月23日", "羽泽鸫": "1月7日",
    "丸山彩": "12月27日", "若宫伊芙": "6月27日", "白鹭千圣": "4月6日", "大和麻弥": "11月3日", "冰川日菜": "3月20日",
}

st.title("邦邦角色生日查找器")

band = st.selectbox("请选择乐队", list(bands.keys()))
if band:
    st.write("该乐队成员有：", ", ".join(bands[band]))
    member = st.text_input("请输入成员姓名")
    if member:
        if member in bands[band]:
            st.success(f"{member}的生日是：{birthdays[member]}")
        else:
            st.error("成员不属于该乐队或不存在")

# To run the application, use the following command:
# streamlit run 邦邦角色生日查找器_web.py/daicijun/Downloads/ngrok config add-authtoken YOUR_AUTHTOKEN