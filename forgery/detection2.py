import torch
import torchvision.transforms as transforms
from torchvision import models
from PIL import Image
import numpy as np
from sklearn.cluster import KMeans

# Load Pretrained ResNet Model
model = models.resnet18(pretrained=True)
model.eval()

# Define Image Transformations
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
])

# Load Precomputed Features if Available
try:
    features = np.load("aadhaar_features.npy")
    kmeans = KMeans(n_clusters=2, random_state=42)
    kmeans.fit(features)
except:
    kmeans = None

# Function to Classify Document
def classify_document(image_path):
    image = Image.open(image_path).convert("RGB")
    image = transform(image).unsqueeze(0)

    with torch.no_grad():
        features = model(image).numpy()

    if kmeans:
        cluster = kmeans.predict(features)
        return "Real" if cluster[0] == 0 else "Forged"
    else:
        return "Unable to classify. Train the model first."
