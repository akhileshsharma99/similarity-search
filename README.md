# Sentence Transformer Embeddings and Similarity Search

## Setup
To set up the project, follow these steps:
1. Clone the repository to your local machine.
2. Install the required dependencies using pip:
   ```
   pip install -r requirements.txt
   ```
3. Set up the environment variables `PINECONE_API_KEY` and `PINECONE_ENVIRONMENT`.

## Startup Command
To start the application, run the following command:
   ```
   streamlit run app/main.py
   ```
## Set Pinecone Index Name for Main File
To set the index for the main file, you need to change the `index_name` variable in the `main.py` file. Here is how you can do it:
1. Open the `main.py` file located in the `app` directory.
2. Locate the line where `index_name` is defined. The line should look like this:
   ```python
   index_name = 'lightning-talk'
   ```
3. Change `'lightning-talk'` to the name of your index.
4. Save the changes and close the file.

Now, when you run the application, it will use the new index you have set.

## Load data into pinecone
To load data into the application, you need to first download the dataset and then modify the `load.py` file. Here is how you can do it:

1. Download the dataset from [here](https://www.kaggle.com/datasets/snap/amazon-fine-food-reviews) and add it to the `app/datasets` directory.

2. Open the `load.py` file located in the `app` directory.

3. Locate the line where the `file_path` is defined. The line should look like this:
   ```python
   file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dataset/Reviews.csv')
   ```
4. Change `'dataset/Reviews.csv'` to the path of your CSV file relative to the `load.py` file. If you have followed step 1, this should be `'datasets/your_downloaded_file.csv'`.

5. Locate the line where the `index_name` is defined in the `if __name__ == "__main__"` block. The line should look like this:
   ```python
   if __name__ == "__main__":
       index_name = 'lightning-talk'
   ```
6. Change `'lightning-talk'` to the name of your index.

7. Save the changes and close the file.

Now, when you run the `load.py` script, it will load the data from your CSV file into the specified index.

## Sentence Transformer Embeddings

This project uses Sentence Transformer Embeddings to generate embeddings for text data. Specifically, it uses the all-MiniLM-L6-v2 model for this purpose.

The all-MiniLM-L6-v2 model is a smaller and faster variant of the original Transformer model, which retains most of the original model's performance while significantly reducing its size and computational requirements. This makes it ideal for tasks like this one, where we need to generate embeddings for large amounts of text data quickly and efficiently.


