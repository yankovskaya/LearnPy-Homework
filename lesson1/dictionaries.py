# Задание 1

dictionary = [{"city": "Москва", "temperature": "20"}]
print(dictionary[0]["city"])
dictionary[0]["temperature"] = "15"
print(dictionary)

# Задание 2

dictionary = {"city": "Москва", "temperature": "20"}
print(dictionary.get("country"))
print(dictionary.get("country", "Россия"))
dictionary["date"]= "27.05.2019"
print(len(dictionary))


