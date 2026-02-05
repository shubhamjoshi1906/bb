import streamlit as st

st.set_page_config(page_title="Only For You 💖", layout="centered")

# ---------------- SESSION STATE ----------------
if "step" not in st.session_state:
    st.session_state.step = 0
if "name" not in st.session_state:
    st.session_state.name = ""
if "music_on" not in st.session_state:
    st.session_state.music_on = False

# ---------------- STYLES ----------------
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #ffe6eb, #fff5f8);
}
h1, h2, h3 {
    font-family: Georgia, serif;
    text-align: center;
}
.fade {
    animation: fadeIn 1.8s ease-in;
}
@keyframes fadeIn {
    from {opacity: 0;}
    to {opacity: 1;}
}
#no-btn {
    position: absolute;
    animation: float 3s ease-in-out infinite;
}
@keyframes float {
    0% {transform: translateY(0);}
    50% {transform: translateY(-18px);}
    100% {transform: translateY(0);}
}
</style>
""", unsafe_allow_html=True)

# ---------------- MUSIC (100% RELIABLE) ----------------
if st.session_state.music_on:
    st.audio(
        "https://cdn.pixabay.com/audio/2022/08/23/audio_7f3c75cfc5.mp3",
        loop=True
    )
    st.caption("🎶 our little background song")

# ---------------- STEP 0 : ENTRY ----------------
if st.session_state.step == 0:
    st.markdown("<h1 class='fade'>🌸 Hey you 🌸</h1>", unsafe_allow_html=True)
    st.markdown("<h3>This place is not for everyone.</h3>", unsafe_allow_html=True)

    password = st.text_input("Say the magic words 💕", type="password")

    if password:
        if password.lower() == "khushi khushi":
            st.success("He smiled when you typed that 😌")

            if st.button("Play our song & enter 💖"):
                st.session_state.music_on = True
                st.session_state.step = 1
                st.rerun()
        else:
            st.error("Nope. Try again 😌")

# ---------------- STEP 1 : NAME (ROMANTIC UPGRADE) ----------------
elif st.session_state.step == 1:
    st.markdown("<h1 class='fade'>Before we go further…</h1>", unsafe_allow_html=True)
    st.markdown(
        "<h3>Ohhh… he already had a name in his mind 😌</h3>",
        unsafe_allow_html=True
    )
    st.markdown(
        "<h3>But he wants to hear it from you.</h3>",
        unsafe_allow_html=True
    )

    name = st.text_input("So tell me… 🥺")

    if name and st.button("Okay 💕"):
        st.session_state.name = name
        st.session_state.step = 2
        st.rerun()

# ---------------- STEP 2 : THE QUESTION ----------------
elif st.session_state.step == 2:
    st.markdown(
        f"""
        <h1 class='fade'>{st.session_state.name} 💖</h1>
        <h2>One honest question…</h2>
        <h2>Are you Shubham’s girlfriend?</h2>
        """,
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:
        if st.button("damn yas 😍"):
            st.balloons()
            st.session_state.step = 3
            st.rerun()

    with col2:
        st.markdown("""
        <button id="no-btn" onmouseover="escape()">no 😒</button>

        <script>
        function escape() {
            const btn = document.getElementById("no-btn");
            const x = Math.random() * (window.innerWidth - 120);
            const y = Math.random() * (window.innerHeight - 120);
            btn.style.left = x + "px";
            btn.style.top = y + "px";
        }
        </script>
        """, unsafe_allow_html=True)

# ---------------- STEP 3 : FINAL ----------------
elif st.session_state.step == 3:
    st.markdown(
        f"""
        <h1 class='fade'>Okay {st.session_state.name}…</h1>
        <h2>You already know this.</h2>

        <h1>
        He calls you<br><br>
        cutiee 💕<br>
        baby 🥺<br>
        boobysauras 🦖<br><br>
        </h1>

        <h1 style="color:#e60073;">
        and always…<br><br>
        M I N E ❤️
        </h1>

        <h3>— not just words.</h3>
        """,
        unsafe_allow_html=True
    )
