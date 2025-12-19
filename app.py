import os
import streamlit as st
import cv2
import mediapipe as mp
import numpy as np
import joblib
from PIL import Image

# ---------------- LOAD MODEL ----------------
model = joblib.load("sign_model.pkl")
label_encoder = joblib.load("label_encoder.pkl")

SUPPORTED_SIGNS = list(label_encoder.classes_)

# ---------------- MEDIAPIPE ----------------
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7
)

# ---------------- UI ----------------
st.title("🤟 Sign Language Converter")

st.info(
    f"⚠️ **This demo supports only these signs:** {', '.join(SUPPORTED_SIGNS)}"
)

mode = st.radio(
    "Select Mode",
    ["Gesture → Text", "Text → Gesture"]
)

# ================= MODE 1 =================
if mode == "Gesture → Text":

    st.subheader("Capture a Hand Sign Using Camera")

    camera_image = st.camera_input("Take a photo")

    if camera_image:
        image = Image.open(camera_image)
        st.image(image, caption="Captured Image", width=300)

        img = np.array(image)
        rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        result = hands.process(rgb)

        if result.multi_hand_landmarks:
            hand = result.multi_hand_landmarks[0]
            landmarks = []

            for lm in hand.landmark:
                landmarks.extend([lm.x, lm.y, lm.z])

            landmarks = np.array(landmarks).reshape(1, -1)
            prediction = model.predict(landmarks)
            sign = label_encoder.inverse_transform(prediction)[0]

            st.success(f"✅ Predicted Sign: **{sign.upper()}**")

        else:
            st.error("❌ No hand detected. Please show a clear hand sign.")

# ================= MODE 2 =================
else:
    st.subheader("Text → Sign Image")

    text = st.text_input("Enter a word")

    if text:
        text = text.lower().strip()

        png_path = f"sign_images/{text}.png"
        jpg_path = f"sign_images/{text}.jpg"

        if os.path.exists(png_path):
            st.image(png_path, caption=f"Sign for '{text}'", width=300)

        elif os.path.exists(jpg_path):
            st.image(jpg_path, caption=f"Sign for '{text}'", width=300)

        else:
            st.error("❌ Sign not supported in this version.")
