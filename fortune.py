import streamlit as st
import random
import datetime
import time

# --- 1. 見た目の偽装（高級感を出す） ---
st.set_page_config(page_title="Celestial Guidance", page_icon="✨")

st.markdown("""
    <style>
    .main-title {
        font-size: 3em;
        color: #4B0082;
        text-align: center;
        font-family: 'Hiragino Mincho ProN', serif;
    }
    .sub-text {
        text-align: center;
        color: #555;
        font-size: 1.1em;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<h1 class="main-title">✨ 星読みの神託 ✨</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-text">古の星々の配置と、あなたの血脈から<br>今日の運命を正確に導き出します。</p>', unsafe_allow_html=True)

st.divider()

# --- 2. 入力エリア ---
today = datetime.date.today()
constellations = [
    "牡羊座 (Aries)", "牡牛座 (Taurus)", "双子座 (Gemini)", "蟹座 (Cancer)", 
    "獅子座 (Leo)", "乙女座 (Virgo)", "天秤座 (Libra)", "蠍座 (Scorpio)", 
    "射手座 (Sagittarius)", "山羊座 (Capricorn)", "水瓶座 (Aquarius)", "魚座 (Pisces)"
]
blood_types = ["Type A", "Type B", "Type O", "Type AB", "Unknown"]

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.caption(f"Date: {today.strftime('%Y.%m.%d')}")
    user_constellation = st.selectbox("Select Your Sign", constellations)
    user_blood = st.selectbox("Select Blood Type", blood_types)
    
    st.write("")
    
    if st.button("運命を紐解く (Reveal Destiny)", use_container_width=True):
        with st.spinner('星々と交信中... 宇宙のエネルギーを受信しています...'):
            time.sleep(2)

        bad_events = [
            "買ったばかりの白い服にカレーうどんが跳ねる", "上司を「お母さん」と呼んでしまう",
            "改札でSuicaの残高不足で止められる", "楽しみにしていたプリンを家族に食べられる",
            "スマホの充電が肝心な時に3%になる", "歩いていると靴紐が3回ほどける",
            "イヤホンのコードが知恵の輪みたいに絡まる", "美容院での会話が全く盛り上がらない",
            "自販機でお釣りを取ろうとして小銭をばら撒く", "傘を持って出た瞬間に雨が止む",
            "傘を忘れた瞬間に豪雨が降る", "トイレに入った瞬間に宅急便が来る",
            "寝癖が芸術的すぎて直らない", "エレベーターの閉まるボタンを押したら人が挟まる",
            "親指の爪の間を紙で切る", "PCがフリーズして3時間分の作業が消える",
            "好きな曲のサビの直前で電話がかかってくる", "味噌汁の豆腐が熱すぎて舌を火傷する",
            "小指をタンスの角に全力でぶつける", "知ってる人だと思って手を振ったら全然知らない人",
            "マスクの紐がプチンと切れる", "大事なプレゼン中にPCの更新プログラムが始まる",
            "隣の人の貧乏ゆすりが震度3レベル", "あくびをした瞬間に虫が口に入る",
            "コンビニで温めますか？と聞かれて「大丈夫です」と言ったのにお弁当",
            "USBの向きが何度やっても刺さらない", "電車で寝て起きたら、終点",
            "シャンプーだと思ったらコンディショナーだった", "レジで財布を出そうとしたらポイントカードしかなかった",
            "鼻毛が一本だけ長く伸びていることに夕方気づく", "靴の中に小石が入っているが、取るタイミングがない",
            "「あ、アレなんだっけ」で会話が終了する", "くしゃみをしたら腰に変な電気が走る",
            "夜中にふと思い出した黒歴史で叫びたくなる", "Wi-Fiのパスワードを3回間違えてロックされる",
            "頼んだランチだけ来るのが異常に遅い", "映画のいいシーンでトイレに行きたくなる",
            "ATMでお金を下ろそうとしたらメンテナンス中",
        ]

        seed_string = f"{today}-{user_constellation}-{user_blood}"
        random.seed(seed_string)
        draw = random.randint(1, 40)

        st.divider()
        
        if draw <= 38:
            event = random.choice(bad_events)
            result_text = f"大吉！<br>{event}、<br>でもええやん。<br>大吉やん。"
            st.markdown(f"<h2 style='text-align: center; color: #FF4B4B;'>🎉 {result_text}</h2>", unsafe_allow_html=True)
            st.balloons()
        else:
            st.markdown("<h2 style='text-align: center; color: #333;'>💀 大凶！...ドンマイ。</h2>", unsafe_allow_html=True)
            st.snow()