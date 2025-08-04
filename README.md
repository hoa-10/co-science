# 🤖 AI Code Assistant Project

This project is an intelligent assistant for generating and analyzing Python code using Google Generative AI (Gemini), `aider-chat`, and custom prompt-based logic.

---

## 🔧 Setup Instructions

### 1️⃣ Clone the Repository

git clone https://github.com/your-username/your-project.git
cd your-project

2️⃣ (Recommended) Create a Virtual Environment

For Linux/macOS:
bashpython -m venv venv
source venv/bin/activate
For Windows:
bashpython -m venv venv
venv\Scripts\activate

3️⃣ Install Dependencies

bashpip install -r requirements.txt

🔐 Configure API Key

Create a .env file in the root directory and add your Google Generative AI API key:
envGOOGLE_API_KEY=your_google_api_key_here
#Download dataset
you should download both of dataset in this given link:
raw data : https://drive.google.com/file/d/1JuoqJGkzN_KLQKQmL2mzwJuwZKlBNIaa/view?usp=sharing
normalized_data : https://drive.google.com/file/d/1TuZ7pOpJtiDSh-mezr3Y44FCFCTppDe2/view?usp=sharing
🚀 Running the Project

If you have a script like test.py, simply run:
bashpython test.py
