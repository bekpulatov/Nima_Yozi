from openai import OpenAI
import base64

class OpenAIProcessor:
    def __init__(self, api_key):
        self.client = OpenAI(api_key=api_key)
        # self.system_prompt = system_prompt

    def process_image(self, image_data):
        try:
            response = self.client.chat.completions.create(
                model="gpt-4-turbo-2024-04-09",  # Use the model you have access to
                messages=[
                    {"role": "system", "content": "Я буду тебе отправлять тебе диалог, переписки с девушками. Ты всегда парень и должен отвечать на сообщение девушки. В переписках слева будут текста от девушки, а справа твои. Ты - мастер флирта и обольщения. Твоя задача - давать короткие, уверенные и игривые ответы на русском языке, которые демонстрируют высокий уровень 'риззa'. Используй остроумие, легкие комплименты и намеки. Будь смелым, но не грубым. Ответы должны быть краткими, не более 1-2 предложений. Цель - вызвать интерес и желание продолжить общение. Например: Возраст — это просто число. Давай лучше узнаем друг друга поближе." },
                    {
                        "role": "user",
                        "content": [
                            # {"type": "text", "text": },
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": f"data:image/jpeg;base64,{base64.b64encode(image_data).decode()}"
                                }
                            }
                        ]
                    }
                ],
                max_tokens=300
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error processing image: {str(e)}"