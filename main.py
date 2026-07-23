import os
from pymongo import MongoClient
from dotenv import load_dotenv
load_dotenv()
from google import genai
api_key=os.getenv("GEMINI_API_KEY")
Mongo_url=os.getenv("MONGO_URL")
mongoclient=MongoClient(Mongo_url)
db=mongoclient["meeting_notes_db"]
collection=db["meetings"]
client=genai.Client(api_key=api_key)
filename=input("Enter the Transcript file name: ")
f=open(filename)
content=f.read()
title = "Untitled Meeting"  # Default title

for line in content.splitlines():
    if line.startswith("Meeting Title:"):
        title = line.replace("Meeting Title:", "").strip()
        break
response=client.models.generate_content(
    model="gemini-3.6-flash",
    contents=f"""Act as Meeting Transcript Summarizer which extract the give contents of the transcript in the provided format:Meeting Title

Date

--------------------------------

Executive Summary

--------------------------------

Key Discussion Points

--------------------------------

Decisions Made

--------------------------------

Action Items

--------------------------------

Risks

--------------------------------

Next Steps 

---------------------------------
Transcript:{content}
rules: dont include explanation just give the output in text format"""
)
print("The Summary of the transcript is")
print(response.text)
transcript=content
notes=response.text
meeting={
     "title":title,
     "transcript":transcript,
     "Notes":notes
}
collection.insert_one(meeting)
print("✅ Meeting Saved Successfully")
if os.path.exists("meeting_notes.txt") and os.path.getsize("meeting_notes.txt")>0:
    with open('meeting_notes.txt','w',encoding='utf-8') as file:
        pass
    with open('meeting_notes.txt','a',encoding='utf-8') as file:
            file.write(response.text)
else:
    with open('meeting_notes.txt','a',encoding='utf-8') as file:
        file.write(response.text)
print("Sucessfully created and written the summary in meeting_notes.txt file")
