# Install Milvus 
* [Guide](https://milvus.io/docs/install_standalone-docker.md)

# Changes in cnn folder

milvus.py
* MilvusDatabase class for easy control and implement milvus object

train_cnn.py
* Haven't run and test, just a draft of workflow:
    * Get `hook` in each epoch 
    * Insert into Milvus db