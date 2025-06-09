### 이진트리

- 모든 노드가 최대 두 개의 자식 노드를 가지는 트리구조이다.
- 각 노드는 왼쪽 자식(left child), 오른쪽 자식(right child)을 가진다. 
- 자식이 없는 경우도 허용된다. 

구성요소 

- 루트 노드 (Root Node): 트리의 최상단 노드. 시작점.
- 자식 노드 (Child Node): 다른 노드에서 이어지는 하위 노드.
- 부모 노드 (Parent Node): 자식 노드를 가지는 노드.
- 리프 노드 (Leaf Node): 자식이 없는 노드.
- 서브트리 (Subtree): 트리의 일부 구조를 이루는 하위 트리.

특징

- 각 노드는 0개, 1개, 또는 2개의 자식 노드를 가질 수 있다.
- 노드의 자식 수는 항상 2 이하이다.
- 자식 노드가 없는 경우 `None`, `null`, 또는 문제에 따라 `.`으로 표현되기도 한다.


트리 순회 방식

1. 전위 순회 (Pre-order): 루트 → 왼쪽 → 오른쪽
2. 중위 순회 (In-order): 왼쪽 → 루트 → 오른쪽
3. 후위 순회 (Post-order): 왼쪽 → 오른쪽 → 루트

시간 복잡도 

- 노드 수가 N일 때, 순회 시간은 O(N)이다. (모든 노드를 한 번씩 방문)


python code

```py
# 이진 트리 노드 클래스 정의
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# 전위 순회 (루트 → 왼쪽 → 오른쪽)
def preorder(node, visit):
    if node is None:
        return
    visit.append(node.value)
    preorder(node.left, visit)
    preorder(node.right, visit)

# 중위 순회 (왼쪽 → 루트 → 오른쪽)
def inorder(node, visit):
    if node is None:
        return
    inorder(node.left, visit)
    visit.append(node.value)
    inorder(node.right, visit)

# 후위 순회 (왼쪽 → 오른쪽 → 루트)
def postorder(node, visit):
    if node is None:
        return
    postorder(node.left, visit)
    postorder(node.right, visit)
    visit.append(node.value)

# 예제 트리 구성
#         A
#        / \
#       B   C
#      / \   \
#     D   E   F
root = Node('A')
root.left = Node('B')
root.right = Node('C')
root.left.left = Node('D')
root.left.right = Node('E')
root.right.right = Node('F')

# 순회 결과 담을 리스트
pre_res = []
in_res = []
post_res = []

# 순회 실행
preorder(root, pre_res)
inorder(root, in_res)
postorder(root, post_res)

# 결과 출력
print("전위 순회 결과:", pre_res)   # ['A', 'B', 'D', 'E', 'C', 'F']
print("중위 순회 결과:", in_res)    # ['D', 'B', 'E', 'A', 'C', 'F']
print("후위 순회 결과:", post_res)  # ['D', 'E', 'B', 'F', 'C', 'A']
```

---

