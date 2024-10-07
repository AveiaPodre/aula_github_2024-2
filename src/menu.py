class Menu:
    def __init__(self, options, title="Menu"):
        self.title = title
        self.options = options

    def get_selection(self):
        op = 0
        while op == 0:
            print(f"{self.title}\n")
            for i, option in enumerate(self.options, start=1):
                print(f"{i} - {option}")

            try:
                op = int(input("Informe a opção desejada: "))
            except ValueError:
                op = 0

            if op < 1 or op > len(self.options):
                print("Opção errada!")
                op = 0

        return op