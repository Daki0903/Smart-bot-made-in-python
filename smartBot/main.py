from chat import get_smart_response
from search import search_web, extract_link
import webbrowser

print("=== SmartBot ===")
print("Select the operating mode:")
print("1. internet search)
print("2. Chatting and learning")
print("3. Exit")

mode = input("Unesi broj režima: ").strip()

if mode == "1":
    print("\nSmartBot [Internet]: Pitaj me nešto.")
    while True:
        query = input("Ti: ").strip()
        if query.lower() in ["izlaz", "kraj", "exit"]:
            break
        result = search_web(query)
        print("SmartBot:", result)

        # Opcija za otvaranje linka
        link = extract_link(query)
        if link:
            otvori = input("Do you want me to open the link? (yes/no): ").strip().lower()
            if otvori == "yes":
                webbrowser.open(link)

elif mode == "2":
    print("\nSmartBot [Chat]: Ask me anything.")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ["Exit", "end", "exit"]:
            break
        response = get_smart_response(user_input)
        print("SmartBot:", response)
else:
    print("Goodbye!")
