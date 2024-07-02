from ultralytics import YOLOv10
import os
import tempfile
import cv2


class YoloDetect:
    def __init__(self, weight_file: str = "weights_helmet/best.pt"):
        self.weight_file = weight_file
        self.model = YOLOv10(self.weight_file)
        self.conf_threshold = 50

    def detect_image(self, image, show: bool = False, save: bool = False):
        result = self.model.predict(image, show=show)
        annotated_img = result[0].plot()
        result_img = annotated_img[:, :, ::-1]

        return result_img

    def detect_video(self, video):
        video_path = tempfile.mktemp(suffix=".mp4")
        with open(video_path, "wb") as f:
            f.write(video.getvalue())

        cap = cv2.VideoCapture(video_path)

        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = cap.get(cv2.CAP_PROP_FPS)

        output_path = tempfile.mktemp(suffix=".mp4")
        print(output_path)
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

        while True:
            ret, frame = cap.read()

            if not ret:
                break

            processed_frame = self.model.predict(source=frame)[0]

            if isinstance(processed_frame, list) and 'bbox' in processed_frame[0]:
                for item in processed_frame:
                    bbox = item['bbox']
                    label = item['label']
                    score = item['score']

                    cv2.rectangle(frame, (int(bbox[0]), int(bbox[1])), (int(
                        bbox[2]), int(bbox[3])), color=(0, 255, 0), thickness=2)
                    cv2.putText(frame, f'{label}: {score:.2f}', (int(bbox[0]), int(
                        bbox[1]-10)), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color=(0, 255, 0))

            out.write(frame)

        cap.release()
        out.release()

        return output_path
