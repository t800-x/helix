from web_scraper import get_data
from ai import get_answer

def main():
    
    print("Welcome to Helix!")
    print("Helix is a chatbot that can answer your queries about anything!")
    
    while True:
        query = input("Enter your query: ")
        context = get_data(query)
        answer = get_answer(context, query)
        print(answer)

if __name__ == "__main__":
    main()
