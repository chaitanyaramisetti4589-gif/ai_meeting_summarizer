# 🤖 AI Meeting Notes Summarizer

An AI-powered Meeting Notes Summarizer that automatically converts meeting transcripts into professional, structured meeting notes using **Google Gemini AI**. The application also stores every transcript and generated summary in **MongoDB**, allowing meetings to be accessed later.

---

## ✨ Features

- 📄 Reads meeting transcripts from a text file
- 🤖 Generates AI-powered meeting summaries using Google Gemini
- 📝 Creates structured meeting notes including:
  - Executive Summary
  - Key Discussion Points
  - Decisions Made
  - Action Items
  - Risks
  - Next Steps
- 💾 Saves generated notes to a text file
- 🗄 Stores transcripts and summaries in MongoDB
- 🏷 Automatically extracts the meeting title from the transcript
- 🔒 Uses environment variables for secure API key and database management

---

## 🛠 Tech Stack

- Python
- Google Gemini API
- PyMongo
- MongoDB Atlas
- python-dotenv

---

## 📂 Project Structure

```
ai-meeting-notes-summarizer/
│
├── transcript.txt
├── meeting_notes.txt
├── main.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

## ⚙️ How It Works

```
Meeting Transcript
        │
        ▼
Read Transcript File
        │
        ▼
Google Gemini AI
        │
        ▼
Generate Meeting Notes
        │
        ▼
Save Notes to Text File
        │
        ▼
Extract Meeting Title
        │
        ▼
Store Transcript + Summary in MongoDB
```

---

## 📦 Installation

### Clone the repository

```bash
git clone https://github.com/yourusername/ai-meeting-notes-summarizer.git
```

### Navigate to the project

```bash
cd ai-meeting-notes-summarizer
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file.

```env
GEMINI_API_KEY=your_gemini_api_key
MONGO_URI=your_mongodb_connection_string
```

---

## ▶️ Run the Project

```bash
python main.py
```

---

## 📁 Example Output

```
Executive Summary

Key Discussion Points

Decisions Made

Action Items

Risks

Next Steps
```

---

## 🗃 MongoDB Document

```json
{
  "title": "Sprint Planning Meeting",
  "transcript": "...",
  "summary": "...",
  "createdAt": "2026-07-24"
}
```

---

## 🚀 Future Improvements

- Upload transcript files through a web interface
- Search previous meetings
- Delete or update meeting records
- Export summaries as PDF
- Email meeting notes automatically
- Multi-language meeting summarization

---

## 👨‍💻 Author

**Chaitanya Ramisetti**

Aspiring AI Engineer passionate about building AI-powered automation tools and real-world applications.

---

## ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub.
