import logging
import wikipedia

def get_wikipedia_introduction(search_term, sentences=2):
  """Retrieves a brief introduction of the provided search term from Wikipedia.

  Handles potential errors like disambiguation or page not found, logging informative messages.

  Args:
      search_term (str): The topic to search for on Wikipedia.
      sentences (int, optional): The number of sentences for the summary. Defaults to 2.

  Returns:
      str: The retrieved summary of the search term or an informative error message.
  """
  logging.basicConfig(level=logging.INFO)  # Set logging level

  try:
    summary = wikipedia.summary(search_term, sentences=sentences)
    logging.info(f"Successfully retrieved summary for: {search_term}")
    return summary
  except wikipedia.DisambiguationError as e:
    logging.warning(f"Disambiguation required: {e}")
    return f"Disambiguation required for '{search_term}': {e}"
  except wikipedia.PageError as e:
    logging.warning(f"Page not found: {e}")
    return f"Wikipedia page not found for '{search_term}'"
  except Exception as e:
    logging.error(f"An unexpected error occurred: {e}")
    return f"An error occurred while retrieving information for '{search_term}'"

# Example usage
search_term = "Quantum Computing"
introduction = get_wikipedia_introduction(search_term)
print(introduction)
