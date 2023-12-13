# Workflow:
# 1. Export Google contacts as Google CSV.
<img width="223" alt="image" src="https://github.com/krischimk/Google-Contacts-to-Google-Earth/assets/121830124/d7627821-828e-4d9c-9c5c-7ffeaab7db9a">

# 2. Open .csv file in Google Sheets. 
(https://docs.google.com/spreadsheets/u/0/)
# 3. Get 'Geocode by Awesome Table' extension for Google Sheets.
(may only be possible in the Chrome browser)<br>
<img width="653" alt="image" src="https://github.com/krischimk/Google-Contacts-to-Google-Earth/assets/121830124/61c2a75b-4567-4e7f-9cfa-22ef2a447401">

# 4. Geocode the 'Address 1 - Formatted' column.
<img width="525" alt="image" src="https://github.com/krischimk/Google-Contacts-to-Google-Earth/assets/121830124/6125d3bc-55dd-4bfc-b310-627c3fbc252c">
<br>Check the values in the Longitude/Latitude columns if they have the right formatting.<br>
If it's wrong, change the the country/language setting in the file settings to 'United States' and geocode again.<br>

# 5. Optional: Do the same for the 'Address 2 - Formatted' column.
You then have to rename the new Longitude and Latitude columns to 'Longitude 2' and 'Latitude 2'<br>
<img width="277" alt="image" src="https://github.com/krischimk/Google-Contacts-to-Google-Earth/assets/121830124/106d5136-398f-45c9-b7d9-32b32f806652">

# 6. Run the Python code (change input/output path in the code before running it).
# If any problems arise, I suggest asking an LLM like ChatGPT.
