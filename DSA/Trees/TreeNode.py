
class TreeNode:
    """The Node of a Binary tree with left and right subtrees and a key and value
    """

    def __init__(self, data):

        self.data = data
        self.left = None
        self.right = None

    def __str__(self) -> str:
        return "{"+" data={}, left:{}, right:{}".format( self.data, self.left == None, self.right == None)+"}"

    def toDict(self):
        """turns a node into a dictionary

        Returns:
           Dictionary : dictionary containing the properties of a node
        """
        return "{"+" data:{}, left:{}, right:{}".format( self.data, self.left == None, self.right == None)+"}"
