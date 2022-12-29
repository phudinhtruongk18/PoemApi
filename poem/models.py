from pydantic import BaseModel

class Poem(BaseModel):
    author: str
    title: str
    content: str
