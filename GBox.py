class GBox():
    def __init__(self, lv=0, wid=8, hig=5):
        if not wid:
            raise ValueError('width error')
        if hig < 3:
            raise ValueError('height error')
        self.wid = wid  # 不含線 字寬
        self.hig = hig  # 高
        self.lv = lv

        self.arr = ['']*self.hig
        self.mid_line = self.hig//2

        self.arr[0] = '┏'+'━'*(wid) + '┓'
        for i in range(1, self.hig-1):
            self.arr[i] = '┃'+' '*(self.wid) + '┃'
        self.arr[-1] = '┗'+'━'*(wid)+'┛'
        if self.lv:
            self.upd(self.lv)

    def upd(self, lv):
        self.lv = lv
        if self.lv:
            self.arr[self.mid_line] = '┃' + \
                f'{str(2**(self.lv)):^{self.wid}}'+'┃'
        else:
            self.arr[self.mid_line] = '┃'+' '*(self.wid) + '┃'

    def __repr__(self):
        return '\n'.join(self.arr)


if __name__ == '__main__':
    for i in range(5):
        test = GBox(lv=i)
        print(test)
