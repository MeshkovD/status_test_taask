from itertools import chain


class TreeStore:
    def __init__(self, items):
        sorted_items = sorted(items, key=lambda x: x["id"])
        flat_items = {}
        for item in sorted_items:
            flat_items[item["id"]] = {
                "item": item,
                "parents": [],
                "children": [],
            }
            if item["parent"] == "root":
                flat_items[item["id"]]['parents'] = [item]
            elif flat_items.get(item["parent"]):
                parent = flat_items[item["parent"]]['item']
                parents_parents = flat_items[item["parent"]]['parents'] if parent['parent'] != 'root' else []
                flat_items[item["id"]]['parents'] = list(chain([parent], parents_parents))
                flat_items[item["parent"]]['children'].append(item)

        self.items = sorted_items
        self.flat_items = flat_items

    def getAll(self):
        return self.items

    def getItem(self, id):
        return self.flat_items[id]["item"]

    def getChildren(self, id):
        return self.flat_items[id]["children"]

    def getAllParents(self, id):
        return self.flat_items[id]["parents"]
