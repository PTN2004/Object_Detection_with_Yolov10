# Object_Detection_with_Yolov10
 Object_Detection_with_Yolov10 is an AI project in the computer vision field. In this project, I use YOLOv10 to train custom data about detecting helmets using images or videos.
 
# Usage
## Intallation

**1. Clone the repository**

    git clone https://github.com/PTN2004/Object_Detection_with_Yolov10.git  
    cd Object_Detection_with_Yolov10.git

**2. (Option) Create and activate a visual environment**
*  For Unix/macOS:  

        python3 -m venv .venv  
        source .venv/bin/active
* For Windows:

        python -m venv venv
        .\venv\Scripts\activate

**3. Install the required dependencies:**

    pip install -r requirements.txt

**4. Clone the Repository of YOLOv10**
    
    git clone https://github.com/THU-MIG/yolov10.git

**5. Move the file helmet_detection, file UI_detect into the yolov10 folder**
     
    mv ./helmet_detection.py ./yolov10
    mv ./UI_detect.py ./yolov10

**6. Install the required dependencies in yolov10**
    
    cd yolov10
    pip install -q -r requirements.txt

**Start the Application**  
Once everything is ready, you can launch the application by running:

      streamlit run UI_detection.py