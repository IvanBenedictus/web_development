import random
import json
import torch
import pickle
from pathlib import Path

from .utils import bag_of_words, tokenize
from .model import NeuralNet

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Construct an absolute path to the intent.json file
current_dir = Path(__file__).parent
json_path = current_dir/"intents.json"

# Open and read the intent.json file
with open(json_path, "r") as file:
    intents = json.load(file)

FILE = current_dir/"data.pkl"
with open(FILE, "rb") as f:
    data = pickle.load(f)

model = data["model"]
all_words = data["all_words"]
tags = data["tags"]

bot_name = "Bot"

def get_response(message):
    sentence = tokenize(message)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    if prob.item() > 0.75:
        for intent in intents["intents"]:
            if tag == intent["tag"]:
                return random.choice(intent["responses"])
    else:
        return "I do not understand..."
    
if __name__ == "__main__":
    print("Let's chat! (type 'quit' to exit)")
    while True:
        sentence = input("You: ")

        if sentence.lower() == "quit":
            break

        response = get_response(sentence)
        print(f"{bot_name}: {response}")