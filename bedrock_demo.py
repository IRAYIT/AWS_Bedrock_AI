import boto3
import json

def main():
    # 1️⃣ Create Bedrock client
    client = boto3.client("bedrock-runtime", region_name="us-east-1")

    # 2️⃣ Define the prompt
    prompt = "Write a small poem about teamwork."

    # 3️⃣ Build request body — OpenAI-style schema
    body = {
        "model": "openai.gpt-oss-120b-1:0",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant that writes creative text."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7,
        "top_p": 0.9,
        "max_completion_tokens": 150
    }

    # 4️⃣ Invoke the model
    response = client.invoke_model(
        modelId="openai.gpt-oss-120b-1:0",
        body=json.dumps(body)
    )

    # 5️⃣ Parse and print the result
    response_body = json.loads(response["body"].read()) 

    poem = response_body["choices"][0]["message"]["content"]
    print("\nGPT-OSS-120B says:\n")
    print(poem)


if __name__ == "__main__":
    main()
