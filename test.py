import NeuralNetwork

C = NeuralNetwork.NeuralNet([3,2,1])
C.forwardpass([2,3,1])
print(C.weights)
for layer in C.layers:
    for node in layer.nodes:
        print(node.input)
        print(node.output)
        print()