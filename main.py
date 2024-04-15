import os
import cv2

def count_people(image_path):
    # Wczytanie obrazu
    image = cv2.imread(image_path)

    # Konwersja obrazu na skale szarości
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Inicjalizacja klasyfikatorów do detekcji twarzy, ludzi i górnych części ciała
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    human_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_fullbody.xml')
    upperbody_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_upperbody.xml')

    # Wykrywanie twarzy na obrazie
    faces = face_cascade.detectMultiScale(gray, 1.101, 4)

    # Wykrywanie ludzi na obrazie
    humans = human_cascade.detectMultiScale(gray, 1.101, 4)

    # Wykrywanie górnych części ciała na obrazie
    upperbodies = upperbody_cascade.detectMultiScale(gray, 1.101, 4)

    # Zapisanie liczby wykrytych osób przez każdy klasyfikator w słowniku
    num_people = {
        'face': len(faces),
        'human': len(humans),
        'upperbody': len(upperbodies)
    }

    # Zwrócenie liczby wykrytych osób przez każdy klasyfikator
    return num_people

# Ścieżka do testowego zdjęcia
test_image_path = os.path.join('zdjecia', 'test5.jpg')

# Testowanie funkcji
num_people = count_people(test_image_path)
print("Liczba osób na zdjęciu:", num_people)
