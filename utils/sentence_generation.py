
# Sentence Gen AI Service Auth

# Sentence Generator

# Need validation of input as to fit the correct language (or value not empty ). Input should also have a limited amount of words
# The word field should not contain HTML


class SentenceGenerator:
    def generate_sentence(self, card):
        """
        Call third party tool to generate a sentence
        """
        # Mock code while sentence generator is developped.
        # Catch exceptions from 3rd party service.
        generated_sentence = (
            f"This is a mock sentence for {card.tl_word} in {self.lang}"
        )
        response = {"card": card, "generated_sentence": generated_sentence}
        return response
