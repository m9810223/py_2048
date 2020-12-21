from GBox import GBox
from random import randint


class G2048():
    def __init__(self, hig=4, wid=4, lv_win=11):
        self.wid, self.hig = wid, hig
        self.had_win, self.lv_win = False, lv_win
        self.lv_array = []
        for i in range(self.hig):
            self.lv_array.append([])
            for j in range(self.wid):
                self.lv_array[i].append(0)
        self.box_array = []
        for i in range(self.hig):
            self.box_array.append([])
            for j in range(self.wid):
                self.box_array[i].append(GBox())
        self.spawn()
        self.spawn()

    @staticmethod
    def _left_move(arr):
        re = []
        for r in range(len(arr)):
            tmp, zero_cnt = [], 0
            for c in range(len(arr[r])):
                t = arr[r][c]
                if t:
                    tmp.append(t)
                else:
                    zero_cnt += 1
            # # 只有最左可以合併
            # if len(tmp) >= 2 and tmp[0] == tmp[1]:
            #     tmp = [tmp[0]+1]+tmp[2:]
            #     zero_cnt += 1

            # 非最左也可合併
            if len(tmp) >= 2:
                for i in range(len(tmp)-1):
                    if tmp[i] == tmp[i+1]:
                        tmp = tmp[:i]+[tmp[i]+1]+tmp[i+2:]
                        zero_cnt += 1
                        break
            tmp += [0]*zero_cnt
            re.append(tmp)
        return re

    def move(self,  direction):
        arr = self.lv_array
        if direction in ['up', 'down']:
            arr = self.transpose(arr)
        if direction in ['right', 'down']:
            arr = self.list_reverse(arr)
        arr = self._left_move(arr)
        if direction in ['right', 'down']:
            arr = self.list_reverse(arr)
        if direction in ['up', 'down']:
            arr = self.transpose(arr)
        self.lv_array = arr
        self.spawn()

    def spawn(self):
        r = randint(0, self.hig*self.wid-1)
        done = False
        for i in range(self.hig):
            for j in range(self.wid):
                pos = (i*self.wid+j+r) % (self.hig*self.wid)
                a = pos//self.wid
                b = pos % self.wid
                if self.lv_array[a][b] == 0:
                    self.lv_array[a][b] = 1
                    self._update()
                    return None

    def _update(self):
        win = False if not self.had_win else True
        for i in range(self.hig):
            for j in range(self.wid):
                self.box_array[i][j].upd(self.lv_array[i][j])
                if not win and self.lv_array[i][j] == self.lv_win:
                    win = True
        if win and not self.had_win:
            self.had_win = True

    @staticmethod
    def transpose(arr):
        return list(map(list, zip(*arr)))

    @staticmethod
    def list_reverse(arr):
        return [_[::-1] for _ in arr]

    @staticmethod
    def has_same_adjacent(arr):
        # 檢查是否發生左右相等
        for i in range(len(arr)):
            for j in range(len(arr[i])-1):
                if arr[i][j] in [0, arr[i][j+1]]:
                    return True
            if arr[i][-1] == 0:
                return True
        return False

    def is_alive(self):
        if self.has_same_adjacent(self.lv_array):
            return True
        arr = self.transpose(self.lv_array)
        if self.has_same_adjacent(arr):
            return True
        return False

    def __repr__(self):
        re = []
        for i in self.box_array:
            for j in range(len(i[0].arr)):
                tmp = ''
                for k in range(self.wid):
                    tmp += i[k].arr[j]
                re.append(tmp)
        return str('\n'.join(re)+'\n')


if __name__ == '__main__':
    pass

    g = G2048(1, 4)

    arr = [[0, 2, 2, 1]]
    g.lv_array = arr
    print(g.lv_array)

    g.move('right')
    print(g.lv_array)
