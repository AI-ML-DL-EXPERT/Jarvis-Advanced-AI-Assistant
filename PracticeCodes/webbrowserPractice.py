import logging
import webbrowser


def search_on_google(query):
    """Opens Google search results for the provided query in the default browser.

  Logs an informative message if the operation is successful or encounters an error.
  """
    url = f"https://www.google.com/search?q={query}"  # Construct search URL
    try:
        webbrowser.open(url)
        logging.info(f"Opened Google search for: {query}")
    except webbrowser.Error as e:
        logging.error(f"Failed to open Google search: {e}")


# Example usage with basic logging configuration
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)  # Set logging level for informative messages
    search_term = input("Enter your search term: ")
    search_on_google(search_term)
