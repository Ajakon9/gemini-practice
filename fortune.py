import streamlit as st
import random
import datetime
import time

# --- 1. 設定とデザイン ---
st.set_page_config(page_title="AI Fortune System", page_icon="🤖")

# CSS（黒背景・ネオン推奨）
st.markdown("""
    <style>
    /* フォントを等幅にしてシステムっぽさを出す */
    .stApp {
        font-family: 'Menlo', 'Consolas', 'Courier New', monospace;
    }
    .main-title {
        font-size: 2.5em;
        color: #00FFFF;
        text-align: center;
        text-shadow: 0 0 10px #00FFFF;
        font-weight: bold;
        letter-spacing: 2px;
        margin-bottom: 0;
    }
    .sub-text {
        text-align: center;
        color: #00FF00;
        font-size: 0.9em;
        margin-top: 5px;
    }
    /* 結果表示ボックス（読みやすく調整） */
    .result-box {
        border: 1px solid #00FFFF;
        padding: 20px;
        border-radius: 8px;
        background-color: rgba(0, 30, 30, 0.8); /* 少し濃い背景 */
        text-align: center;
        margin-top: 20px;
        box-shadow: 0 0 15px rgba(0, 255, 255, 0.2);
    }
    .danger-box {
        border: 1px solid #FF4444;
        padding: 20px;
        border-radius: 8px;
        background-color: rgba(40, 0, 0, 0.8);
        text-align: center;
        margin-top: 20px;
        box-shadow: 0 0 15px rgba(255, 0, 0, 0.2);
    }
    /* 文字を見やすく */
    .event-text {
        color: #fff;
        font-size: 1.3em;
        font-weight: bold;
        margin: 15px 0;
        line-height: 1.5;
    }
    .ai-comment {
        color: #aaa;
        font-size: 1.0em;
        margin-top: 15px;
        text-align: left; /* ログっぽく左寄せ */
        padding-left: 20px;
        border-left: 3px solid #00FFFF; /* 左にアクセント線 */
    }
    .ai-comment-danger {
        color: #ffaaaa;
        font-size: 1.0em;
        margin-top: 15px;
        text-align: left;
        padding-left: 20px;
        border-left: 3px solid #FF4444;
    }
    </style>
    """, unsafe_allow_html=True)

# ヘッダー表示
st.markdown('<h1 class="main-title">SYSTEM: FORTUNE</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-text">AI運勢解析モジュール v3.0 // 起動準備完了</p>', unsafe_allow_html=True)

st.divider()

# --- 2. 入力エリア ---
today = datetime.date.today()
constellations = [
    "おひつじ座", "おうし座", "ふたご座", "かに座", "しし座", "おとめ座",
    "てんびん座", "さそり座", "いて座", "やぎ座", "みずがめ座", "うお座"
]
blood_types = ["A型", "B型", "O型", "AB型", "不明"]

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.markdown(f"<div style='text-align: center; color: #aaa; font-family: monospace;'>TARGET DATE: {today.strftime('%Y-%m-%d')}</div>", unsafe_allow_html=True)
    
    user_constellation = st.selectbox("対象星座データ", constellations)
    user_blood = st.selectbox("血液型データ", blood_types)
    
    st.write("")
    
    if st.button("解析開始 (INITIALIZE)", use_container_width=True):
        
        # --- 3. 演出 ---
        progress_text = "データベース接続中..."
        my_bar = st.progress(0, text=progress_text)

        for percent_complete in range(100):
            time.sleep(0.01) # 少し速くしました
            if percent_complete == 30:
                 my_bar.progress(percent_complete + 1, text="ニューラルネットワーク解析中...")
            elif percent_complete == 60:
                 my_bar.progress(percent_complete + 1, text="未来事象の確率変動を計算中...")
            elif percent_complete == 90:
                 my_bar.progress(percent_complete + 1, text="最終結果を出力します...")
            else:
                 my_bar.progress(percent_complete + 1)
        
        time.sleep(0.2)
        my_bar.empty()

        # --- 4. ロジック ---
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
        
        # 結果表示（日本語ログ風）
        if draw <= 38:
            event = random.choice(bad_events)
            
            result_html = f"""
            <div class="result-box">
                <h2 style="color: #00FF00; margin:0;">RESULT: POSITIVE (大吉)</h2>
                <hr style="border-color: #00FFFF; opacity: 0.3;">
                <div style="color: #ccc; font-size: 0.8em; text-align: left;">[INFO] 予測された事象:</div>
                <p class="event-text">「{event}」</p>
                <div class="ai-comment">
                    [ANALYSIS] 精神的ダメージ: 軽微<br>
                    [CONCLUSION] 許容範囲内です。<br>
                    [MESSAGE] <b>「でも、ええやん。大吉やん。」</b>
                </div>
            </div>
            """
            st.markdown(result_html, unsafe_allow_html=True)
            st.balloons()
            
        else:
            result_html = f"""
            <div class="danger-box">
                <h2 style="color: #FF4444; margin:0;">WARNING: CRITICAL (大凶)</h2>
                <hr style="border-color: #FF4444; opacity: 0.3;">
                <div style="color: #ccc; font-size: 0.8em; text-align: left;">[ALERT] システム警告:</div>
                <p class="event-text">回避不能な不運が予測されます。</p>
                <div class="ai-comment-danger">
                    [ANALYSIS] 精神的ダメージ: 甚大<br>
                    [Recomendation] 直ちに帰宅してください。<br>
                    [MESSAGE] <b>「ドンマイ。」</b>
                </div>
            </div>
            """
            st.markdown(result_html, unsafe_allow_html=True)
            st.snow()