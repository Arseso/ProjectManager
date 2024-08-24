from src.web.models import Text
import re



def text_to_model(text: str) -> Text | None:
    preprocessed_text = [x for x in text.split("\n") if x]
    return preprocessed_text
    
    