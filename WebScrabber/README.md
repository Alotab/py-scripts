This python script uses `requests` library to send GET request to the URL: `https://www.python.org/blogs/` page. We use BeautifulSoup library to parse the HTML content of the page.

The main aim of this scrapper is to scrab all the blog titles from the URL given. So we find all the blog titles on the page by searching for `h` elements with class `event-titl`'.

Each result is printed to the terminal and save all in a file called `blog_title_file.txt`.
