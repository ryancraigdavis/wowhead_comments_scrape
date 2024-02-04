import requests
from bs4 import BeautifulSoup

def scrape_wowhead(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page using Beautiful Soup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract the desired information from the parsed HTML
        # Adjust this part based on the specific content you want to scrape
        
        # Example: Print the titles of all elements with the class 'title'
        titles = soup.find_all(class_='title')
        for title in titles:
            print(title.text)
            
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

if __name__ == "__main__":
    # Replace the URL with the specific webpage you want to scrape
    url = "https://www.wowhead.com/wotlk"
    
    # Call the function with the URL
    scrape_wowhead(url)
