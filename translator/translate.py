from googletrans import Translator

translator = Translator()

def translates():

    text = input("Text to be translated: ")
    result = translator.translate(text)

    print(result.src)
    print(result.dest)
    print(result.text)

    restart=input("Do you want to translate more ?(y/n)")
    if restart == "y" or restart == "Y":
        translates()


if __name__ == "__main__":
    translates()
