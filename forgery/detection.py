import torch
import torchvision.transforms as transforms
from torchvision import models
from PIL import Image
import numpy as np
from sklearn.cluster import KMeans
import os

# Load Pretrained ResNet Model
model = models.resnet18(pretrained=True)
model.eval()

# Define Image Transformations
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
])

# Load All Images and Extract Features
image_folder = r"C:\Users\AARATHISREE\Desktop\Digital Forensics\forgery_detection\forgery\data\new_generated_aadharcard_images"  # Update this path
features = []

for img_file in os.listdir(image_folder):
    img_path = os.path.join(image_folder, img_file)
    image = Image.open(img_path).convert("RGB")
    image = transform(image).unsqueeze(0)

    with torch.no_grad():
        feature = model(image).numpy()
        features.append(feature)

features = np.array(features).reshape(len(features), -1)

# Train K-Means Model
kmeans = KMeans(n_clusters=2, random_state=42)
kmeans.fit(features)

# Save Features
np.save("aadhaar_features.npy", features)
print("Model trained and saved successfully!")
