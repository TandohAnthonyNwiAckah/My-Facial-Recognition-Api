# My Facial Recognition Api
 Verifying the possibility that two faces are those of the same person. 
 Return Successful Image  if both images match and Unsuccessful Image otherwise. 

## REQUIREMENT 

```
pip install opencv-python
pip install face_recognition
pip install scipy
pip install https://github.com/jloh02/dlib/releases/download/v19.22/dlib-19.22.99-cp310-cp310-win_amd64.whl
```


## TOOLS & PLATFORM
- Python Version: 3.10
- dlib Version: 19.22.99
- CMAKE
- GIT and GITHUB
- VS CODE
- POSTMAN
- Platform: Windows 10 64-bit


## TODO

[ ] Build Image Verify

[x] Build Image Verify API

[x] Launch the project on a live server.


## TESTING

```
python image_verify.py public/img/lng.jpg   public/img/doc.jpg
```
> Returns Unsuccessful Image Matching  !! 


```
python image_verify.py public/img/lng.jpg   public/img/lng.jpg
```
> Returns Successful Image Matching  !! 