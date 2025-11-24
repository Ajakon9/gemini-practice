import streamlit as st
import datetime
import time
from openai import OpenAI # AIと話すための電話機

# --- 1. AIサーバーへの接続設定 ---
# ここがポイント！ OpenAIの本家ではなく、あなたのMac(LM Studio)に繋ぎます
client = OpenAI(
    base_url="http://localhost:1234/v1", # LM Studioの住所
    api_key="lm-studio", # パスワードは何でもOK
)

# --- 2. 設定とデザイン（いつものサイバー風） ---
st.set_page_config(page_title="AI Fortune System", page_icon="🤖", layout="wide")

st.markdown("""
    <style>
    .stApp { font-family: 'Menlo', monospace; }
    .main-title {
        font-size: 3em; color: #00FFFF; text-align: center;
        text-shadow: 0 0 10px #00FFFF; margin-bottom: 0;
    }
    .result-box {
        border: 1px solid #00FFFF; padding: 30px; border-radius: 10px;
        background-color: rgba(0, 30, 30, 0.8); text-align: center;
        margin-top: 30px; width: 90%; margin-left: auto; margin-right: auto;
    }
    .event-text {
        color: #fff; font-size: 1.5em; font-weight: bold;
        margin: 20px 0; line-height: 1.4;
    }
    .ai-comment {
        color: #aaa; font-size: 1.1em; margin-top: 20px;
        text-align: left; padding-left: 30px; border-left: 4px solid #00FFFF;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<h1 class="main-title">SYSTEM: FORTUNE (LOCAL AI)</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center; color:#00FF00;">接続先: Localhost (LM Studio) // 完全無料モード</p>', unsafe_allow_html=True)

st.divider()

# --- 3. 入力エリア ---
col1, col2, col3 = st.columns([1, 3, 1])
with col2:
    user_constellation = st.selectbox("対象星座", [
        "おひつじ座", "おうし座", "ふたご座", "かに座", "しし座", "おとめ座",
        "てんびん座", "さそり座", "いて座", "やぎ座", "みずがめ座", "うお座"
    ])
    user_blood = st.selectbox("血液型", ["A型", "B型", "O型", "AB型", "不明"])
    
    if st.button("AI解析開始 (GENERATE)", use_container_width=True):
        
        # プログレスバー演出
        progress_text = "Local AI Loading..."
        my_bar = st.progress(0, text=progress_text)
        for i in range(100):
            time.sleep(0.01)
            my_bar.progress(i + 1)
        my_bar.empty()

        # --- 4. AIへの命令（プロンプト）を作成 ---
        # ここでAIへの「役割」と「やってほしいこと」を文章で指示します
        prompt = f"""
        あなたは「少し意地悪だが、どこか愛のある関西弁の占い師AI」として振る舞ってください。
        以下のユーザーの今日の運勢を占ってください。

        ユーザー情報: {user_constellation}, {user_blood}
        
        【出力のルール】
        1. 「ラッキーアイテム」や「ラッキーカラー」ではなく、**「地味に嫌な予言（オチ）」**を1つ考えてください。
           （例：靴下に穴が開く、Wifiが遅い、など）
        2. その後に、関西弁で「でも、ええやん。〇〇やん。」と無理やりポジティブに励ますコメントをしてください。
        3. JSON形式ではなく、ただのテキストで、以下のフォーマットで出力してください。

        フォーマット:
        予言：[ここに地味に嫌な予言]
        コメント：[ここに関西弁の励まし]
        """

        # --- 5. AIに送信して答えを待つ ---
        try:
            # ここでMac内のLM Studioに通信が飛びます！
            response = client.chat.completions.create(
                model="local-model", # 名前は何でもOK
                messages=[
                    {"role": "system", "content": "あなたは優秀なユーモアあふれるAIです。"},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7, # 創造性の度合い（高いほどランダム）
            )
            
            # AIからの返事を取り出す
            ai_content = response.choices[0].message.content

            # 結果表示
            result_html = f"""
            <div class="result-box">
                <h2 style="color: #00FF00;">AI GENERATED RESULT</h2>
                <hr style="border-color: #00FFFF; opacity: 0.3;">
                <div style="text-align: left; color: white; white-space: pre-wrap;">{ai_content}</div>
            </div>
            """
            st.markdown(result_html, unsafe_allow_html=True)
            st.balloons()

        except Exception as e:
            st.error(f"エラー発生！LM Studioのサーバーは起動していますか？\nエラー内容: {e}")