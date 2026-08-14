# import chromadb
# print(chromadb.__version__)
# import dotenv
# chroma_client = chromadb.Client()
# from datetime import datetime

# collection = chroma_client.create_collection(
#     name="my_collection",
#     metadata={
#         "description": "my first Chroma collection",
#         "created": str(datetime.now())
#     }
# )

# # 
# collection.add(
#     ids= ['id1', 'id2'],
#     documents=[
#         "This is a document about pineapple",
#         "This is a document about oranges"
#     ],
# )
# collection.modify(
#     name="new_name_of_collection",
#     metadata={"description": "new description"}
# )
# list_collection = chroma_client.list_collections()

# print(list_collection)
# print(collection.peek())
# print(collection.count())
# # list = chroma_client.list_collections()
# # print(list)


# # result = collection.query(
# #     query_texts=["This is a document about huwai"],
# #     n_results=1,
# #     include=['documents']
# # )
# # print(result)
# import chromadb
# print(chromadb.__version__)
# import dotenv
# chroma_client = chromadb.Client()
# from datetime import datetime

# collection = chroma_client.create_collection(
#     name="my_collection",
#     metadata={
#         "description": "my first Chroma collection",
#         "created": str(datetime.now())
#     }
# )

# # 
# collection.add(
#     ids= ['id1', 'id2'],
#     documents=[
#         "This is a document about pineapple",
#         "This is a document about oranges"
#     ],
# )
# collection.modify(
#     name="new_name_of_collection",
#     metadata={"description": "new description"}
# )
# list_collection = chroma_client.list_collections()

# print(list_collection)
# print(collection.peek())
# print(collection.count())
# # list = chroma_client.list_collections()
# # print(list)


# # result = collection.query(
# #     query_texts=["This is a document about huwai"],
# #     n_results=1,
# #     include=['documents']
# # )
# # print(result)

import chromadb

chroma_client = chromadb.Client()
collection = chroma_client.get_or_create_collection(name="my_collection")

# Correct way: Put your links inside 'metadatas' instead of 'uris'
collection.add(
    ids=['id1', 'id2'],
    documents=[
        "This is a document about pineapple",
        "This is a document about oranges"
    ],
    metadatas=[
        {
            "category": "tropical", 
            "stock": 50, 
            "source_url": "https://example.com"
        }, 
        {
            "category": "citrus", 
            "stock": 120, 
            "source_url": "https://example.com"
        }
    ]
)

# Fetching the data to see the clean layout
print(collection.get())
