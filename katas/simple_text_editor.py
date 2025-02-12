class TextEditor:
    def __init__(self) -> None:
        self.text = ''
        self.undo_stack = []

    def append(self, s):
        self.undo_stack.append(self.text)
        self.text += s

    def delete(self, k):
        self.undo_stack.append(self.text)
        if k <= len(self.text):
            self.text = self.text[:-k]

    def print(self, k):
        if k <= len(self.text):
            print(self.text[k-1])

    def undo(self):
        if self.undo_stack:
            self.text = self.undo_stack.pop()


if __name__ == '__main__':
    Q = int(input())
    editor = TextEditor()

    for _ in range(Q):
        opt = input().split()

        if opt[0] == '1':
            editor.append(opt[1])
        elif opt[0] == '2':
            editor.delete(int(opt[1]))
        elif opt[0] == '3':
            editor.print(int(opt[1]))
        else:
            editor.undo()
