
* Чтобы сохранить информацию о лицах, необходимо сначала создать ( CreateCollection ) коллекцию лиц в одном из регионов AWS в своей учетной записи. Вы указываете эту коллекцию лиц при вызове операции IndexFaces
Creating collection:EmployeFaceCollection
Collection ARN: aws:rekognition:eu-central-1:119212719574:collection/EmployeFaceCollection

* IndexFaces . Вы можете использовать эту операцию для обнаружения лиц на изображении и сохранения информации о чертах лица, обнаруженных в коллекции.
Face ID: 96a8511d-fa47-427c-8516-318e48d4e9f6

* После создания коллекции лиц и сохранения информации об элементах лица для всех лиц вы можете выполнить поиск в подборке совпадений лиц. Для поиска лиц в изображении вызовите SearchFacesByImage
Matching faces
FaceId:96a8511d-fa47-427c-8516-318e48d4e9f6
Similarity: 100.00%

Вы можете использовать коллекции в различных сценариях. Например, вы можете создать коллекцию лиц для хранения отсканированных изображений значков с помощью операции IndexFaces . Когда сотрудник входит в здание, изображение лица сотрудника захватывается и отправляется в операцию SearchFacesByImage . Если совпадение по лицу дает достаточно высокую оценку сходства (скажем, 99%), вы можете аутентифицировать сотрудника.

https://docs.aws.amazon.com/en_us/rekognition/latest/dg/collections.html#collections-search-faces

examples
https://docs.aws.amazon.com/en_us/code-samples/latest/catalog/code-catalog-python-example_code-rekognition.html


# Распознавание лиц с помощью библиотеки face_recognition
- on github https://github.com/ageitgey/face_recognition
- on pipi https://pypi.org/project/face_recognition/
- live demo https://beta.deepnote.com/project/fb97be4f-c859-465e-81a2-8aced974d32a#%2Fexample.ipynb
- API Docs: https://face-recognition.readthedocs.io.

Jioncfe
https://www.youtube.com/watch?v=iluST-V757A&list=PLEsfXFp6DpzRyxnU-vfs3vk-61Wpt7bOS