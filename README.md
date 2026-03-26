# 🎓 Exam_Viva Pro: AI-Powered Mock Interview & Examiner

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B.svg)
![Gemini API](https://img.shields.io/badge/Google-Gemini_1.5_Flash-orange.svg)
![Hackathon](https://img.shields.io/badge/Award-Most_Use_of_GenAI-gold.svg)

**Exam_Viva Pro** is an AI-driven study companion designed to simulate real-time university vivas and technical mock interviews. By uploading your study notes, the app generates conceptual questions and conducts a turn-based voice interview, grading your answers instantly just like a real professor.

🏆 *Built during the GenAI Hackathon Delhi - Awarded "Most Use of Google GenAI".*

> **Note:** This repository contains the initial hackathon version. For a demonstration of the final, fully-featured version, or to discuss technical opportunities in AI/ML,Mobile App development & Software Development please reach out:
> 
> 📧 **Email:** Praveenchaudhary3@gmail.com
> 📞 **Phone:** +91-8368107816

## ✨ Features

* 📄 **Multi-Format Document Processing:** Upload large documents (`.pdf`, `.docx`, `.txt`) or paste text directly. 
* 🎙️ **Live Voice Viva Mode:** * The AI generates a conceptual question and reads it aloud.
  * Record your answer directly in the browser.
  * The AI transcribes your speech, evaluates your answer, and provides immediate audio and text feedback.
  * *Hybrid Fallback:* If your mic fails, seamlessly switch to text input.
* 📝 **Customizable Written Quizzes:** Generate up to 50 practice questions with adjustable difficulty (Easy to Ph.D. Level). Answers are hidden inside clickable HTML toggles.
* 📥 **Export to Word:** Download your generated Q&A as a clean `.docx` file for offline studying.
* 🌑 **Hacker Dark Mode:** Sleek, distraction-free UI designed for focused study sessions.

## 🛠️ Tech Stack

* **Frontend/UI:** [Streamlit](https://streamlit.io/)
* **LLM Engine:** Google Gemini 1.5 Flash (via the modern `google-genai` SDK)
* **Document Parsing:** `PyPDF2` (PDFs), `python-docx` (Word Documents)
* **Voice Integration:** `SpeechRecognition` (Speech-to-Text), `gTTS` (Text-to-Speech), `streamlit-mic-recorder` (Browser audio capture)

## 🚀 Local Setup & Installation

**1. Clone the repository**
```bash
git clone [https://github.com/PraveenChaudhary/Exam_Viva.git](https://github.com/PraveenChaudhary/Exam_Viva.git)
cd Exam_Viva