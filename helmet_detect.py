from ultralytics import YOLOv10
import os
import tempfile
import cv2


class YoloDetect:
    def __init__(self, weight_file: str = "weights_helmet/best.pt"):
        self.weight_file = weight_file
        self.model = YOLOv10(self.weight_file)
        self.conf_threshold = 50

    def detect_image(self, image, conf_threshold=0.5):
        result = self.model.predict(image, conf=conf_threshold)
        annotated_img = result[0].plot()
        result_img = annotated_img[:, :, ::-1]

        return result_img

    def detect_video(self, video, conf_threshold=0.5):
        video_path = './video.webm'
        with open(video_path, 'wb') as f:
            f.write(video.getbuffer())

        cap = cv2.VideoCapture(video_path)

        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = cap.get(cv2.CAP_PROP_FPS)

        output_path = "./detected_video.webm"
        fourcc = cv2.VideoWriter_fourcc(*'vp80')
        out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

        while True:
            ret, frame = cap.read()

            if not ret:
                break

            processed_frame = self.model.track(
                source=frame, persist=True, conf=conf_threshold)

            annotated_frame = processed_frame[0].plot()

            out.write(annotated_frame)

        cap.release()
        out.release()
        cv2.destroyAllWindows()
        return output_path
