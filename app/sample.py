import csv
import os

def main(file_path: str, num_of_rows: int):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        rows = [next(reader) for _ in range(num_of_rows)]

    new_file_path = os.path.splitext(file_path)[0] + f"_{num_of_rows}.csv"
    with open(new_file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

if __name__ == "__main__":
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dataset/Reviews.csv')
    num_of_rows = 10
    main(file_path, num_of_rows)
