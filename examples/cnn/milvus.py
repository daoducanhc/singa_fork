import numpy as np
from pymilvus import (
    connections,
    utility,
    FieldSchema, CollectionSchema, DataType,
    Collection,
)
import random

class MilvusDatabase():

    def __init__(self, db_name="feature"):
        connections.connect("default", host="localhost", port="19530")

        self.db_name = db_name
        self.db = self.initDb()

        self.index = self.db.index

    def initDb(self):
        has = utility.has_collection(self.db_name)
        print(f"Does collection {self.db_name} exist in Milvus: {has}")

        if has:
            collection = Collection(self.db_name)
            collection.load()
            return collection

        # fields = [
        #     FieldSchema(name="pk", dtype=DataType.VARCHAR, is_primary=True, auto_id=False, max_length=100),
        #     FieldSchema(name="random", dtype=DataType.DOUBLE),
        #     FieldSchema(name="embeddings", dtype=DataType.FLOAT_VECTOR, dim=_dim)
        # ]
        # schema = CollectionSchema(fields, "test milvus")

        # index = FieldSchema(
        #     name="index",
        #     dtype=DataType.INT64,
        #     is_primary=True,
        #     # auto_id=True, # this will randomly generate id
        # )

        # epoch = FieldSchema(
        #     name="epoch",
        #     dtype=DataType.INT64,
        # )

        # feature_id = FieldSchema(
        #     name="feature_id",
        #     dtype=DataType.INT64,
        # )

        feature_vector = FieldSchema(
            name="feature_vector",
            dtype=DataType.FLOAT_VECTOR,
            dim=6400,
        )

        schema = CollectionSchema(
            # fields=[index, epoch, feature_id, feature_vector],
            fields=[feature_vector],
            description="Collection with float vector",
        )
        return Collection(self.db_name, schema)
    
    def flush(self):
        self.db.flush()
                
    def deleteDb(self):
        utility.drop_collection(self.db_namedb_name)


if __name__ == "__main__":
    milvusObj = MilvusDatabase()

    vector = [random.random() for _ in range(6400)]
    # print(vector)
    # data = vector
    data = [
        [vector]
    ]
    milvusObj.db.insert(data)