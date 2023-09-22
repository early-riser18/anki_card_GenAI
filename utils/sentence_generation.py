import os
import openai
import pdb
import requests
# Need validation of input as to fit the correct language (or value not empty ). Input should also have a limited amount of words
# The word field should not contain HTML


class SentenceGenerator:
    def __init__(self):
        self.api_key = os.getenv("OPEN_AI_TOKEN")

    def generate_sentence(self, card, lang):
        """
        Call third party tool to generate a sentence
        """
        trial_count = 0
        response = {"card_id": card.id}
        # Mock code while sentence generator is developped.
        # Catch exceptions from 3rd party service.
        while trial_count < 3:
            generated_sentence = self.call_api(card.tl_word, lang)
            print(f"Generated sentence: {generated_sentence}")

            if self.validate_generated_sentence(card.tl_word, generated_sentence):
                response["generated_sentence"] = generated_sentence
                return response
            else: 
                print("- Failed to generate valid sentence.")
                trial_count += 1

        raise Exception("Unable to generate sentence")

    def call_api(self, word, lang):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}",
        }
        endpoint = "https://api.openai.com/v1/chat/completions"
        system_prompt = "Generate only one example sentence of the user's word, in the provided language only. Word provided must be included. Do not provide a translation. Keep it under 12 words. Sentence helps user understand meaning of word. If unable, reply: '1' "
        data = {
            "model": "gpt-3.5-turbo",
            "messages": [
                {
                    "role": "system",
                    "content": system_prompt,
                },
                {
                    "role": "user",
                    "content": str({"word": f"{word}", "language": f"{lang}"}),
                },
            ],
            "temperature": 1.3,
        }

        res = requests.post(url=endpoint, headers=headers, json=data)
        return res.json()["choices"][0]["message"]["content"]

    def get_model_list(self):
        return requests.get(
            url="https://api.openai.com/v1/models",
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.api_key}",
            },
        ).json()

    def validate_generated_sentence(self, initial_word: str, gen_sentence: str) -> bool:
        """
        Provided a word, checks that the generated sentence contains that word.
        Assumptions:
        - One sentence either contains spaces between words (eg. western writing systems) or none.
        - If multiple words provided, they are found in the generated sentence in the same order and together.
        - Does not expect word which are conjugated (s for plurals or any transformation of verbs)
        """
        transformed = gen_sentence.lower()
        print(f"⭐️ Comparing: '{transformed}' and '{initial_word}' \n")
        validity = initial_word in transformed
        print("Gen Sentence is valid?: ", validity)
        return validity


if __name__ == "__main__":
    from utils.card_management import Card

    a = SentenceGenerator()
    # print(a.api_key)
    # print(a.call_api())
    # print(a.get_model_list())
    test_card = Card(1, "apple", "")
    print(a.generate_sentence(test_card, "en-US"))
