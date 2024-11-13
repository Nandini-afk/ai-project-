
import wikipedia
def get_wikipedia_summary(query, language='en'):
    try:
        wikipedia.set_lang(language)
        summary = wikipedia.summary(query)
        return summary
    except wikipedia.exceptions.DisambiguationError as e:
        try:
            summary = wikipedia.summary(e.options[0])
            return f"Showing results for '{e.options[0]}':\n\n" + summary
        except Exception as e:
            return "Sorry, I couldn't find a relevant summary."
    except wikipedia.exceptions.PageError
        return "Sorry, I couldn't find anything on that topic."
    except Exception as e:
        return f"An error occurred while searching. Please try again. Error: {str(e)}"

def chatbot():
    print("Hi, I'm your enhanced Wikipedia chatbot! Type 'quit' to exit.")

    # Ensure language is set to a valid code, e.g., 'en' for English
    language = input("Which language would you like to use (default is English, e.g., 'es' for Spanish)? ").lower()
    if language == 'english':
        language = 'en'  # Convert "english" to the proper code
    elif not language:
        language = 'en'  # Default to English if no input

    while True:
        subject = input("\nWhat topic would you like to know about? (or type 'quit' to exit): ")
        if subject.lower() == 'quit':
            print("Goodbye!")
            break
        response = get_wikipedia_summary(subject, language)
        if "This topic is ambiguous." in response:
            print(response)
            chosen_topic = input("\nPlease type one of the options above or enter a new query: ")
            response = get_wikipedia_summary(chosen_topic, language)

        print("\n" + response + "\n")

chatbot()
