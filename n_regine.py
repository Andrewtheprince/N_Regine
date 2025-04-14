class NRegine():
    def __init__(self):
        pass

    def solve(self, N):
        self._ricorsione([], N)

    def is_ammissible(self, regina1, regina2):
        if regina1[0] == regina2[0]:
            return False
        if regina1[1] == regina2[1]:
            return False
        if regina1[0] + regina1[1] == regina2[0] + regina2[1]:
            return False
        if regina1[0] - regina1[1] == regina2[0] - regina2[1]:
            return False
        return True

    def is_soluzione(self, parziale):
        for i in range(len(parziale) - 1):
            for j in range(i + 1,len(parziale)):
                result = self.is_ammissible(parziale[i], parziale[j])
                if not result:
                    return False
        return True

    def is_valid(self, nuova_regina, parziale):
        for regina in parziale:
            if not self.is_ammissible(nuova_regina, regina):
                return False
        return True


    def _ricorsione(self, parziale, N):
        if len(parziale) == N:
            if self.is_soluzione(parziale):
                print(parziale)
        else:
            for riga in range(N):
                for col in range(N):
                    parziale.append([riga, col])
                    self._ricorsione(parziale, N)
                    parziale.pop()


if __name__ == "__main__":
    nreg = NRegine()
    nreg.solve(4)