# 🤖 AI Research Assistant for NDT Analysis

A Human-in-the-Loop Multi-AgentSystem for Accelerating Pulsed Eddy Current TestingCorrosion Detection
<p align="center">
  <img src="https://raw.githubusercontent.com/hoa-10/co-science/refs/heads/main/workflow2.jpg?raw=true" alt="workfow" width="600"/>
</p>

## 🚀 Overview

This project provides an automated solution for NDT data analysis through AI-powered code generation. It features:

- **Automated Data Analysis**: AI-driven analysis of NDT datasets
- **Code Generation**: Intelligent Python code generation for experiments
- **Interactive Interface**: User-friendly Gradio web interface
- **Experiment Management**: Automated experiment execution and result visualization
- **Plot Generation**: Automatic visualization of analysis results

## 🔧 Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/hoa-10/co-science.git
cd ai-research-assistant
```

### 2️⃣ Create a Virtual Environment

**Linux/macOS:**
```bash
python -m venv venv
source venv/bin/activate
```

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure API Key

Create a `.env` file in the project root directory and add your Google Generative AI (Gemini) API key:

```env
GEMINI_API_KEY=your_google_api_key_here
```

### 5️⃣ Download Datasets

Download the required datasets and place them in the project root directory:

- **Raw Data**: [pect_ndt_full_dataset.npz](https://drive.google.com/file/d/16Uzy_oml5K2alAY991NjbtW72s4WPvYl/view?usp=sharing)


⚠️ **Important**: Ensure both datasets are downloaded and placed in the project root before running the application.

### 6️⃣ Run the Application

Execute the main script to start the web interface:

```bash
python test.py
```

The application will launch a Gradio interface accessible via your web browser.

## 📁 Project Structure

```
├── base_code/              # Core AI processing modules
│   ├── coding_loop_enhance.py
│   └── processing_data.py
├── prompt/                 # AI prompt templates
│   ├── analyze_data.py
│   └── trainning_prompt.py
├── perform_experiment.py   # Experiment execution logic
├── test.py                # Main application entry point
├── ideas.json             # Experiment ideas configuration
└── requirements.txt       # Python dependencies
```

## 🎯 Usage

1. **Load Ideas**: Import experiment ideas from JSON configuration
2. **Data Analysis**: Run automated analysis on NDT datasets
3. **Code Generation**: Generate Python code for specific experiments
4. **Execute Experiments**: Run generated code and collect results
5. **Visualize Results**: Generate and review plots automatically

## 🎥 Demo

Watch the project demonstration: [YouTube Video](https://youtu.be/QaPIhvVq33M)

## Result
<p align="center">
  <img src="https://github.com/hoa-10/co-science/blob/main/performance.png?raw=true" alt="Performance" width="600"/>
</p>

## 🤝 Contributing

Contributions are welcome! Please feel free to submit issues and enhancement requests.


