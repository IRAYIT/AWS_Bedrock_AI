# AWS_Bedrock_AI

A simple Python program that connects to **AWS Bedrock** and uses the **OpenAI GPT-OSS-120B** model to generate creative text, in this example, a short poem about teamwork.

This project is a clean, minimal example of how to:
- Set up and configure AWS Bedrock access.
- Use the **Bedrock Runtime API** via Python (`boto3`).
- Send a text prompt to the model and read the AI-generated response.
- Clean and display only the model output.

Features:
Connects securely to **AWS Bedrock** using `boto3`.
- Uses **OpenAI GPT-OSS-120B** model (`openai.gpt-oss-120b-1:0`).
- Accepts any user prompt.
- Runs directly in VS Code or any Python environment.
