class Utils:

    @staticmethod
    def get_predicate_for_string_starts_with(search_key):
        def predicate(item):
            return item.startswith(search_key)

        return predicate

    @staticmethod
    def get_names(names, predicate):
        results = []

        for name in names:
            if predicate(name):
                results.append(name)

        return results


names = [
    "Sam",
    "John",
    "Steve",
    "Alice",
    "Sarah",
    "Bob"
]

results = Utils.get_names(
    names,
    Utils.get_predicate_for_string_starts_with("S")
)

for name in results:
    print(name)

results = Utils.get_names(
    names,
    Utils.get_predicate_for_string_starts_with("J")
)

for name in results:
    print(name)
