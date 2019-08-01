import re
import requests
import json
from bs4 import BeautifulSoup


class MovieScraper:

    @staticmethod
    def get_movie(movie):
        # Required variable for the search request
        url = "https://putlocker.kz/search?keyword=" + movie
        get_posts_url = "https://putlocker.kz/get-links/"

        # Search request
        search_results = requests.post(url).content
        soup = BeautifulSoup(search_results, "html.parser")

        # We search for the link of the first result
        # This is not the best way I'll change it later so it finds the exact show/movie
        src_movie = soup.find("a", attrs={"class": "ml-mask"})["href"]

        # We get the HTML of the movie/show
        page = requests.get(src_movie)

        # We search for the variables to make a post request to putlocker's server
        # They store two variables in a script that are later used to make a request to get the links
        soup = BeautifulSoup(page.content, "html.parser")
        scripts = str(soup.find_all("script"))

        # We search for the variable id on the script
        movie_id = re.compile("var id = (.*?);")
        search = movie_id.search(scripts)
        # We get the first result(since there's only one) and remove the quotation marks
        movie_id = str(search.groups()[0].replace("'", ""))

        # Repeat the same step with variable e
        e = re.compile("var e = (.*?);")
        search = e.search(scripts)
        e = str(search.groups()[0].replace("'", ""))

        # Required parameters for the request
        body = {"id": movie_id, "e": e}
        links_json = requests.post(get_posts_url, data=body).content  # .replace("[", "").replace("]", "")

        links_json = json.loads(links_json)
        links = []
        for link in links_json:
            links.append(link['src'])

        return links
