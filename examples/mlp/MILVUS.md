
# Changes in mlp/model.py to use Milvus

Requierment: Extract feature vector / vector respresentation of input

## For storing feature between epochs
* Add a `hook` variable to store feature of a **second last layer** and return it with the original output.

## For practical usage (haven't implement yet) to store feature when model is trained
* Keep the forward function as original.
* Write additional one extract feature vector.