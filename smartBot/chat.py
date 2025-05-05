import json
import os
import torch
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
MEM_FILE = "learned_memory.json"

def load_memory():
    if not os.path.exists(MEM_FILE):
        return []
    with open(MEM_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    # Proveri da li su svi podaci u ispravnom formatu (listi rečnika)
    corrected_data = []
    for entry in data:
        if isinstance(entry, dict) and "question" in entry and "answer" in entry and "embedding" in entry:
            corrected_data.append(entry)
        else:
            print("Neispravan format u memoriji, zanemarujem zapis:", entry)
    
    return corrected_data

def save_memory(memory):
    with open(MEM_FILE, "w", encoding="utf-8") as f:
        json.dump(memory, f, indent=2, ensure_ascii=False)

def get_smart_response(user_input):
    memory = load_memory()
    if not memory:
        return ask_and_learn(user_input, memory)

    input_embedding = model.encode(user_input, convert_to_tensor=True)

    best_score = 0
    best_answer = None

    for entry in memory:
        emb_list = entry["embedding"]
        emb_tensor = torch.tensor(emb_list).unsqueeze(0)  # [1, 384]
        score = util.pytorch_cos_sim(input_embedding, emb_tensor).item()

        if score > best_score:
            best_score = score
            best_answer = entry["answer"]

    if best_score > 0.7:
        return best_answer
    else:
        return ask_and_learn(user_input, memory)

def ask_and_learn(user_input, memory):
    print("SmartBot: Ne znam odgovor. Kako da odgovorim?")
    answer = input("Ti (odgovor): ").strip()
    if answer:
        embedding_tensor = model.encode(user_input, convert_to_tensor=True)
        embedding_list = embedding_tensor.tolist()  # Pretvaranje u listu pre čuvanja
        memory.append({
            "question": user_input, 
            "answer": answer, 
            "embedding": embedding_list
        })
        save_memory(memory)
        return "Zapamtio sam to!"
    return "Nisam dobio odgovor."
