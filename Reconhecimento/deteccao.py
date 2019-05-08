import cv2
import dlib

def get_frame(cap, scaling_factor):
    # Capture the frame from video capture object
    ret, img = cap.read()

    # Resize the input frame
    img = cv2.resize(img, None, fx=scaling_factor,
            fy=scaling_factor, interpolation=cv2.INTER_AREA)

    return img

if __name__=='__main__':
    cap = cv2.VideoCapture(0)
    scaling_factor = 0.7


    # Iterate until the user presses ESC key

    f = open("..\Reconhecimento\Laudo_faca.doc", "a")

    while True:
        img = get_frame(cap, scaling_factor)
        cv2.imshow('Original image', img)

        detectorFacaSerrilhada = dlib.simple_object_detector("detector_faca_serrilhada.svm")
        detectorFaca = dlib.simple_object_detector("detector_faca.svm")
        detectorRebite = dlib.simple_object_detector("detector_faca_rebite.svm")
        detectorAfiada = dlib.simple_object_detector("detector_faca_afiada_ed3.svm")
        existe_Faca = 0
        num_Rebite = 0
        num_Foto = 0
        objetosDetectados_faca_serrilhada = detectorFacaSerrilhada(img)
        objetosDetectados_faca = detectorFaca(img)
        objetosDetectados_rebite = detectorRebite(img)
        objetosDetectados_faca_afiada = detectorAfiada(img)
        for d in objetosDetectados_faca:
            num_Foto = num_Foto + 1
            e, t, d, b = (int(d.left()), int(d.top()), int(d.right()), int(d.bottom()))
            cv2.rectangle(img, (e, t), (d, b), (0, 255, 0), 2)  # verde
            cv2.putText(img, "FACA", (e, b), cv2.FONT_HERSHEY_DUPLEX, 1.0, (0, 255, 0))
            from datetime import datetime

            now = datetime.now()
            f = open("Laudo_faca.doc", "a")
            f.write(
                "\n" + str(now.day) + "/" + str(now.month) + "/" + str(now.year) + " - " + str(now.hour) + ":" + str(
                    now.minute) + ":" + str(now.second) + " - Item " + str(num_Foto) + ": Faca ")
            existe_Faca = 1
        for d in objetosDetectados_faca_serrilhada:
            e, t, d, b = (int(d.left()), int(d.top()), int(d.right()), int(d.bottom()))
            cv2.rectangle(img, (e, t), (d, b), (0, 0, 255), 2)  # azul
            cv2.putText(img, "SERRILHADA", (e, b), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1.0, (0, 0, 255))
            if (existe_Faca == 1):
                f = open("Laudo_faca.doc", "a")
                f.write("serrilhada ")
        for d in objetosDetectados_faca_afiada:
            e, t, d, b = (int(d.left()), int(d.top()), int(d.right()), int(d.bottom()))
            cv2.rectangle(img, (e, t), (d, b), (255, 0, 0), 2)  # vermelho
            cv2.putText(img, "AFIADA", (e, b), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1.0, (255, 255, 0))
            if (existe_Faca == 1):
                f = open("Laudo_faca.doc", "a")
                f.write("afiada ")
        for d in objetosDetectados_rebite:
            e, t, d, b = (int(d.left()), int(d.top()), int(d.right()), int(d.bottom()))
            cv2.rectangle(img, (e, t), (d, b), (255, 255, 255), 2)  # branca
            cv2.putText(img, "REB", (d, t), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1.0, (255, 255, 255))
            num_Rebite = num_Rebite + 1
        if (existe_Faca == 1 and num_Rebite == 1):
            f = open("Laudo_faca.doc", "a")
            f.write(str(num_Rebite) + " rebites")
        elif (existe_Faca == 1 and num_Rebite > 1):
            f = open("Laudo_faca.doc", "a")
            f.write(str(num_Rebite) + " rebites")
        elif (existe_Faca == 0):
            f = open("Laudo_faca.doc", "a")
            f.write("Item " + ": Não ha facas. ")

        c = cv2.waitKey(5)
        if c == 27:
            break

    cv2.destroyAllWindows()