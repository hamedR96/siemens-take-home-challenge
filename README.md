# Siemens Take-Home Challenge

This repository contains the codebase and setup instructions for the Siemens Take-Home Challenge, including data preprocessing, training with LoRA, and inference examples using AI models.

---

## 🚀 Project Overview

This project trains a model to perform zero-shot image generation and defect identification based on structured image descriptions. It relies on the [ai-toolkit](https://github.com/ostris/ai-toolkit) for training infrastructure and integrates pretrained models for image generation.

---

## 🔧 Setup Instructions

Follow the steps below to set up the project environment:

```bash
# Clone the main repository
git clone https://github.com/hamedR96/siemens-take-home-challenge.git
cd siemens-take-home-challenge

# Clone the AI toolkit
git clone https://github.com/ostris/ai-toolkit.git
cd ai-toolkit

# Create and activate the conda environment
conda create -n fluxdef python=3.10 -y
conda activate fluxdef

# Install dependencies
pip3 install --no-cache-dir torch==2.6.0 torchvision==0.21.0 --index-url https://download.pytorch.org/whl/cu126
pip3 install -r requirements.txt
```

## 🧹Data Preparation

Return to the main directory and run the data preparation script:
```bash
cd ../siemens-take-home-challenge
python data_prep.py
```

## 🏋️ Training

### 1) Sign into Hugging Face:
Make sure you are logged in to your Hugging Face account:

```bash
huggingface-cli login
```

### 2) Run Training:
Training parameters are pre-optimized in the YAML file, but feel free to modify them before execution:

```bash
python ai-toolkit/run.py train_lora_flux_schnell_24gb-defect.yaml
```

## 🔍 Inference

For inference, check out the example notebook:
```bash
zero_shot_image_generation.ipynb
```

## 📊 Data Preprocessing

Further details on the preprocessing pipeline can be found in:


```bash
data_preprocessing.ipynb
```

## ⚠️ Notes

Not all images in the dataset include both object and defect descriptions.
Only entries with both descriptions are used during training.
For others, it's recommended to generate descriptions using:
a LLM, or ideally a VLM that can infer both the object and type of defect to produce suitable textual descriptions.

## 📁 Repository Structure
```bash
.
├── ai-toolkit/               # Training framework
├── data_preprocessing.ipynb  # Data preprocessing notebook
├── data_prep.py              # Script for preparing training data
├── train_lora_flux_schnell_24gb-defect.yaml  # Training config
├── zero_shot_image_generation.ipynb  # Inference demo
└── README.md
```

## 📬 Contact
For questions or suggestions, please open an issue or reach out via GitHub.


Let me know if you’d like this version customized with badges, licensing info, or linked references to datasets or models!
