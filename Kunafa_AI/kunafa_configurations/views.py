from django.shortcuts import render
from kunafa_configurations.forms import IPCameraForm
from .models import IPCamera
from .constants import *
import cv2

# Create your views here.
def load_main_page(request):
    status=False
    ip_form=IPCameraForm
    all_data=IPCamera.objects.all()
    if request.POST:
        form = ip_form(request.POST)
        if form.is_valid():
            form.save()
            status=True
    context={
        'form':ip_form,
        'status':status,
        'all_data':all_data}
    return render(request,"index.html",context)

def kill(request):
    IPCamera.objects.all().delete()
    context={'delete':'deleted'}
    return render(request,"deleted.html",context)

def track_object_from_video(cascade_path, camera, frame_name,mode):
    """Track objects from video"""    
    cap = cv2.VideoCapture(camera)
    faceCascade = cv2.CascadeClassifier(cascade_path)
    framer = frame_name
    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        net = faceCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        if mode==True:
            if len(net) >= 2:
                return True
        for (x, y, w, h) in net:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.imshow(framer, frame)
        if cv2.waitKey(1) & 0xFF == ord("x"):
            break
    cap.release()
    cv2.destroyAllWindows()
    

def track_kunafa(request):
    camera_config=IPCamera.objects.all()
    for config in camera_config:
        ipcam=config.IPV4
        mode=config.MODEL
        print(ipcam+"---->",mode)
    if mode=="Face_Tracking":        
        track_object_from_video(FACE_PATH,int(ipcam),"KUNAFA VISION",False)   
    elif mode=="Full_Body_Detection":
        track_object_from_video(FULL_BODY_PATH,int(ipcam),"KUNAFA VISION",False)
    return render(request,"stopped_camera_service.html")
