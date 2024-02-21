import json
import pickle
import numpy as np
from pathlib import Path

import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader

from .utils import bag_of_words, tokenize, stem


class ChatDataset(Dataset):
    def __init__(self):
        self.n_samples = len(x_train)
        self.x_data = x_train
        self.y_data = y_train

    # We can call len(dataset) to return the size
    def __len__(self):
        return self.n_samples
    
    # Support indexing such that dataset[i] can be used to get i-th sample
    def __getitem__(self, index):
        return self.x_data[index], self.y_data[index]
    
class NeuralNet(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(NeuralNet, self).__init__()
        self.l1 = nn.Linear(input_size, hidden_size) 
        self.l2 = nn.Linear(hidden_size, hidden_size) 
        self.l3 = nn.Linear(hidden_size, output_size)
        self.relu = nn.ReLU()
    
    def forward(self, x):
        x = self.l1(x)
        x = self.relu(x)
        x = self.l2(x)
        x = self.relu(x)
        x = self.l3(x)
        return x


current_dir = Path(__file__).parent
json_path = current_dir/"intents.json"

with open(json_path, "r") as f:
    intents = json.load(f)

all_words = []
tags = []
xy = []

# Loop through each sentence in our intents patterns
for intent in intents["intents"]:
    # Create tag list
    tag = intent["tag"]
    tags.append(tag)

    for pattern in intent["patterns"]:
        # Tokenize each word in the sentence
        w = tokenize(pattern)
        # Add to our words list
        all_words.extend(w)

        # Add to xy pair
        xy.append((w, tag))

# Stem and lower each word
ignore_words = ["?", ".", "!", ","]
all_words = [stem(w) for w in all_words if w not in ignore_words]

# Remove duplicates and sort
all_words = sorted(set(all_words))
tags = sorted(set(tags))

# Create training data
x_train = []
y_train = []
for (pattern_sentence, tag) in xy:
    # x: Bag of words for each pattern_sentence
    bag = bag_of_words(pattern_sentence, all_words)
    x_train.append(bag)
    
    # y: PyTorch CrossEntropyLoss needs only class labels, not one-hot
    label = tags.index(tag)
    y_train.append(label)

x_train = np.array(x_train)
y_train = np.array(y_train)

# Hyper-parameters 
num_epochs = 1000
batch_size = 8
learning_rate = 0.001

input_size = len(x_train[0])
hidden_size = 8
output_size = len(tags)

dataset = ChatDataset()
train_loader = DataLoader(dataset=dataset, batch_size=batch_size, shuffle=True, num_workers=0)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = NeuralNet(input_size, hidden_size, output_size).to(device)

# Loss and optimizer
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

# Train the model
for epoch in range(num_epochs):
    for (words, labels) in train_loader:
        words = words.to(device)
        labels = labels.to(dtype=torch.long).to(device)
        
        # Forward pass
        outputs = model(words)
        loss = criterion(outputs, labels)
        
        # Backward and optimize
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        
    if (epoch+1) % 100 == 0:
        print (f"Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}")

print(f"final loss: {loss.item():.4f}")

current_dir = Path(__file__).parent
FILE = current_dir/"data.pkl"

data = {
    "model": model,
    "all_words": all_words,
    "tags": tags
}
with open(FILE, "wb") as f:
    pickle.dump(data, f)

print(f"training complete. file saved to {FILE}")