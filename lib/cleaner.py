class Deduplicate:
    def __init__(self, content):
        self.content = content
        self.result = self.clean(content)

    def clean(self, seq):
        if not isinstance(seq, (list, tuple)):
            raise TypeError("Input must be a list or tuple.")
        
        seen = set()
        seen_add = seen.add
        if isinstance(seq, tuple):
            return tuple(x for x in seq if not (x in seen or seen_add(x)))
        return [x for x in seq if not (x in seen or seen_add(x))]

    def update_content(self, new_content):
        self.content = new_content
        self.result = self.clean(new_content)

    def get_result(self):
        return self.result

if __name__ == "__main__":
    data = [1, 2, 2, 3, 4, 4, 5]
    deduper = Deduplicate(data)
    print(deduper.get_result())

    new_data = [10, 20, 10, 30]
    deduper.update_content(new_data)
    print(deduper.get_result())
