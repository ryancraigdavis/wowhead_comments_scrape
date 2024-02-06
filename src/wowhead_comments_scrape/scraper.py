import requests
from bs4 import BeautifulSoup

def scrape_wowhead(url):
    # Send a GET request to the URL
    response = requests.get(url)
    print(response.status_code)
    
    # This code won't work, switch to Scrapy
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page using Beautiful Soup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract the comments based on the class "Comment wrapper"
        comments = soup.find_all(class_='comment-wrapper')
        
        # Print the content of each comment
        for comment in comments:
            # Modify this part based on the specific structure of the comments
            comment_content = comment.find(class_='comment-text').text
            print(comment_content)


    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

if __name__ == "__main__":
    # Replace the URL with the specific webpage you want to scrape
    url = "https://www.wowhead.com/wotlk/quest=12199"
    
    # Call the function with the URL
    scrape_wowhead(url)
