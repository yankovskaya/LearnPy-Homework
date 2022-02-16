# Задание 1

dictionary = {"city": "Москва", "temperature": "20"}
print(dictionary["city"])
temp = int(dictionary["temperature"]) - 5
dictionary["temperature"] = str(temp)
print(dictionary)

# Задание 2

dictionary = {"city": "Москва", "temperature": "20"}
print('country' in dictionary)
print(dictionary.get("country", "Россия"))
dictionary["date"]= "27.05.2019"
print(len(dictionary))


