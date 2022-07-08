# My Facial Recognition Api
 Verifying the possibility that two faces are those of the same person. 
 Return Successful Image  if both images match and Unsuccessful Image otherwise. 

## REQUIREMENT 

```
pip install face_recognition
pip install scipy
pip install https://github.com/jloh02/dlib/releases/download/v19.22/dlib-19.22.99-cp310-cp310-win_amd64.whl
pip install flask

```

## TESTING

 
```
A:
python image_verify.py public/img/lng.jpg   public/img/doc.jpg
```
> Returns Unsuccessful Image Matching  !! 



```
B :
python image_verify.py public/img/lng.jpg   public/img/lng.jpg
```
> Returns Successful Image Matching  !! 

```
C:
 python api.py
 ```
 > Returns Running on http://127.0.0.1:8050

```
D:
pip freeze > requirements.txt

 > Create Requirement text file
```


```
E:
 pip3 install gunicorn  

 > keep python app live with Gunicorn

 ```


## ***PREVIEW***

| SUCCESS RESPONSE | FAILED RESPONSE |
|     ------------- | ------------- |
| ![Main Page](public/screenshot/true.PNG)| ![Main Page](public/screenshot/false.PNG)|




## TOOLS & PLATFORM
- Python Version: 3.10
- dlib Version: 19.22.99
- CMAKE
- GIT and GITHUB
- VS CODE
- POSTMAN
- Platform: Windows 10 64-bit


## TODO

- [x] Build Image Verify

- [x] Build Image Verify API

- [ ] Launch the project on a live server.
