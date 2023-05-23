import csv


def save_to_csv(data, file_name):
    headers = list(data[0].keys())

    with open(file_name, "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)
