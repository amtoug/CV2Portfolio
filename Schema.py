from pydantic import BaseModel
from typing import List


class Education(BaseModel):
    degree: str
    field: str
    institution: str
    period: str


class Experience(BaseModel):
    role: str
    organization: str
    period: str
    description: str


class Project(BaseModel):
    name: str
    description: str
    technologies: List[str]

class languages(BaseModel):
    language: str
    level: str

class Portfolio(BaseModel):
    name: str
    title: str
    summary: str
    location:str
    email:str
    phone:str
    skills: List[str]
    education: List[Education]
    experience: List[Experience]
    projects: List[Project]
    languages: List[languages]
