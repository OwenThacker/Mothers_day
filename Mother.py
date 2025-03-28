import streamlit as st
import os
import time
from PIL import Image, ImageFile
import random
import base64

# Allow truncated images to load
ImageFile.LOAD_TRUNCATED_IMAGES = True

# Function to add custom CSS
def add_bg_from_url():
    st.markdown(
        f"""
        <style>
            .stApp {{
                background: linear-gradient(to bottom, #ffe6f2, #ffcccc);
                background-size: cover;
            }}
            .title {{
                font-family: 'Comic Sans MS', cursive, sans-serif;
                color: #FF69B4;
                text-align: center;
                font-size: 3rem;
                text-shadow: 2px 2px 4px #ffffff;
                animation: pulse 2s infinite;
            }}
            @keyframes pulse {{
                0% {{
                    transform: scale(1);
                }}
                50% {{
                    transform: scale(1.05);
                }}
                100% {{
                    transform: scale(1);
                }}
            }}
            .subtitle {{
                font-family: 'Comic Sans MS', cursive, sans-serif;
                color: #FF1493;
                text-align: center;
                font-size: 1.2rem;
                margin-bottom: 30px;
            }}
            .image-container {{
                border-radius: 15px;
                box-shadow: 0 0 20px rgba(0, 0, 0, 0.2);
                overflow: hidden;
                position: relative;
                margin: 20px auto;
                max-width: 80%;
            }}
            .heart {{
                position: fixed;
                animation: float 6s ease-in infinite;
                z-index: -1;
                opacity: 0.7;
            }}
            @keyframes float {{
                0% {{ transform: translateY(0px); opacity: 0; }}
                50% {{ opacity: 0.7; }}
                100% {{ transform: translateY(-100vh); opacity: 0; }}
            }}
            .message-box {{
                background-color: rgba(255, 255, 255, 0.8);
                border-radius: 10px;
                padding: 20px;
                margin: 20px auto;
                max-width: 80%;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }}
            .audio-player {{
                background-color: rgba(255, 192, 203, 0.3);
                border-radius: 10px;
                padding: 10px;
                margin: 20px auto;
                max-width: 80%;
            }}
            .stAudio {{
                margin: 0 auto;
            }}
            .custom-footer {{
                position: fixed;
                bottom: 5px;
                width: 100%;
                text-align: center;
                color: #FF69B4;
                font-family: 'Comic Sans MS', cursive, sans-serif;
                font-size: 0.8rem;
                opacity: 0.7;
            }}
        </style>
        """,
        unsafe_allow_html=True
    )

    # Add floating hearts
    heart_sizes = [15, 20, 25, 30, 35]
    heart_colors = ["#FF69B4", "#FF1493", "#FF6B8B", "#FF5E78", "#FF4757"]
    
    for i in range(15):
        size = random.choice(heart_sizes)
        color = random.choice(heart_colors)
        left = random.randint(0, 100)
        duration = random.randint(10, 20)
        delay = random.randint(0, 10)
        
        st.markdown(
            f"""
            <div class="heart" style="left: {left}vw; animation-duration: {duration}s; animation-delay: {delay}s;">
                <svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="{color}">
                    <path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/>
                </svg>
            </div>
            """,
            unsafe_allow_html=True
        )

# Set up the Streamlit app
add_bg_from_url()

# Title with HTML for styling
st.markdown('<h1 class="title">💖 Happy Mother\'s Day! 💖</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">For the most amazing mum in the world</p>', unsafe_allow_html=True)

# Load images from the 'images' folder
image_folder = "images"
if os.path.exists(image_folder):
    image_files = [
        os.path.join(image_folder, f) for f in os.listdir(image_folder) 
        if f.lower().endswith(("jpg", "jpeg", "png"))
    ]
else:
    st.warning(f"Image folder '{image_folder}' not found. Please create it and add your images.")
    image_files = []

# Personal message
st.markdown(
    '<div class="message-box">'
    '<p style="font-family: \'Comic Sans MS\', cursive; text-align: center; color: #FF1493;">'
    'Happy Mother\'s Day, Mum! You said not to get you a card, so I didn\'t. '
    'Cards are old anyway, like you said you\'d just throw them in the bin, '
    'so I wanted to give you something you couldn\'t throw away, and that hopefully you won\'t delete. '
    '<br><br>'
    'Your love and support have meant everything to me, and this is just a small '
    'way to show how much I appreciate you. '
    '<br><br>'
    'I hope you will love this as much as we do you. '
    'Lots of Love from Owen xoxoxo'
    '</p>'
    '</div>',
    unsafe_allow_html=True
)

# Display the personal recorded voice message
st.markdown('<div class="audio-player">', unsafe_allow_html=True)
st.markdown('<p style="text-align: center; color: #FF1493;">Click play to hear my message to you ❤️</p>', unsafe_allow_html=True)

# Check if the personal recorded message exists
audio_file = "owen_mothers_day_message.mp3"
if os.path.exists(audio_file):
    # Create a more mobile-friendly audio element
    st.markdown(
        f"""
        <audio controls style="width: 100%;">
            <source src="data:audio/mp3;base64,{base64.b64encode(open(audio_file, 'rb').read()).decode()}" type="audio/mp3">
            Your browser does not support the audio element.
        </audio>
        """,
        unsafe_allow_html=True
    )
else:
    st.error(f"Audio file '{audio_file}' not found. Please ensure it's in the same directory as this script.")

st.markdown('</div>', unsafe_allow_html=True)

# Add a container for the image with styling
st.markdown('<div class="image-container">', unsafe_allow_html=True)
image_display = st.empty()
st.markdown('</div>', unsafe_allow_html=True)

st.markdown(
    '<p style="text-align: center; font-family: \'Comic Sans MS\', cursive; color: #FF1493; margin-top: 20px;">'
    'Our special memories together ❤️'
    '</p>',
    unsafe_allow_html=True
)

# Progress bar for the slideshow
progress_bar = st.progress(0)

# Add a small footer
st.markdown(
    '<div class="custom-footer">Made with love for Mother\'s Day 2025</div>',
    unsafe_allow_html=True
)

try:
    # Infinite loop for slideshow
    counter = 0
    while True:
        for i, image_file in enumerate(image_files):
            if not image_files:
                time.sleep(1)
                continue
                
            try:
                img = Image.open(image_file)
                # Check if rotation is needed based on EXIF data
                try:
                    # Attempt to get orientation from EXIF
                    exif = img._getexif()
                    if exif and 274 in exif:  # 274 is the EXIF tag for orientation
                        orientation = exif[274]
                        if orientation == 3:
                            img = img.rotate(180, expand=True)
                        elif orientation == 6:
                            img = img.rotate(270, expand=True)
                        elif orientation == 8:
                            img = img.rotate(90, expand=True)
                    else:
                        # If no EXIF data, apply your original rotation
                        img = img.rotate(-90)
                except:
                    # If error reading EXIF, apply your original rotation
                    img = img.rotate(-90)
                
                # Display the image in the placeholder (replaces previous one)
                image_display.image(img, use_container_width=True)
                
                # Update progress bar
                progress = (i + 1) / len(image_files)
                progress_bar.progress(progress)
                
                # Sleep to show image for a while
                time.sleep(3)
                
            except Exception as e:
                st.error(f"Error loading image {image_file}: {e}")
        
        # Reset progress bar for next cycle
        progress_bar.progress(0)
        
        # Increment counter to prevent infinite loops in development
        counter += 1
        if counter > 100 and not st.session_state.get("confirmed_loop"):
            if st.button("Continue Slideshow"):
                st.session_state["confirmed_loop"] = True
                counter = 0
            else:
                break

except KeyboardInterrupt:
    st.write("Slideshow stopped.")