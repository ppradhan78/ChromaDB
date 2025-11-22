import chromadb
import uuid
import os

os.environ["CHROMA_TELEMETRY_ENABLED"] = "true"

# chroma_client = chromadb.Client()
# chroma_client = chromadb.PersistentClient(path="chroma_storage")
chroma_client = chromadb.PersistentClient(path="./country")
# chroma_client = chromadb.HttpClient(host="localhost",port=8000)
# chroma_client = chromadb.CloudClient(path="./country")

# collection = chroma_client.create_collection(name="capitals")
collection = chroma_client.get_or_create_collection(name="capitals")
with open("files/capitals.txt", "r",encoding="utf-8") as f:
    contents:list[str] = f.read().splitlines()

# print(contents)
collection.add(
    ids=[str(uuid.uuid4()) for _ in contents],
    documents=contents,
    metadatas=[{"line":line} for line in range(len(contents))]
)
# print(collection.peek())

results = collection.query(
    query_texts=["What is the Capitals of Telangana","What is the Capitals of Odisha"], # Chroma will embed this for you
    n_results=1 # how many results to return
)
# print(results)
for i,query_result  in enumerate(results["documents"]):
    print(f"\nQuery {i}")
    print("\n".join(query_result))

