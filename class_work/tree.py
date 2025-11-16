class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def search(root, key):
  
    # Base Cases: root is null or key 
    # is present at root
    if root is None or root.key == key:
        return root
    
    # Key is greater than root's key
    if root.key < key:
        return search(root.right, key)
    
    # Key is smaller than root's key
    return search(root.left, key)


root = Node(50)
root.left = Node(30)
root.left.left = Node(20)
root.left.right = Node(40)
root.right = Node(70)
root.right.left = Node(60)
root.right.right = Node(80)

print('=' * 50)
print('Код працює')
print('=' * 50)

result = search(root, 50)
if result:
    print(f'Знайдено 50: {result.key}')
else:
    print(f'50 не знайдено')






