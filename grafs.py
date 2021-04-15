class Grafs:
    def create_graf(graf):
        char_list = list(graf)
        graf = {}
        x = 0 
        for c in char_list:
            graf[x] = c
            x += 1
        return graf