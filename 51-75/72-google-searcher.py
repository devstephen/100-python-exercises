import webbrowser

query = input("Enter your query  ")
url = f"https://www.google.com/search?q={query}"



webbrowser.open(url)

# Explanation:

# We're using webbrowser  here which is a standard library that is used to open a web browser.

# First, we're getting the search term stored in variable query via the input  function. 
# You need to first do a manual search on Google and observe how Google will construct the URL. 
# Depending on where you are in the world the URL may be different, but the above URL should work everywhere.

# You will see that the URL contains your search term at the end. 
# Therefore, we concatenate the first part of the URL with the search term we get from input .