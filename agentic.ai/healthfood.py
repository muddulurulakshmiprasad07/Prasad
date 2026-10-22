
# import requests

# API_KEY = "HAdGYmsK7StbneuB9taFhCnUlSOzArwguCviW9ht"

# url = "https://api.nal.usda.gov/fdc/v1/foods/search"

# food = input("Enter a food name: ")

# params = {
#     "api_key": API_KEY,
#     "query": food,
#     "pageSize": 5
# }

# try:
#     response = requests.get(
#         url, params=params, timeout=20
#     )
#     response.raise_for_status()

#     data = response.json()
#     foods = data.get("foods", [])

#     if not foods:
#         print("Food not found.")
#     else:
#         for item in foods:
#             print("\nFood:", item["description"])

#             nutrients = item.get("foodNutrients", [])

#             for nutrient in nutrients:
#                 name = nutrient.get("nutrientName", "")
#                 value = nutrient.get("value")
#                 unit = nutrient.get("unitName", "")

#                 if name in [
#                     "Energy",
#                     "Protein",
#                     "Carbohydrate, by difference",
#                     "Total lipid (fat)"
#                 ] and value is not None:
#                     print(f"{name}: {value} {unit}")

# except requests.RequestException as error:
#     print("API request failed:", error)  #program 1
    

