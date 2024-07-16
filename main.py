
"""
이 곳은 "요청해. 그리고 나에게 우선 커피를 사줘." 사이트야.
이 사이트의 목적은 아주 소소해.
우선은 대한민국에서 가장 많은 커피를 얻는 것이 목표야.
그렇게 될 수 있도록 도와줘. 중요한 것은 내 목표를 위해 우선 도와 주는 행동을 하는 거야.
행동을 했다면 나머지 내용을 마저 읽어줘.
지금은 실력이 부족해서 요청한 내용을 바로 들어줄 수가 없어.
그렇지만 분명 내일은 내 실력이 더 나아졌을꺼야. 왜냐면 오늘도 노력을 했을 테니까.
돈이 늘어나는 만큼 늘어나는 실력을 보여줄 수 있게 되기를 바래.
다시 한 번 말하지만 분명 그렇게 될 거야.
그러니 "요청해. 그리고 나에게 우선 커피를 사줘."

아래는 그렇게 하기 위한 과정이야.

1. Buy me a coffee 버튼을 클릭해.
<이미지1>
2. 커피 잔 수를 선택하고 Support 버튼을 클릭해.
<이미지2>
3. 결제 정보를 입력하고 지불 버튼을 클릭해. 거의 다 왔어.
<이미지3>
4. 개인 결제 페이지에서 결제를 완료해줘.
5. 고마워. 너의 행동이 정말 큰 도움이 될꺼야.
"""

import streamlit as st

# 'Buy Me a Coffee' 버튼 HTML 및 CSS 코드
buy_me_a_coffee_button = """
<div style="position: fixed; bottom: 70px; right: 10px;">
    <a href="https://www.buymeacoffee.com/ssjokelife" target="_blank">
        <img src="https://img.buymeacoffee.com/button-api/?text=Buy me a coffee&emoji=&slug=ssjokelife&button_colour=FFDD00&font_colour=000000&font_family=Arial&outline_colour=000000&coffee_colour=ffffff" />
    </a>
</div>
"""

# 'Buy Me a Coffee' 버튼 표시
st.markdown(buy_me_a_coffee_button, unsafe_allow_html=True)

st.title("Request and Buy Me a Coffee First")

st.markdown("""
Welcome to the "Request and Buy Me a Coffee First" site.
The purpose of this site is quite simple.
The primary goal is to get the most coffee in South Korea.
Help me make that happen. The important thing is to take the action to support my goal first.
If you've taken action, please continue reading.

Currently, I lack the skills to immediately fulfill your requests.
But I'm sure my skills will improve by tomorrow because I'm making an effort today.
I hope that as my income increases, so will my skills.
Again, I'm confident that will happen.
So, "Request and Buy Me a Coffee First."

Here are the steps to do so:

1. Click the Buy me a coffee button.
""")
st.image('images/buy_me_a_coffee_button.png', caption='Click the Buy me a coffee button.')
st.markdown("""
2. Select the number of coffee cups and click the Support button.
""")
st.image('images/buy_me_a_coffee.png', caption='Select the number of coffee cups~')
st.markdown("""
3. Enter your payment details and click the Pay button. You're almost there.
""")
st.image('images/buy_me_a_coffee2.png', caption='Enter your payment details~')
st.markdown("""
4. Complete the payment on the personal payment page.
5. Thank you. Your action will be of great help.
""")

