import chromadb
print(chromadb.__version__)
import dotenv
chroma_client = chromadb.Client()

collection = chroma_client.create_collection(name="my_collection")

collection.add(
    ids= ['id1', 'id2'],
    documents=[
        "This is a document about pineapple",
        "This is a document about oranges"
    ],
)

new_collection = chroma_client.get_or_create_collection(name='qasim_chroma')

list = chroma_client.list_collections()
print(list)
chroma_client.delete_collection(name="qasim_chroma")
my_collections = chroma_client.list_collections()
print("After delete:", my_collections)

result = collection.query(
    query_texts=["This is a document about huwai"],
    n_results=1,
    include=['documents']
)
print(result)