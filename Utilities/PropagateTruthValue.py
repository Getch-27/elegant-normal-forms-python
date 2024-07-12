from typing import Union
from DataStructures.Trees import *


def propagateTruthValue(
    currentNode: BinaryExpressionTreeNode,
    truthValue: bool = True,
) -> Union[BinaryConstraintTreeNode, None]:
    temporaryNode: BinaryConstraintTreeNode = BinaryConstraintTreeNode("")

    if currentNode.type == NodeType.ROOT:
        temporaryNode.type = currentNode.type
        temporaryNode.value = currentNode.value
        if currentNode.right is not None:
            temporaryNode.right = propagateTruthValue(currentNode.right, truthValue)
        return temporaryNode

    if currentNode.type == NodeType.NOT:
        if currentNode.right is not None:
            return propagateTruthValue(currentNode.right, not truthValue)

    elif currentNode.type in [NodeType.AND, NodeType.OR]:
        if truthValue == False:
            if currentNode.type == NodeType.AND:
                temporaryNode.type = NodeType.OR
                temporaryNode.value = "OR"
            else:
                temporaryNode.type = NodeType.AND
                temporaryNode.value = "AND"

        else:
            temporaryNode.value = currentNode.value
            temporaryNode.type = currentNode.type

        if currentNode.left is not None and currentNode.right is not None:
            temporaryNode.left = propagateTruthValue(currentNode.left, truthValue)
            temporaryNode.right = propagateTruthValue(currentNode.right, truthValue)
        return temporaryNode
    else:
        temporaryNode.value = currentNode.value
        temporaryNode.type = currentNode.type
        temporaryNode.constraint = truthValue
        return temporaryNode
