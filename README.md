
# Amazon Search API


## FLASK API Setup







1] Clone the repository to your local machine:

```bash
  git clone https://github.com/pp5253397/amazon-search-api-python
```

2] Go to Backend Folder and install dependencies:

```bash
  pip3 install -r requirements.txt
```

3] Run Flask App:

```bash
  Flask run
```

## React Setup

1] Go to Frontend Folder and go to amazon app folder. Install dependencies:

```bash
  npm -i
```

2] Run React App using below command:

```bash
  npm start
```
## Usage

1. Enter a keyword in the search form on the React app.
2. Click the "Search" button.
3. The React app will send a POST request to the Flask API with the keyword parameter.
4. The Flask API will scrape the search results from Amazon and return them as a JSON array.
5. The React app will display the list of products on the page.
