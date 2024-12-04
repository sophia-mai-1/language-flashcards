#importing all necessary APIs
import requests
import pinyin
import pinyin.cedict

# def userInput():
    #prompts user to input word that they want to convert to flashcard

    #(this may be more of a form intake thing on the html side)
    #takes input and preps it to be sent to Google Translate API translate method
    #stores input word as a global variable
    

# translating the text that the user inputs
def get_pinyin(chinese_text):
    try:
        pinyin_result = pinyin.get(chinese_text)
        return pinyin_result
    except Exception as e:
        return f"Error: {e}"
    

def get_translation(chinese_text):
    try:
        translation_result = pinyin.cedict.translate_word(chinese_text)
        return translation_result
    except Exception as e:
        return f"Error: {e}"

def main():
    print("Welcome to the Pinyin Conversion Tool!")
    chinese_text = input("\nEnter Chinese text (or type 'exit' to quit): ")
    if chinese_text.lower() == "exit":
        print("Goodbye!")
        
    pinyin_output = get_pinyin(chinese_text)
    print(f"Pinyin: {pinyin_output}")

    translation_output = get_translation(chinese_text)
    print(f"Translation: {translation_output}")



if __name__ == "__main__":
    main()



def create_flashcard(englishw, chinesew, sentence, api_key):
    url = "https://api.mochicard.com/create_flashcard"
    data = {
        'front': englishw,
        'back': f"{chinesew} - {sentence}",
        'tags': ['English-Chinese']
    }
    headers = {
        'Authorization': f"Bearer {api_key}"
    }
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 201:
        return response.json()
    else:
        raise Exception(f"Mochicard API error: {response.text}")

