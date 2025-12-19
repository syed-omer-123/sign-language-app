# sign-language-app
🤟 Sign Language Converter

A real-time Sign Language Conversion web application that bridges communication gaps by converting hand gestures to text using a live camera and text to sign images.
Built using Streamlit, MediaPipe, and Machine Learning.

🚀 Features

🔹 Gesture → Text
Capture hand signs using a live camera
Extract hand landmarks using MediaPipe
Predict the sign using a trained ML model
Display the recognized sign instantly

🔹 Text → Gesture
Enter a supported word
View the corresponding sign image
Helpful for learning and reference


🧠 Supported Signs (Current Version)

⚠️ This is a demo version and supports only the following signs:
hello
yes
no
please
sorry
thankyou
love

🛠️ Tech Stack

Python
Streamlit (Web Interface)
MediaPipe (Hand Landmark Detection)
OpenCV
Scikit-learn (ML Model)
NumPy
Joblib
Pillow

📸 How It Works

The camera captures a hand image.
MediaPipe extracts 21 hand landmarks (x, y, z).
Landmarks are fed into a trained ML classifier.
The predicted sign is displayed as text.
For text input, pre-stored sign images are shown.

🌐 Live Demo

🔗 Deployed App:
👉 (Add your Streamlit Cloud URL here after deployment)

⚠️ Disclaimer
This project supports only static hand signs.
Accuracy depends on lighting and hand visibility.
Not intended for full sign language translation.
Designed for learning, demo, and accessibility awareness purposes.

⭐ Future Improvements

Add dynamic sign support (video-based)
Speech output for predicted text
More sign classes
Mobile-friendly optimizationz

👨‍💻 Author
Syed Omer Hussaini
🎓 Computer Science & Data Science
https://www.linkedin.com/in/syed-omer-hussaini-b023437a/
farazhussaini124@gmail.com
