import streamlit as st
from PIL import Image
from Object_Detection_with_Yolov10.helmet_detect import YoloDetect
import tempfile

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
        elif file_type == "video/mp4":
            video_path = tempfile.mktemp(suffix=".mp4")
            with open(video_path, "wb") as f:
                f.write(file.getvalue())
            st.video(video_path)


btn = st.button("Detect")

with col2:
    st.title('Result:')
    if btn:
        if file_type in ["image/jpeg", "image/png"]:
            result = detect.detect_image(image, save=True)
            st.image(result, caption='Detected Image')

        elif file_type == "video/mp4":
            result = detect.detect_video(file)
            st.video(result)
