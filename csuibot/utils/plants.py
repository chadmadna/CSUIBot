import random


class Plants:

    def __init__(self, plants_facts=None, file='assets/plants_trivia.txt'):
        self.plants_facts = plants_facts
        if self.plants_facts is None:
            with open(file, 'r', encoding='utf-8-sig') as f:
                self.plants_facts = f.readlines()
                self.plants_facts = [lines.strip() for lines in self.plants_facts]

    def facts(self):
        result = random.choice(self.plants_facts)
        return result
