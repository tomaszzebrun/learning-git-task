print()

shopping_list = {
    "piekarnia": ["chleb", "pączek", "bulka"],
    "warzywniak": ["marchew", "seler", "rukola"]
}

quantity = 0

print("Lista zakupów")

for shop, things in shopping_list.items():
    print("Idę do " + shop.capitalize() + ", kupuję tu następujące rzeczy: " \
        + str([thing.capitalize() for thing in things]) + ".")
    quantity = quantity + len(things)


print("W sumie kupuję " + str(quantity) + " produktów.")

print()