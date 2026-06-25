<div align="center">

![Header](https://capsule-render.vercel.app/api?type=waving&color=0:0f2027,50:203a43,100:2c5364&height=180&section=header&text=Age%20%26%20Gender%20Prediction&fontSize=38&fontColor=ffffff&fontAlignY=38&desc=Deep%20Learning%20%7C%20CNN%20%7C%20Face%20Analysis%20%7C%20Food%20Recommendation&descAlignY=58&descSize=15&descColor=a8d8ea)

[![License](https://img.shields.io/badge/License-MIT-2c5364?style=for-the-badge)](#-license)
[![Stars](https://img.shields.io/github/stars/MuhammadAdnan586/Age-and-Gender-Prediction?style=for-the-badge&color=2c5364&label=Stars)](https://github.com/MuhammadAdnan586/Age-and-Gender-Prediction/stargazers)
[![Last Commit](https://img.shields.io/github/last-commit/MuhammadAdnan586/Age-and-Gender-Prediction?style=for-the-badge&color=2c5364&label=Updated)](https://github.com/MuhammadAdnan586/Age-and-Gender-Prediction/commits/main)
[![Jupyter](https://img.shields.io/badge/Notebook-Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](#)

</div>

---

### 📌 About the Project

**Age & Gender Prediction** is a deep learning project that uses Convolutional Neural Networks (CNN) to predict a person's **age and gender from facial images**. Built on top of TensorFlow and Keras, the model is trained on real-world face datasets and achieves strong accuracy across diverse age groups and genders.

> As a bonus feature, the project also includes a **Food Recommendation System** that suggests food based on the predicted age group — combining computer vision with a practical recommendation engine.

---

### ✨ Key Features

**🔹 Age & Gender Prediction**
- CNN-based deep learning model for facial analysis
- Predicts age (regression) and gender (classification) simultaneously
- Preprocessing pipeline with face detection using OpenCV
- Model evaluation with accuracy metrics and confusion matrix

**🔹 Food Recommendation System**
- Rule-based recommendation engine tied to predicted age group
- Suggests nutritionally appropriate foods (child, adult, senior)
- Easily extensible to collaborative filtering

**🔹 Technical Highlights**
- Transfer learning support for faster training
- Data augmentation to improve generalization
- Visualizations — training curves, sample predictions, heatmaps
- Clean Jupyter Notebook workflow for reproducibility

---

### 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=flat-square&logo=tensorflow&logoColor=white)
![Keras](https://img.shields.io/badge/Keras-D00000?style=flat-square&logo=keras&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=flat-square&logo=opencv&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=flat-square&logo=matplotlib&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=flat-square&logo=jupyter&logoColor=white)

| Layer | Technology |
|---|---|
| Deep Learning Framework | TensorFlow + Keras |
| Face Detection | OpenCV (Haar Cascade / DNN) |
| Data Processing | NumPy, Pandas |
| Visualization | Matplotlib, Seaborn |
| Notebook Environment | Jupyter Notebook |
| Language | Python 3.x |

---

### ⚙️ Quick Start

```bash
# 1. Clone the repo
git clone https://github.com/MuhammadAdnan586/Age-and-Gender-Prediction.git
cd Age-and-Gender-Prediction

# 2. Install dependencies
pip install tensorflow keras opencv-python numpy pandas matplotlib seaborn jupyter

# 3. Open the notebook
cd "Deep Learning"
jupyter notebook
```

---

### 📂 Project Structure
```
Age-and-Gender-Prediction/
├── Deep Learning/
│   ├── age_gender_prediction.ipynb   ← Main model training notebook
│   ├── food_recommendation.ipynb     ← Food recommendation system
│   ├── models/                       ← Saved trained models
│   └── data/                         ← Dataset (download separately)
└── .gitignore
```

---

### 📊 Model Performance

| Task | Metric | Score |
|---|---|---|
| Gender Classification | Accuracy | ~90%+ |
| Age Estimation | MAE | ~5 years |
| Face Detection | OpenCV DNN | Real-time |

---

### 🗂️ Dataset

This project uses publicly available face datasets. Recommended:

- **UTKFace** — [kaggle.com/datasets/jangedoo/utkface-new](https://www.kaggle.com/datasets/jangedoo/utkface-new)
- **IMDB-WIKI** — large-scale face dataset with age & gender labels

> Download the dataset and place it in the `Deep Learning/data/` folder before running the notebooks.

---

### 🤝 Contributing

Contributions, issues, and feature requests are welcome!
Feel free to check the [issues page](https://github.com/MuhammadAdnan586/Age-and-Gender-Prediction/issues) or open a pull request.

---

### 📄 License

This project is licensed under the **MIT License**.

---

<div align="center">

![Footer](https://capsule-render.vercel.app/api?type=waving&color=0:2c5364,50:203a43,100:0f2027&height=100&section=footer)

Made with ❤️ by [**Muhammad Adnan**](https://github.com/MuhammadAdnan586) — Data Scientist | ML Engineer  
[LinkedIn](https://www.linkedin.com/in/m-adnan-12a816402) • [Portfolio](https://portfolio-eight-delta-7blam1yft8.vercel.app)

</div>
