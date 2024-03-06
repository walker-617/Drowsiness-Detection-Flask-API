import dlib
import cv2

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

def find_area(face):
    a = face.left()
    b = face.top()
    c=face.right()
    d=face.bottom()
    return a*b*c*d

def get_landmarks(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = detector(gray)

    if len(faces)==0:
        return None
    else:
        max_area_face=faces[0]
        max_area=0
        for face in faces:
            if find_area(face)>max_area:
                max_area=find_area(face)
                max_area_face=face

        landmarks = predictor(gray, max_area_face)
        coordinates = [[point.x, point.y] for point in landmarks.parts()]
        return coordinates