# ✉️ **Spam Detection Terminal Application**
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)](https://www.python.org/)
[![Machine Learning](https://img.shields.io/badge/ML-Naive%20Bayes-ff69b4?logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

> 🛡️ **Real-time message classification that keeps your inbox clean!**

---

## 🎬 **Demo**

```bash
$ python app.py

Type your message to scan:
> Congratulations! You've won a free ticket. Reply now!

⛔ Result: Spam (Confidence: 98.4%)
```

---

## 🏆 **Features**

✨ **Quick Prediction via Terminal** — Enter any text and detect spam instantly  
✨ **Machine Learning Driven** — Naive Bayes model, TF-IDF feature extraction  
✨ **Confidence Scores** — Know how certain the model is  
✨ **Easy Retraining** — Swap out the dataset and rebuild the model  
✨ **Lightweight & Fast** — Run easily on nearly any computer

---

## ⚙️ **Project Structure**

```
.
├── app.py              # Terminal (CLI) application
├── train_model.py      # ML training pipeline
├── spam_model.pkl      # Saved model (binary)
├── download_data.py    # Dataset fetcher
├── requirements.txt    # Dependencies
└── README.md           # This file!
```

---

## 📦 **Installation & Setup**

1. **Clone this repository**
   ```bash
   git clone https://github.com/Bhavik0702/email-spam-detection-vs.git
   cd email-spam-detection-vs
   ```

2. **Create and activate a virtual environment (recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate    # Mac/Linux
   venv\Scripts\activate       # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

---

## 🗂️ **Dataset**

- Uses the classic SMS Spam Collection ([link 🔗](https://archive.ics.uci.edu/ml/datasets/sms+spam+collection)).  
- Run `download_data.py` to fetch `spam.csv` for training.

---

## 🏋️ **Model Training**

Retrain the classifier anytime:

```bash
python download_data.py       # Download spam.csv
python train_model.py         # Train & save spam_model.pkl
```

---

## 🚦 **Usage**

1. Launch the application:
   ```bash
   python app.py
   ```
2. Enter any message to check if it's Spam or Ham, and see the confidence score.

---

## 🤝 **Contributing**

Want to improve this project?  
- Fork, branch, commit, and open a pull request.
- Found a bug? [Open an issue](https://github.com/Bhavik0702/email-spam-detection-vs/issues)

---

## 📝 **License**

Licensed under the MIT License. See [`LICENSE`](LICENSE).

---

## 👤 **Author**

**Bhavik0702**  
[GitHub](https://github.com/Bhavik0702)

---

## 🎉 **Acknowledgments**

- Dataset: [UCI SMS Spam Collection](https://archive.ics.uci.edu/ml/datasets/sms+spam+collection)
- Libraries: Python, scikit-learn, pandas

---

> _Type, scan, and stay spam-free. Enjoy!_
