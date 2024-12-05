#importing all necessary APIs
import requests
import pinyin
import pinyin.cedict
    

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

# def userInput():
    #prompts user to input word that they want to convert to flashcard

    #(this may be more of a form intake thing on the html side)
    #takes input and preps it to be sent to Google Translate API translate method
    #stores input word as a global variable
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

