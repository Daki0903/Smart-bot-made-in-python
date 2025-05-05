from chat import get_smart_response
from search import search_web, extract_link
import webbrowser

print("=== SmartBot ===")
print("Odaberi režim rada:")
print("1. Internet pretraga")
print("2. Ćaskanje i učenje")
print("3. Izlaz")

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
            otvori = input("Želiš da otvorim link? (da/ne): ").strip().lower()
            if otvori == "da":
                webbrowser.open(link)

elif mode == "2":
    print("\nSmartBot [Ćaskanje]: Pitaj me bilo šta.")
    while True:
        user_input = input("Ti: ").strip()
        if user_input.lower() in ["izlaz", "kraj", "exit"]:
            break
        response = get_smart_response(user_input)
        print("SmartBot:", response)
else:
    print("Doviđenja!")
