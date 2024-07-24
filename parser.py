from bs4 import BeautifulSoup
import pandas as pd

# Path to the HTML file
html_file_path = 'https://www.circlek.se/drivmedel/drivmedelspriser'

# Read the HTML file
with open(html_file_path, 'r', encoding='utf-8') as file:
    soup = BeautifulSoup(file, 'lxml')

# Find the table in the HTML
table = soup.find('table')

# Extract the headers
headers = [header.text.strip() for header in table.find_all('th')]

# Extract the rows
rows = []
for row in table.find_all('tr'):
    cells = row.find_all('td')
    if cells:
        rows.append([cell.text.strip() for cell in cells])

# Create a DataFrame using pandas
df = pd.DataFrame(rows, columns=headers)

# Display the DataFrame
print(df)
