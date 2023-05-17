import os
import requests

linkedin_test_json_url = "https://gist.githubusercontent.com/emarco177/0d6a3f93dd06634d95e46a2782ed7490/raw/fad4d7a87e3e934ad52ba2a968bad9eb45128665/eden-marco.json"

def scrap_linkedin_profile():
    """scrape information from linkedin profiles,
    Manually scrape the information from the LinkedIn profiles"""

    response = requests.get(url=linkedin_test_json_url)

    return response
