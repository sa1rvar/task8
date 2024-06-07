
#task1
# def relation_to_luke(names):
#     relations = {
#         "Darth Vader": "father",
#         "Leia": "sister",
#         "Han": "brother"
#     }
#     if names in relations:
#         return f"Luke, I am your {relations[names]}"
#
#
#
# print(relation_to_luke("Darth Vader")) #➞ "Luke, I am your father."
# print(relation_to_luke("Leia")) #➞ "Luke, I am your sister."
# print(relation_to_luke("Han")) #➞ "Luke, I am your brother in law."

#task2

# def get_budgets(dict):
#     result = 0
#     for x in dict:
#         a = x.get("budget")
#         result += a
#     return result
# print(get_budgets([
#   { "name": "John", "age": 21, "budget": 23000 },
#   { "name": "Steve",  "age": 32, "budget": 40000 },
#   { "name": "Martin",  "age": 16, "budget": 2700 }
# ])) #➞ 65700
#
# print(get_budgets([
#   { "name": "John",  "age": 21, "budget": 29000 },
#   { "name": "Steve",  "age": 32, "budget": 32000 },
#   { "name": "Martin",  "age": 16, "budget": 1600 }
# ])) #➞ 62600


#task3
# def get_student_names(dict):
#     lst1 = []
#     for x in dict:
#         lst1.append(x)
#     return sorted(dict.values())
#
#
# print(get_student_names({
#     "Student 1": "Steve",
#     "Student 2": "Becky",
#     "Student 3": "John"
# })) #➞ ["Becky", "John", "Steve"]

#task4
# def maximum_score(dict):
#     result = 0
#     for x in dict:
#         a = x.get("score")
#         result += a
#     return result
#
#
# print(maximum_score([
#   { "tile": "B", "score": 2 },
#   { "tile": "V", "score": 4 },
#   { "tile": "F", "score": 4 },
#   { "tile": "U", "score": 1 },
#   { "tile": "D", "score": 2 },
#   { "tile": "O", "score": 1 },
#   { "tile": "U", "score": 1 }
# ])) #➞ 15
#task5







#task6
# def mapping(letters):
#     lst = []
#     for x in letters:
#         a = x.capitalize()
#         lst.append(x)
#         lst.append(a)
#     return lst
# print(mapping(["p", "s"]))# ➞ { "p": "P", "s": "S" }
# print(mapping(["a", "b", "c"])) #➞ { "a": "A", "b": "B", "c": "C" }
# print(mapping(["a", "v", "y", "z"])) #➞ { "a": "A", "v": "V", "y": "Y", "z": "Z" }

#task7
# def count_all(str):
#     dict = {"LETTERS":0,"DIGITS":0}
#     for x in str:
#         if x.isalpha():
#             dict["LETTERS"] += 1
#         if x.isdigit():
#             dict["DIGITS"] += 1
#     return dict
#
# print(count_all("Hello World")) #➞ {"LETTERS": 10, "DIGITS": 0}
# print(count_all("H3ll0 Wor1d")) #➞ {"LETTERS": 7, "DIGITS": 3}
# print(count_all("149990")) #➞ {"LETTERS": 0, "DIGITS": 6}

#task8
# def calc_diff(dict, num):
#     result = 0
#     for x in dict.values():
#         result += x
#     return result - num
# print(calc_diff({"baseball bat": 20 }, 5))# ➞ 15
# print(calc_diff({"skate": 10, "painting": 20 }, 19))# ➞ 11
# print(calc_diff({"skate": 200, "painting": 200, "shoes": 1 }, 400))# ➞ 1

#task9












#task10

# p1 = Person("Samuel", 24)
# p2 = Person("Joel", 36)
# p3 = Person("Lily", 24)
# p1.compare_age(p2) #➞ "Joel is older than me."
# p2.compare_age(p1) #➞ "Samuel is younger than me."
# p1.compare_age(p3) #➞ "Lily is the same age as me."

#task11
# def dict_to_list(dict):
#     result = []
#     for x in dict.items():
#         result.append(x)
#     return result
# print(dict_to_list({
#   "D": 1,
#   "B": 2,
#   "C": 3
# }))# ➞ [("B", 2), ("C", 3), ("D", 1)]
# print(dict_to_list({
#   "likes": 2,
#   "dislikes": 3,
#   "followers": 10
# }))#➞ [("dislikes", 3), ("followers", 10), ("likes", 2)]

# task12
# def space_weights(planet_a,weight,planet_b):





# print(space_weights("Earth", 1, "Mars")) #➞ 0.38
# print(space_weights("Earth", 1, "Jupiter"))# ➞ 2.53
# print(space_weights("Earth", 1, "Neptune"))# ➞ 1.14
# task12
# def get_frequencies(lst):
#     dict = {}
#     for x in lst:
#         lst.count(x)
# print(get_frequencies(["A", "B", "A", "A", "A"]))# ➞ { "A" : 4, "B" : 1 }
# print(get_frequencies([1, 2, 3, 3, 2]))# ➞ { 1: 1, 2: 2, 3: 2 }
# print(get_frequencies([True, False, True, False, False])) #➞ { True: 2, False: 3 }
# print(get_frequencies([])) #➞ {}

# task13
# def oldest(lst):
#     old = max(lst,key=lst.get)
#     return old
# print(oldest({
#   "Emma": 71,
#   "Jack": 45,
#   "Amy": 15,
#   "Ben": 29
# })) #➞ "Emma"
#
# print(oldest({
#   "Max": 9,
#   "Josh": 13,
#   "Sam": 48,
#   "Anne": 33
# })) #➞ "Sam"
# task14
# def topnote(dict):
#     a = max(dict.get("notes"))
#     return f"{dict.items(),dict.pop("notes")}, top_notes:{a}"
# print(topnote({ "name": "John", "notes": [3, 5, 4] })) #➞ { "name": "John", "top_note": 5 }
# print(topnote({ "name": "Max", "notes": [1, 4, 6] })) #➞ { "name": "Max", "top_note": 6 }
# print(topnote({ "name": "Zygmund", "notes": [1, 2, 3] })) #➞ { "name": "Zygmund", "top_note": 3 }

# task15
# def profit(dict):
#     a = sum(dict.values())
#     return a / 12
#
# print(profit({
#   "cost_price": 32.67,
#   "sell_price": 45.00,
#   "inventory": 1200
# })) #➞ 14796
#
# print(profit({
#   "cost_price": 225.89,
#   "sell_price": 550.00,
#   "inventory": 100
# })) #➞ 32411
#
# print(profit({
#   "cost_price": 2.77,
#   "sell_price": 7.95,
#   "inventory": 8500
# })) #➞ 44030





