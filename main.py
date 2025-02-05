import os
import dotenv
from openai import OpenAI

dotenv.load_dotenv()

def getGptResponse(content: str):

    client = OpenAI(
    api_key=os.getenv("OPENAI_KEY")
    )

    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    store=True,
    messages=[
        {"role": "developer", "content": "voce ira receber um conteudo de resumo de uma matéria, seu papel será formular oito perguntas e respostas baseadas nesse conteúdo"},
        {"role": "developer", "content": "voce irá gerar cada um dos pares pergunta resposta em um json com a chave question e chave answer, cada json estará dentro de um array principal com todas perguntas e respostas."},
        {
            "role": "user",
            "content": f"Conteúdo: {content}"
        }
    ]
    )

    print(completion.choices[0].message);


if __name__ == "__main__":
    getGptResponse("Segunda guerra mundial.")