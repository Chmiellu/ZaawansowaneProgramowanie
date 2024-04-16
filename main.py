import numpy as np
import cv2

image_path = 'zdjecia/test6.jpg'
prototxt_path = 'models/MobileNetSSD_deploy.prototxt'
model_path = 'models/MobileNetSSD_deploy.model'
min_confidence = 0.3

classes = ['background',
           'aeroplane', 'bicycle', 'bird', 'boat',
           'bottle', 'bus', 'car', 'cat', 'chair',
           'cow', 'diningtable', 'dog', 'horse',
           'motorbike', 'person', 'pottedplant',
           'sheep', 'sofa', 'train', 'tvmonitor']

np.random.seed(543210)
colors = np.random.uniform(0, 255, size=(len(classes), 3))

net = cv2.dnn.readNetFromCaffe(prototxt_path, model_path)

image = cv2.imread(image_path)
height, weight = image.shape[0], image.shape[1]
blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 0.007, (300, 300), 130)

net.setInput(blob)
detected_objects = net.forward()

for i in range(detected_objects.shape[2]):
    confidence = detected_objects[0][0][i][2]
    if confidence > min_confidence:
        class_index = int(detected_objects[0, 0, i, 1])

        upper_left_x = int(detected_objects[0, 0, i, 3] * image.shape[1])
        upper_left_y = int(detected_objects[0, 0, i, 4] * image.shape[0])
        lower_right_x = int(detected_objects[0, 0, i, 5] * image.shape[1])
        lower_right_y = int(detected_objects[0, 0, i, 6] * image.shape[0])

        cv2.rectangle(image, (upper_left_x, upper_left_y), (lower_right_x, lower_right_y), colors[class_index], 3)


cv2.imshow("Detected Objects", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

