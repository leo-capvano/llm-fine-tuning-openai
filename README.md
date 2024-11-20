# 🚀 Fine-Tuning and Chatbot with Python
Welcome to Eva, your customizable chatbot powered by fine-tuned models! This project demonstrates how to fine-tune a language model and deploy it seamlessly into a conversational assistant.

## 🌟 Features
Chat with Eva
A responsive chatbot that interacts dynamically with users. Start the conversation and let Eva assist you.

### Fine-Tune Your Model
Customize a base language model using your own dataset and create a fine-tuned version tailored to your needs.

### Real-Time Fine-Tuning Progress
Monitor the progress of your fine-tuning job and retrieve the final model ID once completed.

## 🛠️ Installation
Clone the repository:

> git clone https://github.com/your-repo/fine-tune-chatbot.git  
> cd fine-tune-chatbot

### Install dependencies: 
Ensure you have Python 3.9+ installed, then run:

> pip install -r requirements.txt  

### Prepare your training file: 

Place your training file (in JSONL format) in the **res/** folder.

## 🚦 Usage
1. Chatbot Mode
Launch Eva, your chatbot:

> python chatbot.py  

Eva will greet you and await your queries. Type your questions and experience the conversational capabilities!

2. Fine-Tuning Mode
Fine-tune a base model using your dataset:

> python fine_tune.py

### Steps in Fine-Tuning Mode:

1. Enter the name of your training file located in the res/ folder.
2. Confirm to start the fine-tuning process.
3. Monitor the progress, and retrieve your custom model ID upon completion.

## 📖 How It Works
### Chatbot Interaction:
The chatbot (chatbot.py) uses the ask_model service to process user inputs and return dynamic responses.

### Fine-Tuning Workflow:
The fine-tuning script (fine_tune.py) uses:

> upload_training_file() to upload your dataset.  
> create_training_job() to start a fine-tuning job.  
> training_job_status() to monitor the job and retrieve the fine-tuned model.  

## 🛡️ Requirements
- Python: 3.12+
- OpenAI API Access: Make sure you have access to OpenAI's fine-tuning services.
- Training Dataset: Format your training file in JSONL format.

## 🤝 Contributing
Contributions are welcome! Feel free to open issues or submit pull requests to improve this project.

## 🙌 Acknowledgments
Powered by OpenAI API for state-of-the-art language models.
Special thanks to the developers and contributors of this repository.
---
Enjoy using Eva, your customizable fine-tuned chatbot! ✨