import json
import csv

with open("exercicio4.json") as file:
    livros = json.load(file)
    categories_quantities = {}
    for livro in livros:
        for category in livro['categories']:
            # if not categories_quantities.get(category):
            #     categories_quantities[category] = 0
            # categories_quantities[category] += 1
            if category in categories_quantities:
                categories_quantities[category] += 1
            else:
                categories_quantities[category] = 1

    categories_percentage = [
        [category, number / len(livros)]
        for category, number in categories_quantities.items()
    ]

print(categories_percentage)
headers = ["categoria", "percentagem"]
with open("categories_percentage.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    writer.writerows(categories_percentage)


# import json
# import csv


# def retrieve_books(file):
#     return json.load(file)


# def count_books_by_categories(books):
#     categories = {}
#     for book in books:
#         for category in book["categories"]:
#             if not categories.get(category):
#                 categories[category] = 0
#             categories[category] += 1
#     return categories


# def calculate_percentage_by_category(book_count_by_category, total_books):
#     return [
#         [category, num_books / total_books]
#         for category, num_books in book_count_by_category.items()


# def write_csv_report(file, header, rows):
#     writer = csv.writer(file)
#     writer.writerow(header)
#     writer.writerows(rows)


# if __name__ == "__main__":
#     # retrieve books
#     with open("books.json") as file:
#         books = retrieve_books(file)

#     # count by category
#     book_count_by_category = count_books_by_categories(books)

#     # calculate percentage
#     number_of_books = len(books)
#     books_percentage_rows = calculate_percentage_by_category(
#         book_count_by_category, number_of_books
#     )

#     # write csv
#     header = ["categoria", "percentagem"]
#     with open("report.csv", "w") as file:
#         write_csv_report(file, header, books_percentage_rows)
