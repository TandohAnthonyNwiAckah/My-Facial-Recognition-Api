import sys
import warnings
import face_recognition.api as face_recognition
import scipy


# Old Image Fxn
def old_image_src(src_old):

    src_old_encodings = []

    old_image = face_recognition.load_image_file(src_old)

    encode_old_image = face_recognition.face_encodings(old_image)

    if len(encode_old_image) == 1:
      
        src_old_encodings.append(encode_old_image[0])

    return src_old_encodings

# New Image Fxn
def new_image_src(src_new,  src_old_encodings):

    new_image = face_recognition.load_image_file(src_new)

    # Scale down image
    if new_image.shape[1] > 1600:
        scale_factor = 1600.0 / new_image.shape[1]
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            new_image = scipy.misc.imresize(new_image, scale_factor)

    encode_new_image = face_recognition.face_encodings(new_image)

    if len(encode_new_image)==1:
        for one_encode_new_image in encode_new_image:

            result = face_recognition.compare_faces(src_old_encodings, one_encode_new_image)

            print("Successful Image Matching")  if True in result else print("Unsuccessful Image Matching  !! ")

        return result[0]
    else:
        return "0","No face Detected"

def onCreate(src_old, src_new):

    src_old_encodings = old_image_src(src_old)

    result= new_image_src(src_new,  src_old_encodings)

    return result

if __name__ == "__main__":
   onCreate(sys.argv[1],sys.argv[2])