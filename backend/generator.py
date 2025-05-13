import re


def generate_flashcards(text):
    flashcards = []


    text = re.sub(r'\s+', ' ', text).strip()


    sentences = re.split(r'[.!?]', text)


    for s in sentences:
        s = s.strip()


        if not s:
            continue


        if len(s.split()) >= 3 and 'is' in s:
            parts = s.split('is', 1)
            question = f"What is {parts[0].strip()}?"
            answer = parts[1].strip()
            flashcards.append({'question': question, 'answer': answer})


    return flashcards
