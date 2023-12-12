# Workflow:
# 1. Export Google contacts.
# 2. Open .csv file in Google Sheets. (https://docs.google.com/spreadsheets/u/0/)
# 3. Get 'Geocode by Awesome Table' extension for Google Sheets (may only be possible in the Chrome browser).
# 4. Geocode the 'Address 1 - Formatted' column (check the Longitude/Latitude columns for the right formatting).
# 5. Optional: Do the same for the 'Address 2 - Formatted' column.
# 6. Run this code (change input/output path before!).
# If any problems arise, I suggest asking an LLM like ChatGPT.

import csv

# Constants
# CHANGE INPUT/OUTPUT PATHS HERE:
INPUT_CSV_FILE = r'path\to\your\file\contacts.csv'
OUTPUT_KML_FILE = r'desired\output\path\contacts.kml'

try:
    import simplekml
except ImportError:
    print("Error: The 'simplekml' module is not installed. Please install it using 'pip install simplekml'.")
    exit()


def create_kml(input_csv, output_kml):
    kml = simplekml.Kml()

    try:
        with open(input_csv, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                name = row['Name']
                latitude_str, longitude_str = row['Latitude'], row['Longitude']

                # Skip rows with missing latitude or longitude
                if not latitude_str or not longitude_str:
                    continue

                latitude, longitude = float(latitude_str), float(longitude_str)

                # Extracting values directly
                address_type, address_formatted, photo_url = row[
                    'Address 1 - Type'], row['Address 1 - Formatted'], row['Photo']

                # Create marker for Address 1
                placemark = kml.newpoint(
                    name=name, coords=[(longitude, latitude)])
                # Format into HTML for the pop-up
                placemark.description = f"{address_type}<br>\n{address_formatted}\n<img src=\"{photo_url}\">"

                # Check and create marker for Address 2 if present
                if row.get('Address 2 - Formatted') and row.get('Latitude 2') and row.get('Longitude 2'):
                    address_type_2, address_formatted_2, photo_url_2 = row[
                        'Address 2 - Type'], row['Address 2 - Formatted'], row['Photo']
                    latitude_2, longitude_2 = float(
                        row['Latitude 2']), float(row['Longitude 2'])

                    # Modify the name only if there is a second address
                    name_2 = f"{name} ({address_type_2})" if address_type_2 else name

                    placemark_2 = kml.newpoint(
                        name=name_2, coords=[(longitude_2, latitude_2)])
                    # Format into HTML for the pop-up
                    placemark_2.description = f"{address_type_2}<br>\n{address_formatted_2}\n<img src=\"{photo_url_2}\">"

        kml.save(output_kml)
        print(f'KML file "{output_kml}" created successfully.')

    except FileNotFoundError as e:
        print(f"Error: The file '{input_csv}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == '__main__':
    create_kml(INPUT_CSV_FILE, OUTPUT_KML_FILE)
