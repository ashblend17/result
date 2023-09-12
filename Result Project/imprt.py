import requests
from bs4 import BeautifulSoup
import csv

# Send an HTTP request to the webpage and parse the HTML content
url = 'https://erp.iiitkottayam.ac.in/php/2022/1/2022BCS0183.html'  # Replace with the actual URL
response = requests.get(url)

if response.status_code == 200:
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')
else:
    print('Failed to retrieve the webpage.')
    exit()

# Find the third table on the page (index 2 since Python uses 0-based indexing)
tables = soup.find_all('table')
if len(tables) >= 3:
    table = tables[2]
else:
    print('The third table was not found on the webpage.')
    exit()

# Create a CSV file and write the header row
with open('output.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)

    # Write the header row
    header_row = ['Course ID', 'Course Name', 'Grade']
    writer.writerow(header_row)

    # Iterate through the table rows and write the data to the CSV file
    rows = table.find_all('tr')[1:]  # Skip the first row as it contains the column headers
    for row in rows:
        cells = row.find_all('td')
        if len(cells) == 3:
            course_id = cells[0].text.strip()
            course_name = cells[1].text.strip()
            grade = cells[2].text.strip()
            writer.writerow([course_id, course_name, grade])
print('Data from the third table has been scraped and saved to output.csv')