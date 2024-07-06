import streamlit as st
from PIL import Image
from helmet_detect import YoloDetect
import os


detect = YoloDetect()
st.title("Helmet detection Application")
col1, col2 = st.columns(2)

with col1:
    st.title('Input data: ')
    file = st.file_uploader("Upload file: ", type=['jpg', 'png', 'mp4'])
    if file is not None:
        file_type = file.type
        if file_type in ["image/jpeg", "image/png"]:
            image = Image.open(file)
            st.image(image)
        elif file_type == "video/mp4":
            video_path = './video.mp4'
            with open(video_path, "wb") as f:
                f.write(file.getbuffer())
            st.video(video_path)
        config_threshold = st.slider("Config Threshold:", 1, 100, 50)
        config_threshold = config_threshold/100


btn = st.button("Detect")

with col2:
    st.title('Result:')
    if btn:
        if file_type in ["image/jpeg", "image/png"]:
            result = detect.detect_image(image, config_threshold)
            read_cuccessed = st.image(result, caption='Detected Image')
            if read_cuccessed:
                print('read image cusseced!')

        elif file_type == "video/mp4":
            with st.spinner('Detecting...'):
                result = detect.detect_video(file, config_threshold)
                video_successed = st.video(result)
                if video_successed:
                    print('detect successed')
                    os.remove(video_path)
