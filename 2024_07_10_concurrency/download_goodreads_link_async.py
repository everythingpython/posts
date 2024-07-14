from time import sleep
from googlesearch import search

from concurrent.futures import ThreadPoolExecutor
import pandas as pd
import time


def download_book(title):
    """
    Downloads book information by searching for the title on Goodreads.

    Parameters:
        title (str): The title of the book.

    Returns:
        dict: A dictionary with the book title as the key and the Goodreads link as the value.
    """
    title_dict = {}
    print(f"Processing {title}\r")

    try:
        search_results = search(f"{title} goodreads", num_results=5)
        first_result = None

        for result in search_results:
            if first_result is None:
                first_result = result
            if "goodreads.com/book/show" in result:
                title_dict[title] = result
                break

        if title_dict.get(title) is None:
            title_dict[title] = first_result

    except Exception as e:
        print(f"Error processing {title}: {e}")
        title_dict[title] = "No link found"

    sleep(5)  # Simulate delay
    return title_dict


def main():
    time_start = time.time()

    # Read CSV file
    df = pd.read_csv('data/books_5.csv')
    books_list = df["title"].tolist()
    num_books = len(books_list)

    # Determine number of workers
    MAX_WORKERS = 5
    workers = min(MAX_WORKERS, num_books)

    # Download books concurrently
    with ThreadPoolExecutor(workers) as executor:
        res = list(executor.map(download_book, sorted(books_list)))

    # Process the results
    book_list = {"Title": [], "Link": []}
    for result in res:
        for title, link in result.items():
            book_list["Title"].append(title)
            book_list["Link"].append(link)

    # Save results to CSV
    result_df = pd.DataFrame(book_list)
    result_df.to_csv("data/book_links_5.csv", index=False)

    # Print the results
    time_end = time.time()
    time_taken = time_end - time_start
    print(f"Downloaded {num_books} books in {time_taken:.2f} seconds")


if __name__ == "__main__":
    main()
