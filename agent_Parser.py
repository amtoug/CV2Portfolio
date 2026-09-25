from LLM_Benchmark.models import llm_Groq
from dotenv import load_dotenv

Model=llm_Groq("openai/gpt-oss-safeguard-20b")

def agent_parser(cv_text):
    prompt = f'''
You are a professional CV information extraction system.

Your task is to extract structured information from the CV provided below and return it as a single valid JSON object.

STRICT RULES:
1. Return ONLY valid JSON.
2. Do NOT return Markdown, explanations, comments, or code fences.
3. Do NOT invent, infer, assume, or hallucinate information.
4. Extract information ONLY from the CV.
5. Preserve the original meaning of the CV.
6. If information is missing, use an empty string "" or an empty array [].
7. Use EXACTLY the JSON schema provided below.
8. Do NOT add, remove, or rename any fields.
9. Keep the same structure for every CV.
10. Keep descriptions concise while preserving important technical information.
11. Do not duplicate the same information across multiple sections.
12. Preserve proper names of people, organizations, institutions, technologies, certifications, and projects.
13. Preserve dates and periods as they appear in the CV.
14. Do not convert or normalize dates unless necessary for extraction.
15. Skills must contain individual skills or technologies, not complete sentences.
16. Languages must contain the languages explicitly mentioned in the CV.
17. For experience, extract internships, jobs, freelance experiences, and other professional experiences explicitly mentioned.
18. For projects, extract explicitly identified academic, personal, professional, or portfolio projects.
19. Do not create a project from a simple mention of a technology.
20. If a section does not exist in the CV, return an empty array.

JSON SCHEMA:

{{
  "name": "",
  "title": "",
  "summary": "",
  "location":"",
  "email":"",
  "phone":"",
  "skills": [],
  "education": [
    {{
      "degree": "",
      "field": "",
      "institution": "",
      "period": ""
    }}
  ],
  "experience": [
    {{
      "role": "",
      "organization": "",
      "period": "",
      "description": ""
    }}
  ],
  "projects": [
    {{
      "name": "",
      "description": "",
      "technologies": []
    }}
  ],
  "languages": [
    {{
      "language": "",
      "level": ""
    }}
  ],
}}

CV:
{cv_text}
'''
    return  Model.invoke(prompt).content
