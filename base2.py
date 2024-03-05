import requests
from bs4 import BeautifulSoup
from docx import Document

# Function to scrape university information based on subject from a single page
def scrape_university_info_from_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract relevant information from the website
    # Modify this section based on the structure of the university websites
    
    return university_name, location, program_details  # Sample extracted information

# Function to scrape university information from all pages of search results
def scrape_university_info(subject):
    base_url = f"https://www.example.com/search?subject={subject}"  # Replace with actual search URL
    all_data = []
    
    page_num = 1
    while True:
        url = f"{base_url}&page={page_num}"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract links to individual university pages from the search results page
        links = [link['href'] for link in soup.find_all('a', class_='result-link')]
        
        if not links:
            break
        
        for link in links:
            university_info = scrape_university_info_from_page(link)
            all_data.append(university_info)
        
        page_num += 1
    
    return all_data

# Function to create a Word document and store information in a table
def create_word_document(data):
    doc = Document()
    
    # Add a table to the document
    table = doc.add_table(rows=1, cols=3)
    table.style = 'Table Grid'
    
    # Add headers to the table
    hdr_cells = table.rows[0].cells
    hdr_cells[0].text = 'University Name'
    hdr_cells[1].text = 'Location'
    hdr_cells[2].text = 'Program Details'
    
    # Add data to the table
    for item in data:
        row_cells = table.add_row().cells
        row_cells[0].text = item[0]
        row_cells[1].text = item[1]
        row_cells[2].text = item[2]
    
    doc.save('university_info.docx')

# Main function to orchestrate the process
def main():
    subjects = ['engineering', 'medicine', 'business']  # List of subjects to search for
    
    all_data = []
    
    for subject in subjects:
        university_info = scrape_university_info(subject)
        all_data.extend(university_info)
    
    create_word_document(all_data)

if __name__ == "__main__":
    main()
