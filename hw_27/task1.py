'''Розширити структуру, яку побудували на уроці,
можливістю вставки дерева в наявне дерево та видалення
піддерева з дерева, що існує.'''


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

def insert_subtree(root, key, subtree, direction='left'):
    # Вставляє піддерево в дерево

    node = search(root, key)

    if node is None:
        print(f'Node with key {key} not found')
        return
    
    if direction == 'left':
        if node.left is not None:
            print(f'Error: the node {key} has a child!')
            return
        node.left = subtree
        
    elif direction == 'right':
        if node.right is not None:
            print(f'Error: the node {key} has a child!')
            return
        node.right = subtree
    
    else:
        print(f'Direction must be "left" or "right"')

def find_parent(root, key):
    # Знаходить батька вузла з ключем key
    
    if root is None or root.key == key:
        return None 
    
    if (root.left and root.left.key == key) or (root.right and root.right.key == key):
        return root
    
    parent = find_parent(root.left, key)
    if parent:
        return parent
    return find_parent(root.right, key)

def delete_subtree(root, key):
    # Видаляє вузол з key і все його піддерево
    if root.key == key:
        print(f'You can\'t delet tree\'s root!')
        return
    
    parent = find_parent(root, key)
    
    if parent is None:
        print(f'Node with key {key} not found')
        return
    
    if parent.left and parent.left.key == key:
        parent.left = None  # Видаляємо ліву гілку
        print(f'Deleted subtree with root {key}')

    elif parent.right and parent.right.key == key:
        parent.right = None  # Видаляємо праву гілку
        print(f'Deleted subtree with root {key}')

def inorder(node):
    # Виводить дерево
    if node:
        inorder(node.left)
        print(node.key, end=' ')
        inorder(node.right)

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

print('Дерево до вставки:')
inorder(root)
print()

new_tree = Node(90)
new_tree.left = Node(85)
new_tree.right = Node(95)

insert_subtree(root, 80, new_tree, 'right')

print('Після вставки:')
inorder(root)
print('\n')

# Тест 2: Видалення піддерева
delete_subtree(root, 30)

print('Після видалення вузла 30:')
inorder(root)
print()