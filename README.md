# Book Highlights Organizer

## Overview

This Python script helps you organize book highlights or annotations from a file into Markdown format.

## Prerequisites

- Python 3.x installed on your machine

## Getting Started

1. **Clone the repository to your local machine:**

    ```bash
    git clone https://github.com/your-username/your-repository.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd your-repository
    ```

3. **Install dependencies (if any):**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Ensure your book highlights file is in the correct format (e.g., "clippings.txt").**

2. **Open the `config.py` file and update the `FILE` variable with the correct path to your book highlights file.**

3. **Run the script:**

    ```bash
    python main.py
    ```

4. **Follow the on-screen prompts to select a book or process all books.**

## Options

- To process all books and generate Markdown files for each, enter "all" when prompted for a book index.

## Output

- If processing a specific book, the script will generate a Markdown file in the "books" directory for that book.

- If processing all books, Markdown files for each book will be created in the "books" directory.

