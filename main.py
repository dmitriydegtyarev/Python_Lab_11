import csv

input_file = "index_data.csv"
output_file = "results_data.csv"

def read_csv(file_path):
    try:
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            data = [entry for entry in reader]
            return data
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

def find_gdp(data, year="2019 [YR2019]"):
    if not data:
        return []

    header = data[0]
    try:
        year_index = header.index(year)
    except ValueError:
        print(f"Error: Year {year} not found.")
        return []

    results = []
    for record in data[1:]:
        if record[0] == "GDP per capita (current US$)":
            country = record[2]
            try:
                gdp_value = record[year_index]
                results.append([country, gdp_value])
            except IndexError:
                print(f"Error: Incorrect data format in row {record}")

    return results

def search_country(data, country_name):
    for entry in data:
        if entry[0].lower() == country_name.lower():
            return entry
    return None

def write_csv(file_path, data):
    try:
        with open(file_path, mode='w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Country", "GDP per capita"])
            writer.writerows(data)
        print(f"Result written in '{file_path}'.")
    except Exception as e:
        print(f"Error writing to file: {e}")

csv_data = read_csv(input_file)
if csv_data:
    gdp_data = find_gdp(csv_data)

    for row in gdp_data:
        print(row)

    user_country = input("Enter the country name to search GDP per capita: ")
    result = search_country(gdp_data, user_country)
    if result:
        print(f"GDP per capita у {result[0]}: {result[1]}")
        write_csv(output_file, [result])
    else:
        print(f"Date about '{user_country}' not found.")