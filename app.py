from deepface import DeepFace

# Compare two images
result = DeepFace.verify('student1.jpg', 'student2.jpg', enforce_detection=False)

if result['verified']:
    print("Faces match!")
else:
    print("Faces do not match.")
