import streamlit as st
import random
import datetime
import time

# --- 1. 設定とデザイン（サイバーパンク風） ---
st.set_page_config(page_title="AI Fortune System", page_icon="🤖")

# CSSで強制的に「黒×ネオン」の世界観を作る
st.markdown("""
    <style>
    /* 全体のフォントをデジタルっぽく */
    .stApp {
        font-family: 'Courier New', monospace;
    }
    /* タイトル（ネオン発光） */
    .main-title {
        font-size: 2.5em;
        color: #00FFFF; /* サイアンブルー */
        text-align: center;
        text-shadow: 0 0 10px #00FFFF, 0 0 20px #00FFFF;
        font-weight: bold;
        letter-spacing: 2px;
        margin-bottom: 0;
    }
    /* サブタイトル */
    .sub-text {
        text-align: center;
        color: #00FF00; /* ネオングリーン */
        font-size: 1.0em;
        margin-top: 0;
    }
    /* 結果表示ボックス（枠線付き） */
    .result-box {
        border: 2px solid #00FFFF;
        padding: 20px;
        border-radius: 5px;
        background-color: rgba(0, 255, 255, 0.05); /* 薄い青背景 */
        text-align: center;
        margin-top: 20px;
    }
    /* 大凶用の赤いボックス */
    .danger-box {
        border: 2px solid #FF0000;
        padding: 20px;
        border-radius: 5px;
        background-color: rgba(255, 0, 0, 0.1);
        text-align: center;
        margin-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# 画面表示
st.markdown('<h1 class="main-title">SYSTEM: FORTUNE</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-text">>>> AI運勢解析モジュール 起動中...<br>>>> 生体データと日付から未来事象を演算します。</p>', unsafe_allow_html=True)

st.divider()

# --- 2. 入力エリア（日本語化） ---
today = datetime.date.today()

# 日本語リストに戻す
constellations = [
    "おひつじ座", "おうし座", "ふたご座", "かに座", "しし座", "おとめ座",
    "てんびん座", "さそり座", "いて座", "やぎ座", "みずがめ座", "うお座"
]
blood_types = ["A型", "B型", "O型", "AB型", "不明"]

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    # 日付をデジタル時計っぽく表示
    st.markdown(f"<div style='text-align: center; color: #aaa; font-family: monospace;'>TARGET DATE: {today.strftime('%Y-%m-%d')}</div>", unsafe_allow_html=True)
    
    # 入力フォーム
    user_constellation = st.selectbox("対象星座データ (Target Sign)", constellations)
    user_blood = st.selectbox("血液型データ (Blood Type)", blood_types)
    
    st.write("") # 余白
    
    # ボタン
    if st.button("解析開始 (INITIALIZE)", use_container_width=True):
        
        # --- 3. 演出（データ解析風） ---
        # プログレスバーを表示
        progress_text = "Connecting to Database..."
        my_bar = st.progress(0, text=progress_text)

        for percent_complete in range(100):
            time.sleep(0.015) # スピード調整
            if percent_complete == 30:
                 my_bar.progress(percent_complete + 1, text="Analyzing Neural Network...")
            elif percent_complete == 60:
                 my_bar.progress(percent_complete + 1, text="Calculating Probabilities...")
            elif percent_complete == 90:
                 my_bar.progress(percent_complete + 1, text="Rendering Future Events...")
            else:
                 my_bar.progress(percent_complete + 1)
        
        time.sleep(0.3)
        my_bar.empty() # バーを消す

        # --- 4. ロジック（オチの生成） ---
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
        
        # 結果表示（HTMLでかっこよく組む）
        if draw <= 38:
            event = random.choice(bad_events)
            
            # AIシステムログ風の出力
            result_html = f"""
            <div class="result-box">
                <h2 style="color: #00FF00; margin:0; font-family: 'Courier New';">RESULT: POSITIVE (大吉)</h2>
                <hr style="border-color: #00FFFF; opacity: 0.3;">
                <p style="color: #fff; font-size: 1.2em;">予測事象: 「{event}」</p>
                <p style="color: #aaa; font-size: 0.9em; margin-top: 15px;">
                >> 許容範囲内ト判断シマス。<br>
                >> 総合評価: 大吉<br>
                >> "デモ エエヤン"
                </p>
            </div>
            """
            st.markdown(result_html, unsafe_allow_html=True)
            st.balloons()
            
        else:
            # 大凶（警告モード）
            result_html = f"""
            <div class="danger-box">
                <h2 style="color: #FF0000; margin:0; font-family: 'Courier New';">WARNING: CRITICAL (大凶)</h2>
                <hr style="border-color: #FF0000; opacity: 0.3;">
                <p style="color: #fff; font-size: 1.2em;">システムエラー発生。<br>回避不能ナ不運ガ予測サレマス。</p>
                <p style="color: #aaa; font-size: 0.9em; margin-top: 15px;">
                >> 推奨アクション: ドンマイ。<br>
                >> REBOOT REQUIRED.
                </p>
            </div>
            """
            st.markdown(result_html, unsafe_allow_html=True)
            st.snow()