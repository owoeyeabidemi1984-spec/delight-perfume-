# app.py  (Streamlit version)
# Delight Cosmetic and Beauty Shop
# No 6, Balqis Jumoke Street, Fate, Ilorin, Kwara State
#
# Run locally:   streamlit run app.py
# Put logo.png in the same folder as this file (optional).

import os
from urllib.parse import quote

import streamlit as st

# ------------------------------------------------------------------
# SETTINGS - CHANGE THESE
# ------------------------------------------------------------------
# WhatsApp number: country code + number, no "+" and no spaces
WHATSAPP_NUMBER = "2348012345678"

SHOP_NAME = "Delight Cosmetic and Beauty Shop"
SHOP_ADDRESS = "No 6, Balqis Jumoke Street, Fate, Ilorin, Kwara State"

# Your perfumes and prices - add or change any item here
PERFUMES = [
    {"name": "Oud Royal Perfume", "size": "100ml", "price": 15000, "category": "Unisex", "image": "🌸"},
    {"name": "Floral Blush Perfume", "size": "100ml", "price": 12000, "category": "Ladies", "image": "🌷"},
    {"name": "Ocean Fresh Perfume", "size": "100ml", "price": 10000, "category": "Men", "image": "🌊"},
    {"name": "Vanilla Dream Perfume", "size": "50ml", "price": 8000, "category": "Ladies", "image": "🍦"},
    {"name": "Musk Classic Perfume", "size": "100ml", "price": 18000, "category": "Unisex", "image": "✨"},
    {"name": "Strawberry Sweet Perfume", "size": "50ml", "price": 7500, "category": "Ladies", "image": "🍓"},
    {"name": "Leather Bold Perfume", "size": "100ml", "price": 20000, "category": "Men", "image": "🔥"},
    {"name": "Jasmine Gold Perfume", "size": "100ml", "price": 16500, "category": "Ladies", "image": "🌼"},
]

PLACEHOLDER = "-- Choose Perfume --"
PERFUME_BY_NAME = {p["name"]: p for p in PERFUMES}

# ------------------------------------------------------------------
# PAGE CONFIG + STYLE
# ------------------------------------------------------------------
st.set_page_config(page_title=SHOP_NAME, page_icon="💖", layout="wide")

st.markdown(
    """
    <style>
        .stApp { background: #fff5f8; }
        .block-container { padding-top: 1rem; max-width: 1100px; }

        .top-bar {
            background: #8e0038; color: white;
            padding: 10px 15px; border-radius: 10px;
            display: flex; justify-content: space-between;
            align-items: center; gap: 10px; flex-wrap: wrap;
        }
        .top-bar .address { font-size: 13px; }
        .wa-btn {
            background: #25D366; color: white !important;
            text-decoration: none !important;
            padding: 10px 18px; border-radius: 50px;
            font-weight: bold; font-size: 14px; white-space: nowrap;
        }
        .wa-btn:hover { background: #1eb856; }

        .shop-title {
            color: #8e0038; text-align: center;
            text-transform: uppercase; font-size: 28px;
            font-weight: 800; margin: 10px 0 0 0;
        }
        .shop-sub { text-align: center; color: #666; margin: 4px 0; }

        .welcome {
            text-align: center; background: #ffe3ec;
            padding: 20px; border-radius: 12px; margin: 15px 0;
        }
        .welcome h2 { color: #8e0038; margin: 0; }
        .welcome p { margin-top: 8px; line-height: 1.6; }

        .emoji { font-size: 45px; text-align: center; }
        .p-name { color: #8e0038; font-weight: bold; text-align: center; font-size: 17px; }
        .p-info { text-align: center; color: #555; font-size: 14px; }
        .p-price { text-align: center; font-size: 20px; font-weight: bold; color: green; margin: 6px 0; }
        .tag {
            display: block; width: fit-content; margin: 0 auto 8px auto;
            background: #eee; padding: 3px 10px; border-radius: 20px; font-size: 12px;
        }

        .footer { text-align: center; padding: 20px; color: #777; font-size: 13px; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ------------------------------------------------------------------
# SESSION STATE + CALLBACKS
# ------------------------------------------------------------------
if "product_select" not in st.session_state:
    st.session_state["product_select"] = PLACEHOLDER


def choose_perfume(name: str) -> None:
    """Called when a customer clicks 'Order This Perfume' on a card."""
    st.session_state["product_select"] = name
    st.toast(f"{name} selected - scroll down to the order form 👇")


def whatsapp_link(text: str) -> str:
    """Build a safe wa.me link (handles spaces, ₦, &, #, new lines...)."""
    return f"https://wa.me/{WHATSAPP_NUMBER}?text={quote(text)}"


# ------------------------------------------------------------------
# TOP BAR (WhatsApp button at the extreme top right)
# ------------------------------------------------------------------
top_wa = whatsapp_link("Hello Delight Shop! I want to order for home delivery")
st.markdown(
    f"""
    <div class="top-bar">
        <div class="address">📍 {SHOP_ADDRESS}</div>
        <a class="wa-btn" href="{top_wa}" target="_blank">💬 WhatsApp Us - Home Delivery</a>
    </div>
    """,
    unsafe_allow_html=True,
)

# ------------------------------------------------------------------
# HEADER / LOGO
# ------------------------------------------------------------------
logo_path = next(
    (p for p in ("logo.png", "static/logo.png") if os.path.exists(p)), None
)
_, logo_col, _ = st.columns([2, 1, 2])
with logo_col:
    if logo_path:
        st.image(logo_path, use_container_width=True)
    else:
        st.markdown("<div class='emoji'>💖</div>", unsafe_allow_html=True)

st.markdown(f"<div class='shop-title'>{SHOP_NAME}</div>", unsafe_allow_html=True)
st.markdown(f"<div class='shop-sub'>{SHOP_ADDRESS}</div>", unsafe_allow_html=True)
st.markdown(
    f"<div class='shop-sub'>📞 WhatsApp: {WHATSAPP_NUMBER} | 🛵 Fast Home Delivery in Ilorin</div>",
    unsafe_allow_html=True,
)

# ------------------------------------------------------------------
# WELCOME MESSAGE
# ------------------------------------------------------------------
st.markdown(
    f"""
    <div class="welcome">
        <h2>Welcome to {SHOP_NAME}! 💖</h2>
        <p>Thank you for visiting us. We sell original and long-lasting perfumes
        at the best prices in Fate, Ilorin.<br>
        Choose your favourite perfume below, fill in your phone number and address,
        and we will deliver to your doorstep.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# ------------------------------------------------------------------
# PERFUME GRID
# ------------------------------------------------------------------
COLS_PER_ROW = 4
for start in range(0, len(PERFUMES), COLS_PER_ROW):
    row = PERFUMES[start:start + COLS_PER_ROW]
    cols = st.columns(COLS_PER_ROW)
    for col, p in zip(cols, row):
        with col:
            with st.container(border=True):
                st.markdown(f"<div class='emoji'>{p['image']}</div>", unsafe_allow_html=True)
                st.markdown(f"<div class='p-name'>{p['name']}</div>", unsafe_allow_html=True)
                st.markdown(
                    f"<div class='p-info'>{p['size']} - {p['category']}</div>",
                    unsafe_allow_html=True,
                )
                st.markdown(f"<div class='p-price'>₦{p['price']:,}</div>", unsafe_allow_html=True)
                st.markdown("<span class='tag'>In Stock</span>", unsafe_allow_html=True)
                st.button(
                    "Order This Perfume",
                    key=f"order_{start}_{p['name']}",
                    on_click=choose_perfume,
                    args=(p["name"],),
                    use_container_width=True,
                )

# ------------------------------------------------------------------
# ORDER FORM
# ------------------------------------------------------------------
st.markdown("---")
st.markdown(
    "<h2 style='color:#8e0038;text-align:center;'>🛒 Place Your Order - Home Delivery</h2>",
    unsafe_allow_html=True,
)

with st.form("order_form", clear_on_submit=False):
    name = st.text_input("Your Full Name", placeholder="e.g. Aisha Bello")
    phone = st.text_input("Phone Number", placeholder="e.g. 08012345678")
    product = st.selectbox(
        "Select Perfume",
        [PLACEHOLDER] + [p["name"] for p in PERFUMES],
        key="product_select",
        format_func=lambda n: n
        if n == PLACEHOLDER
        else f"{n} - ₦{PERFUME_BY_NAME[n]['price']:,}",
    )
    quantity = st.number_input("Quantity", min_value=1, value=1, step=1)
    address = st.text_area("Delivery Address", placeholder="e.g. No 10, Fate Road, Ilorin")
    submitted = st.form_submit_button("✅ Confirm Order on WhatsApp", use_container_width=True)

if submitted:
    errors = []
    if not name.strip():
        errors.append("Please enter your full name.")
    if not phone.strip():
        errors.append("Please enter your phone number.")
    elif sum(ch.isdigit() for ch in phone) < 10:
        errors.append("Please enter a valid phone number.")
    if product == PLACEHOLDER:
        errors.append("Please select a perfume.")
    if not address.strip():
        errors.append("Please enter your delivery address.")

    if errors:
        for e in errors:
            st.error(e)
    else:
        item = PERFUME_BY_NAME[product]
        total = item["price"] * int(quantity)
        wa_text = (
            f"Hello Delight Shop! My name is {name.strip()}. "
            f"I want to order {item['name']} ({item['size']}) x {int(quantity)} "
            f"- Total: ₦{total:,}. "
            f"My phone is {phone.strip()}. "
            f"My delivery address is: {address.strip()}"
        )
        # Orders are printed in the app logs. Replace with a database/Excel save if needed.
        print(f"NEW ORDER: {name} | {phone} | {item['name']} x {quantity} | {address}")

        st.success(
            f"Thank you {name.strip()}! Your order for {item['name']} x {int(quantity)} "
            f"(₦{total:,}) is ready. Tap the button below to send it on WhatsApp."
        )
        st.link_button(
            "💬 Send Order on WhatsApp",
            whatsapp_link(wa_text),
            use_container_width=True,
        )

# ------------------------------------------------------------------
# FOOTER
# ------------------------------------------------------------------
st.markdown(
    f"""
    <div class="footer">
        <b>{SHOP_NAME}</b><br>
        {SHOP_ADDRESS}<br>
        © 2026 {SHOP_NAME} - All Rights Reserved
    </div>
    """,
    unsafe_allow_html=True,
)
