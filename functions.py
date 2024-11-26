#importing all necessary APIs



# def userInput():
    #prompts user to input word that they want to convert to flashcard

    #(this may be more of a form intake thing on the html side)
    #takes input and preps it to be sent to Google Translate API translate method
    #stores input word as a global variable
def get_input(text):
	if text:
		return text
	return None

# translating the text that the user inputs
def translate_text(target: str, text: str) -> dict:
    """Translates text into the target language.

    Target must be an ISO 639-1 language code.
    See https://g.co/cloud/translate/v2/translate-reference#supported_languages
    """
    from google.cloud import translate_v2 as translate

    translate_client = translate.Client()

    if isinstance(text, bytes):
        text = text.decode("utf-8")

    # Text can also be a sequence of strings, in which case this method
    # will return a sequence of results for each text.
    result = translate_client.translate(text, target_language=target)

    print("Text: {}".format(result["input"]))
    print("Translation: {}".format(result["translatedText"]))
    print("Detected source language: {}".format(result["detectedSourceLanguage"]))

    return result

# def getExamples():
    #access openAI API to prompt a response that would give examples for the word at hand.





