import numpy as np
import cv2

image_path = 'zdjecia/mass.jpg'
prototxt_path = 'models/MobileNetSSD_deploy.prototxt'
model_path = 'models/MobileNetSSD_deploy.model'
min_confidence = 0.3

classes = ['person']


net = cv2.dnn.readNetFromCaffe(prototxt_path, model_path)

image = cv2.imread(image_path)
height, weight = image.shape[0], image.shape[1]
blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 0.007, (300, 300), 130)

net.setInput(blob)
detected_objects = net.forward()

num_people = 0

for i in range(detected_objects.shape[2]):
    confidence = detected_objects[0][0][i][2]
    if confidence > min_confidence:
        class_index = int(detected_objects[0, 0, i, 1])
        if class_index == 15:
             num_people += 1

        upper_left_x = int(detected_objects[0, 0, i, 3] * image.shape[1])
        upper_left_y = int(detected_objects[0, 0, i, 4] * image.shape[0])
        lower_right_x = int(detected_objects[0, 0, i, 5] * image.shape[1])
        lower_right_y = int(detected_objects[0, 0, i, 6] * image.shape[0])

        cv2.rectangle(image, (upper_left_x, upper_left_y), (lower_right_x, lower_right_y), (0, 255, 0), 3)

text = f'Number of people: {num_people}'
cv2.putText(image, text, (10, 30), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 2)

cv2.imshow("Detected people", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

