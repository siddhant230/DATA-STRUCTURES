class TrieNode:
    def __init__(self, char):
        self.data = char
        self.counter = 1
        self.childs = [None for _ in range(ord('a'),ord('z')+1)]

class Trie:
    def __init__(self, head):
        self.head = head

    def insert_node(self, string):
        temp = self.head

        for s in string:
            position = ord(s) - ord('a')

            if temp.childs[position] is None:
                #print('creating new node')
                temp.childs[position] = TrieNode(s)
                temp = temp.childs[position]

            else:
                #print('inc node')
                temp = temp.childs[position]
                temp.counter += 1


    def query_check(self, query):
        temp = self.head

        completed = True
        prev = None

        for q in query:
            position = ord(q) - ord('a')
            if temp.childs[position] is not None:
                prev = temp
                temp = temp.childs[position]
                print(temp.data, temp.counter)
            else:
                completed = False

        if completed:
            return prev.childs[position].counter
        else:
            return None

    def deleteNode(self, string):
        temp = self.head

        for s in string:
            position = ord(s) - ord('a')
            if temp.childs[position].counter > 1:
                if temp.childs[position] is not None:
                    temp = temp.childs[position]
                    temp.counter -= 1
            else:
                temp.childs[position] = None


if __name__ == "__main__":
    head = TrieNode('*')

    trie = Trie(head)

    string_list = ['call', 'cam', 'cat', 'calmer']
    for all_str in string_list:
        trie.insert_node(all_str)

    query_strings = ['ca', 'cold']
    for query_str in query_strings:
        print("num of occurences : {}".format(trie.query_check(query_str)))

    trie.deleteNode('cat')

    query_strings = ['ca', 'cold','cat']
    for query_str in query_strings:
        print("num of occurences : {}".format(trie.query_check(query_str)))

    trie.insert_node('cat')

    query_strings = ['ca', 'cold','cat']
    for query_str in query_strings:
        print("num of occurences : {}".format(trie.query_check(query_str)))
