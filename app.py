import streamlit as st
import numpy as np
import joblib

st.set_page_config(page_title="FuelIQ", page_icon="⛽", layout="centered")
model = joblib.load("models/fuel_model.pkl")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@700;800&family=Inter:wght@400;500;600;700&display=swap');

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

html, body,
[data-testid="stApp"],
[data-testid="stAppViewContainer"] {
    background: #060810 !important;
    font-family: 'Inter', sans-serif;
    color: #f1f5f9;
    overflow-x: hidden;
}

#MainMenu, footer, header,
[data-testid="stToolbar"],
[data-testid="stDecoration"],
[data-testid="stStatusWidget"] { display: none !important; }

.block-container {
    max-width: 580px !important;
    padding: 0 1.4rem 6rem !important;
    margin: 0 auto;
}

[data-testid="stVerticalBlock"] { position: relative; z-index: 2; }

/* ═══════════════════════════════════════
   ANIMATED BACKGROUND
═══════════════════════════════════════ */
[data-testid="stAppViewContainer"] {
    position: relative;
    overflow: hidden;
}

[data-testid="stAppViewContainer"]::before {
    content: '';
    position: fixed;
    top: -120px;
    left: 50%;
    transform: translateX(-50%);
    width: 700px;
    height: 340px;
    background: radial-gradient(ellipse at center, rgba(74,222,128,0.18) 0%, rgba(74,222,128,0.04) 45%, transparent 72%);
    pointer-events: none;
    z-index: 0;
    animation: auroraPulse 5s ease-in-out infinite;
    border-radius: 50%;
}

@keyframes auroraPulse {
    0%,100% { opacity: .7; transform: translateX(-50%) scaleY(1);   }
    50%      { opacity: 1;  transform: translateX(-50%) scaleY(1.12); }
}

.orb {
    position: fixed;
    border-radius: 50%;
    pointer-events: none;
    z-index: 0;
    animation: orbFloat linear infinite;
}
.orb1 {
    width: 320px; height: 320px;
    top: 30%; left: -160px;
    background: radial-gradient(circle, rgba(74,222,128,0.06) 0%, transparent 70%);
    animation-duration: 18s;
    animation-name: orbFloat1;
}
.orb2 {
    width: 260px; height: 260px;
    bottom: 20%; right: -120px;
    background: radial-gradient(circle, rgba(99,102,241,0.07) 0%, transparent 70%);
    animation-duration: 22s;
    animation-name: orbFloat2;
}
.orb3 {
    width: 180px; height: 180px;
    top: 60%; left: 40%;
    background: radial-gradient(circle, rgba(34,211,238,0.05) 0%, transparent 70%);
    animation-duration: 15s;
    animation-name: orbFloat3;
}

@keyframes orbFloat1 {
    0%,100% { transform: translateY(0px);   }
    50%      { transform: translateY(-40px); }
}
@keyframes orbFloat2 {
    0%,100% { transform: translateY(0px);  }
    50%      { transform: translateY(30px); }
}
@keyframes orbFloat3 {
    0%,100% { transform: translate(0,0);      }
    33%      { transform: translate(20px,-20px); }
    66%      { transform: translate(-15px,15px); }
}

/* ═══════════════════════════════════════
   HERO
═══════════════════════════════════════ */
.hero {
    text-align: center;
    padding: 3.6rem 0 2.6rem;
    animation: heroIn .8s cubic-bezier(.22,1,.36,1) both;
}
@keyframes heroIn {
    from { opacity:0; transform:translateY(-24px); }
    to   { opacity:1; transform:translateY(0); }
}

.hero-pill {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: rgba(74,222,128,0.1);
    border: 1px solid rgba(74,222,128,0.28);
    border-radius: 999px;
    padding: 6px 16px;
    font-size: 10.5px;
    font-weight: 700;
    letter-spacing: 1.8px;
    text-transform: uppercase;
    color: #4ade80;
    margin-bottom: 22px;
    text-shadow: 0 0 8px rgba(74,222,128,0.4); /* Glow added */
    animation: heroIn .8s cubic-bezier(.22,1,.36,1) .1s both;
}
.hero-dot {
    width: 7px; height: 7px;
    border-radius: 50%;
    background: #4ade80;
    box-shadow: 0 0 8px #4ade80;
    animation: dotPulse 2s ease-in-out infinite;
}
@keyframes dotPulse {
    0%,100% { box-shadow: 0 0 5px #4ade80;  transform: scale(1);    }
    50%      { box-shadow: 0 0 14px #4ade80; transform: scale(1.25); }
}

.hero-title {
    font-family: 'Syne', sans-serif;
    font-size: clamp(68px, 14vw, 96px);
    font-weight: 800;
    line-height: 1;
    letter-spacing: -3px;
    color: #ffffff;
    margin-bottom: 16px;
    filter: drop-shadow(0 0 15px rgba(74,222,128,0.3)); /* Glow added */
    animation: titleIn .9s cubic-bezier(.22,1,.36,1) .15s both;
    background: linear-gradient(135deg, #ffffff 0%, #ffffff 55%, #4ade80 56%, #22c55e 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}
@keyframes titleIn {
    from { opacity:0; transform:translateY(-16px) scale(.97); }
    to   { opacity:1; transform:translateY(0) scale(1); }
}

.hero-sub {
    font-size: 2500px;
    font-weight: 5000;
    color: #94a3b8;
    max-width: 520px; /* Slightly wider for a cleaner text wrap */
    margin: 0 auto;
    text-align: center !important; /* Forces the text itself to center */
    line-height: 1.7;
    text-shadow: 0 0 8px rgba(148,163,184,0.3); 
    animation: heroIn .8s cubic-bezier(.22,1,.36,1) .25s both;
}

/* ═══════════════════════════════════════
   FORM ALIGNMENT & GLOW
═══════════════════════════════════════ */
.clabel {
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: #4ade80;
    margin-bottom: 24px;
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 0 6px; /* ALIGNMENT FIX */
    text-shadow: 0 0 12px rgba(74,222,128,0.6); /* GLOW FIX */
}
.clabel::after {
    content:'';
    flex:1;
    height:1px;
    background: linear-gradient(90deg, rgba(74,222,128,.25), transparent);
}

.fw { 
    margin-bottom: 20px; 
    padding: 0 6px; /* ALIGNMENT FIX */
}
.frow {
    display:flex;
    justify-content:space-between;
    align-items:baseline;
    margin-bottom:8px;
}
.fname {
    font-size: 13.5px;
    font-weight: 600;
    color: #ffffff;
    letter-spacing: .1px;
    text-shadow: 0 0 10px rgba(255, 255, 255, 0.4); /* GLOW FIX */
}
.fhint {
    font-size: 11px;
    color: #94a3b8;
    font-weight: 500;
    text-shadow: 0 0 8px rgba(148, 163, 184, 0.3); /* GLOW FIX */
}

/* ── Number input ── */
[data-testid="stNumberInput"] { width:100%; }
[data-testid="stNumberInput"] > div {
    background: rgba(10,14,26,0.9) !important;
    border: 1.5px solid rgba(255,255,255,0.08) !important;
    border-radius: 11px !important;
    overflow: hidden;
    transition: border-color .2s, box-shadow .2s;
}
[data-testid="stNumberInput"] > div:focus-within {
    border-color: rgba(74,222,128,.55) !important;
    box-shadow: 0 0 0 3px rgba(74,222,128,.1), 0 0 20px rgba(74,222,128,.15) !important;
}
[data-testid="stNumberInput"] input {
    background: transparent !important;
    border: none !important;
    color: #f8fafc !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 15px !important;
    font-weight: 600 !important;
    padding: 11px 14px !important;
    box-shadow: none !important;
    border-radius: 0 !important;
    text-shadow: 0 0 8px rgba(255, 255, 255, 0.3) !important; /* GLOW FIX */
}
[data-testid="stNumberInput"] button {
    background: rgba(255,255,255,0.04) !important;
    border: none !important;
    border-left: 1.5px solid rgba(255,255,255,0.06) !important;
    color: #475569 !important;
    border-radius: 0 !important;
    transition: all .15s !important;
}
[data-testid="stNumberInput"] button:hover {
    background: rgba(74,222,128,.12) !important;
    color: #4ade80 !important;
}

/* ── Selectbox ── */
[data-testid="stSelectbox"] > div > div {
    background: rgba(10,14,26,0.9) !important;
    border: 1.5px solid rgba(255,255,255,0.08) !important;
    border-radius: 11px !important;
    color: #f8fafc !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 14.5px !important;
    font-weight: 600 !important;
    padding: 4px 8px !important;
    min-height: 44px !important;
    transition: border-color .2s, box-shadow .2s !important;
    text-shadow: 0 0 8px rgba(255, 255, 255, 0.3) !important; /* GLOW FIX */
}
[data-testid="stSelectbox"] > div > div:focus-within,
[data-testid="stSelectbox"] > div > div[aria-expanded="true"] {
    border-color: rgba(74,222,128,.55) !important;
    box-shadow: 0 0 0 3px rgba(74,222,128,.1), 0 0 20px rgba(74,222,128,.15) !important;
}
[data-testid="stSelectbox"] svg { color: #475569 !important; }

[data-testid="stSelectboxVirtualDropdown"],
div[role="listbox"] {
    background: #0f1422 !important;
    border: 1.5px solid rgba(255,255,255,.08) !important;
    border-radius: 13px !important;
    box-shadow: 0 24px 60px rgba(0,0,0,.75), 0 0 0 1px rgba(74,222,128,.05) !important;
    overflow: hidden;
    padding: 5px !important;
}
div[role="option"] {
    font-family: 'Inter', sans-serif !important;
    font-size: 13.5px !important;
    font-weight: 500 !important;
    color: #94a3b8 !important;
    padding: 9px 14px !important;
    border-radius: 8px !important;
    transition: all .12s !important;
}
div[role="option"]:hover,
div[role="option"][aria-selected="true"] {
    background: rgba(74,222,128,.1) !important;
    color: #f1f5f9 !important;
    text-shadow: 0 0 8px rgba(255,255,255,0.4) !important; /* GLOW FIX */
}

/* Hide Streamlit labels */
[data-testid="stWidgetLabel"],
[data-testid="stWidgetLabel"] p,
label { display: none !important; }

.form-note {
    font-size: 11.5px;
    color: #94a3b8;
    font-weight: 500;
    padding: 14px 6px 0; /* ALIGNMENT FIX */
    margin-top: 4px;
    border-top: 1px solid rgba(255,255,255,.04);
    text-shadow: 0 0 8px rgba(148, 163, 184, 0.3); /* GLOW FIX */
}

/* ═══════════════════════════════════════
   BUTTON
═══════════════════════════════════════ */
.stButton { margin-top: 10px; }
[data-testid="stButton"] > button {
    width: 100% !important;
    background: linear-gradient(135deg, #16a34a 0%, #4ade80 100%) !important;
    color: #021005 !important;
    font-family: 'Syne', sans-serif !important;
    font-size: 16px !important;
    font-weight: 800 !important;
    letter-spacing: .5px !important;
    border: none !important;
    border-radius: 13px !important;
    padding: 16px 28px !important;
    cursor: pointer !important;
    transition: transform .18s, box-shadow .18s, opacity .18s !important;
    box-shadow: 0 4px 24px rgba(74,222,128,.3), 0 1px 0 rgba(255,255,255,.12) inset !important;
    position: relative;
    overflow: hidden;
}
[data-testid="stButton"] > button::after {
    content:'';
    position:absolute;
    inset:0;
    background: linear-gradient(135deg, rgba(255,255,255,.18) 0%, transparent 60%);
    pointer-events:none;
}
[data-testid="stButton"] > button:hover {
    transform: translateY(-3px) !important;
    box-shadow: 0 10px 38px rgba(74,222,128,.45), 0 1px 0 rgba(255,255,255,.15) inset !important;
}
[data-testid="stButton"] > button:active {
    transform: translateY(-1px) !important;
}

/* ═══════════════════════════════════════
   RESULT CARD
═══════════════════════════════════════ */
.rcard {
    background: rgba(15,20,35,0.85);
    border: 1px solid rgba(255,255,255,.07);
    border-radius: 20px;
    padding: 26px 24px;
    margin-top: 18px;
    backdrop-filter: blur(12px);
    animation: resultIn .55s cubic-bezier(.22,1,.36,1) both;
    box-shadow: 0 24px 60px rgba(0,0,0,.5);
}
@keyframes resultIn {
    from { opacity:0; transform:translateY(22px) scale(.98); }
    to   { opacity:1; transform:translateY(0) scale(1); }
}

.rlabel {
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: #4ade80;
    margin-bottom: 18px;
    display: flex;
    align-items: center;
    gap: 10px;
    text-shadow: 0 0 10px rgba(74,222,128,0.5); /* GLOW FIX */
}
.rlabel::after {
    content:'';
    flex:1;
    height:1px;
    background: linear-gradient(90deg, rgba(74,222,128,.25), transparent);
}

.metrics {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
    margin-bottom: 16px;
}

.mbox {
    border-radius: 14px;
    padding: 20px 18px;
    animation: mboxIn .5s cubic-bezier(.22,1,.36,1) .1s both;
}
@keyframes mboxIn {
    from { opacity:0; transform:scale(.92) translateY(10px); }
    to   { opacity:1; transform:scale(1)   translateY(0); }
}
.mbox.g {
    background: linear-gradient(145deg, rgba(10,28,18,.95), rgba(12,34,20,.95));
    border: 1px solid rgba(74,222,128,.22);
    box-shadow: 0 0 30px rgba(74,222,128,.06) inset;
}
.mbox.v {
    background: linear-gradient(145deg, rgba(12,14,48,.95), rgba(16,18,58,.95));
    border: 1px solid rgba(99,102,241,.22);
    box-shadow: 0 0 30px rgba(99,102,241,.06) inset;
}

.mtag {
    font-size: 9.5px;
    font-weight: 700;
    letter-spacing: 2.5px;
    text-transform: uppercase;
    margin-bottom: 8px;
}
.mbox.g .mtag { color: #4ade80; text-shadow: 0 0 10px rgba(74,222,128,0.5); }
.mbox.v .mtag { color: #818cf8; text-shadow: 0 0 10px rgba(129,140,248,0.5); }

.mval {
    font-family: 'Syne', sans-serif;
    font-size: 40px;
    font-weight: 800;
    line-height: 1;
    letter-spacing: -1.5px;
    animation: countUp .6s cubic-bezier(.22,1,.36,1) .15s both;
}
@keyframes countUp {
    from { opacity:0; transform:translateY(12px); }
    to   { opacity:1; transform:translateY(0); }
}
.mbox.g .mval { color: #dcfce7; text-shadow: 0 0 15px rgba(220, 252, 231, 0.6); }
.mbox.v .mval { color: #e0e7ff; text-shadow: 0 0 15px rgba(224, 231, 255, 0.6); }
.munit { font-size: 11.5px; font-weight: 500; margin-top:5px; opacity:.6; }

/* verdict */
.verdict {
    border-radius: 13px;
    padding: 15px 18px;
    display: flex;
    align-items: center;
    gap: 13px;
    margin-bottom: 16px;
    animation: mboxIn .5s cubic-bezier(.22,1,.36,1) .2s both;
}
.verdict.gr { background: rgba(10,28,18,.9); border: 1px solid rgba(74,222,128,.22); }
.verdict.ok { background: rgba(12,14,48,.9); border: 1px solid rgba(99,102,241,.22); }
.verdict.lo { background: rgba(26,18,0,.9);  border: 1px solid rgba(234,179,8,.22);  }

.vico { font-size: 28px; flex-shrink:0; filter: drop-shadow(0 0 8px rgba(255,255,255,0.3)); }
.vhead { font-size:13.5px; font-weight:700; margin-bottom:3px; }
.verdict.gr .vhead { color:#86efac; text-shadow: 0 0 8px rgba(134,239,172,0.4); }
.verdict.ok .vhead { color:#a5b4fc; text-shadow: 0 0 8px rgba(165,180,252,0.4); }
.verdict.lo .vhead { color:#fde047; text-shadow: 0 0 8px rgba(253,224,71,0.4);  }
.vbody { font-size:12px; font-weight:500; color:#94a3b8; line-height:1.55; }

/* tips */
.tips {
    border-top: 1px solid rgba(255,255,255,.05);
    padding-top: 16px;
    animation: mboxIn .5s cubic-bezier(.22,1,.36,1) .3s both;
}
.tipslbl {
    font-size: 9.5px;
    font-weight: 700;
    letter-spacing: 2.5px;
    text-transform: uppercase;
    color: #d97706;
    margin-bottom: 12px;
    text-shadow: 0 0 8px rgba(217,119,6,0.4);
}
.tip { display:flex; gap:9px; margin-bottom:8px; align-items:flex-start; }
.tip:last-child { margin-bottom:0; }
.tipb { width:5px;height:5px;border-radius:50%;background:#d97706;margin-top:6px;flex-shrink:0; box-shadow: 0 0 6px #d97706;}
.tipt { font-size:12px;font-weight:500;color:#94a3b8;line-height:1.55; }

/* footer */
.pgfoot {
    text-align:center;
    font-size:11.5px;
    font-weight:500;
    color:#475569;
    padding:3.5rem 0 1rem;
    letter-spacing:.3px;
    animation: heroIn 1s cubic-bezier(.22,1,.36,1) .6s both;
}
.pgfoot em { color:#4ade80; font-style:normal; text-shadow: 0 0 8px rgba(74,222,128,0.4); }
</style>

<div class="orb orb1"></div>
<div class="orb orb2"></div>
<div class="orb orb3"></div>
""", unsafe_allow_html=True)

# ── HERO ─────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
    <div class="hero-pill"><span class="hero-dot"></span>ML-Powered &nbsp;·&nbsp; Indian Cars</div>
    <div class="hero-title">FuelIQ</div>
    <p class="hero-sub">Enter a few details about your car and instantly see how far it goes on every litre of fuel.</p>
</div>
""", unsafe_allow_html=True)

# ── FORM CARD ─────────────────────────────────────────────────────────────
st.markdown('<div class="clabel">Car Details</div>', unsafe_allow_html=True)

# Engine Size
st.markdown('<div class="fw"><div class="frow"><span class="fname">Engine Size</span><span class="fhint">in CC — bigger = more power, more fuel</span></div></div>', unsafe_allow_html=True)
engine = st.number_input("__e", label_visibility="collapsed", min_value=500, max_value=5000, value=1200, step=100)
st.markdown('<div style="height:14px"></div>', unsafe_allow_html=True)

# Cylinders — dropdown
st.markdown('<div class="fw"><div class="frow"><span class="fname">Number of Cylinders</span><span class="fhint">the power chambers of your engine</span></div></div>', unsafe_allow_html=True)
CYL_MAP = {
    "2  —  Micro / scooter engine":           2,
    "3  —  Small city car":                  3,
    "4  —  Most hatchbacks & sedans":        4,
    "5  —  Uncommon, some older Volvos":      5,
    "6  —  Mid-size SUV or premium sedan":    6,
    "8  —  Performance or muscle car":        8,
    "10 —  Supercar":                        10,
    "12 —  Hypercar / ultra-luxury":         12,
}
cyl_sel = st.selectbox("__c", list(CYL_MAP.keys()), index=2, label_visibility="collapsed")
cyl = CYL_MAP[cyl_sel]
st.markdown('<div style="height:14px"></div>', unsafe_allow_html=True)

# Fuel Type
st.markdown('<div class="fw"><div class="frow"><span class="fname">Fuel Type</span><span class="fhint">check your fuel cap if unsure</span></div></div>', unsafe_allow_html=True)
FUEL_MAP = {
    "Petrol  —  most common, red pump":          0,
    "Diesel  —  usually cheaper, green pump":    1,
    "CNG  —  compressed gas, cylinder in boot":  2,
}
fuel_sel = st.selectbox("__f", list(FUEL_MAP.keys()), label_visibility="collapsed")
st.markdown('<div style="height:14px"></div>', unsafe_allow_html=True)

# Drivetrain
st.markdown('<div class="fw"><div class="frow"><span class="fname">Drive Type</span><span class="fhint">which wheels push the car</span></div></div>', unsafe_allow_html=True)
DRIVE_MAP = {
    "FWD  —  Front Wheel Drive, most cars":        0,
    "RWD  —  Rear Wheel Drive, sports / luxury":   1,
    "AWD  —  All Wheel Drive, SUVs":               2,
}
drive_sel = st.selectbox("__d", list(DRIVE_MAP.keys()), label_visibility="collapsed")

st.markdown('<p class="form-note">💡 Not sure about drivetrain? FWD covers 90 % of everyday Indian cars.</p>', unsafe_allow_html=True)

# ── BUTTON ───────────────────────────────────────────────────────────────
st.markdown('<div style="height:12px"></div>', unsafe_allow_html=True)
go = st.button("Calculate Fuel Efficiency →", use_container_width=True)

# ── RESULTS ──────────────────────────────────────────────────────────────
if go:
    data    = np.array([[engine, cyl, FUEL_MAP[fuel_sel], DRIVE_MAP[drive_sel]]])
    mileage = model.predict(data)[0]
    fc      = 100 / mileage

    if mileage > 20:
        vc,vi,vh = "gr","🏅","Outstanding Efficiency"
        vb = f"At ₹100/L you're spending ~₹{100/mileage:.0f} per km. Your car sips fuel like a champ — perfect for daily commutes."
    elif mileage > 15:
        vc,vi,vh = "ok","👌","Decent Mileage"
        vb = "A solid balance of power and economy. Smooth driving habits can push this even higher."
    else:
        vc,vi,vh = "lo","⚠️","Fuel-Hungry Engine"
        vb = "Normal for larger or older engines. Regular servicing and gentle acceleration will help a lot."

    st.markdown(f"""
    <div class="rcard">
        <div class="rlabel">Your Results</div>
        <div class="metrics">
            <div class="mbox g">
                <div class="mtag">Mileage</div>
                <div class="mval">{mileage:.1f}</div>
                <div class="munit">km / litre</div>
            </div>
            <div class="mbox v">
                <div class="mtag">Consumption</div>
                <div class="mval">{fc:.1f}</div>
                <div class="munit">litres / 100 km</div>
            </div>
        </div>
        <div class="verdict {vc}">
            <div class="vico">{vi}</div>
            <div>
                <div class="vhead">{vh}</div>
                <div class="vbody">{vb}</div>
            </div>
        </div>
        <div class="tips">
            <div class="tipslbl">Tips to stretch every litre</div>
            <div class="tip"><div class="tipb"></div><span class="tipt">Keep tyre pressure at recommended levels — low pressure wastes 2–3 km/L.</span></div>
            <div class="tip"><div class="tipb"></div><span class="tipt">Service your engine every 5,000–10,000 km for peak efficiency.</span></div>
            <div class="tip"><div class="tipb"></div><span class="tipt">Accelerate smoothly — aggressive starts cut mileage by up to 15 %.</span></div>
            <div class="tip"><div class="tipb"></div><span class="tipt">Limit AC in stop-and-go traffic — it drops mileage by 10–20 %.</span></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ── FOOTER ───────────────────────────────────────────────────────────────
st.markdown('<div class="pgfoot">Machine Learning &nbsp;·&nbsp; Indian Car Dataset &nbsp;·&nbsp; <em>FuelIQ</em></div>', unsafe_allow_html=True)