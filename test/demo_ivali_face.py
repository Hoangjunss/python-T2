import cv2
import face_recognition

imgTeam = face_recognition.load_image_file("dataset/image.png")
imgTeam = cv2.cvtColor(imgTeam, cv2.COLOR_BGR2RGB)

faceLoc = face_recognition.face_locations(imgTeam)
print(f"Đã tìm thấy {len(faceLoc)} khuôn mặt trong ảnh.")

nums = ["1", "2", "3", "4"]

for num,  face in zip(nums, faceLoc):
    print(face)
    top, right, bottom, left = face
    cv2.rectangle(imgTeam, (left, top), (right, bottom), (255, 0, 0), 2)
    cv2.putText(imgTeam, num, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX,
                0.9, (255, 255, 255), 2)

""" imgTeamEncodings = face_recognition.face_encodings(imgTeam)[0]

cv2.rectangle(imgTeam, (faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]), (255, 0, 0), 2)

# Resize và gán kết quả trả về cho biến imgTeam """
imgTeam = cv2.resize(imgTeam, (720, 660))

cv2.imshow("Team", imgTeam)
cv2.waitKey()
cv2.destroyAllWindows()
