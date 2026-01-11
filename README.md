# Fish_Classification

**🐟 FishPro AI - Deep Learning Fish Classification**

FishPro AI is a state-of-the-art Computer Vision application designed to automatically identify and classify fish species from images. Built with a custom "Ocean-Themed" UI, this project utilizes Transfer Learning (MobileNetV2) to achieve high-precision results, aiding in seafood identification and marine biology education.

**📝 Project OverviewObjective:**

To develop a robust Deep Learning model capable of recognizing different fish species with high accuracy and to deploy it via a user-friendly web interface. The system analyzes uploaded images in real-time and provides the species name along with a confidence score.

**🚀 Key Features**

High Accuracy: The deployed model achieves an impressive 99.27% accuracy on validation data.
Ocean-Themed UI: A custom-styled Streamlit interface featuring deep-sea gradients, high-visibility text, and intuitive navigation.
Transfer Learning: Utilizes the MobileNetV2 architecture, pre-trained on ImageNet, fine-tuned for specific fish features.
Multi-Model Comparison: The final model was selected after evaluating 6 different architectures (InceptionV3, ResNet50, VGG16, etc.).
Confidence Meter: Visual progress bar indicating how certain the AI is about its prediction.

**💿 Dataset Details**

The model is trained on a large dataset of fish images, utilizing Image Augmentation (rotation, flipping, zooming) to improve robustness.
Classes (11 Species):The AI can currently identify the following species:

** Animal Fish
** Bass
** Black Sea Sprat
** Gilt Head Bream
** Horse Mackerel
** Red Mullet
** Red Sea Bream
** Sea Bass
** Shrimp
** Striped Red Mullet
** Trout

**🛠️ Tech Stack**

Language: Python 
Deep Learning Framework: TensorFlow / KerasWeb 
Framework: Streamlit (Custom HTML/CSS integration)
Image Processing: Pillow (PIL), NumPy, ImageDataGenerator
Visualization: Matplotlib (for training evaluation)

**📊 Model Performance**

We trained multiple models to find the best balance between speed and accuracy. 
MobileNetV2 was chosen as the winner for the final deployment.

Model Architecture	   Accuracy	         Status
MobileNetV2	           99.27%	           Winner (Deployed)
InceptionV3	          ~94.5%	           High Accuracy
EfficientNetV2	      ~92.0%	           Good Performance
ResNet50	            ~90.1%	           Heavy Computation
VGG16	                ~88.4%	           Slow Inference
Custom CNN	          ~75.0%	           Baseline Model


