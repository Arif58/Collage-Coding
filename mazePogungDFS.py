arr = [
    [1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,0,1,1,1,1,0,1,1,1,1,0,1,0,0,1,1],
    [1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,0,1,1,1,1,0,1,1,1,1,0,1,0,0,1,1],
    [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,1,0,0,0,0],
    [1,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,0,1,1,1,1,1,1,0,0,0,0],
    [0,0,0,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,0,1,1,1,1,1,1,0,0,1,1],
    [1,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,0,0,0,0,0,0,0,1,0,1,1],
    [1,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,0,1,1,1,1,1,1,0,0,1,1],
    [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0],
    [1,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,0,1,1,1,1,1,1,0,0,1,1],
    [1,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,0,1,0,0,0,0,0,1,0,1,1],
    [1,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,0,1,0,1,1,1,1,0,0,1,1],
    [1,1,0,0,0,0,0,0,0,1,1,1,1,1,0,1,1,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0],
    [1,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,1,1,1,0,0,1,1],
    [1,1,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,1,1,1,0,0,1,1],
    [0,0,0,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,1,0,1,1],
    [1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,0,0,0,0],
    [1,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,0,0,1,1],
    [1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,2,1,0,1,1],
    [1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,0,0,1,1],
    [1,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,1,1,0,1,1,1,1,1,1,1,1,0,0,0,0],
    [1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,0,0,1,1]
]
visited = [[0 for i in range(32)] for j in range(21)]

koordinatAwalX = input('Masukan Koordinat Awal x: ')
x = int(koordinatAwalX)
koordinatAwalY = input('Masukan Koordinat Awal y: ')
y = int(koordinatAwalY)
#class stack untuk checkpoint
class Stack:
    def __init__(self):
        self.list = []
    
    def push(self, checkpoint):
        self.list.append(checkpoint)

    def pop(self):
        self.list.pop()

    def get_list(self):
        return self.list
    
    def is_empty(self):
        if len(self.list)==0:
            return True
        return False

#stack untuk menyimpan checkpoint
stack = Stack()

#masukan koordinat inputan ke dalam stack
tail = koordinatAwalX+","+koordinatAwalY
stack.push(tail)

#untuk mengecek apakah checkpoint
def is_checkpoint(x, y):
    if (x>0 and x<len(arr)-1 and y>0 and y<len(arr[0])-1):
        if (arr[x][y-1]!=1 and arr[x][y+1]!=1 and arr[x-1][y]==1 and arr[x+1][y]==1): #koordinat yang bukan chekpoint (jalan lurus horizontal)
            return False
        if (arr[x][y-1]==1 and arr[x][y+1]==1 and arr[x-1][y]!=1 and arr[x+1][y]!=1): #koordinat yang bukan chekpoint (jalan lurus vertikal)
            return False
        return True
    return True

#untuk mengecek apakah jalananya buntu (tidak ada jalan)
def is_buntu(x, y):
    if (x>0 and arr[x-1][y]==0 and not visited[x-1][y]):
        return False
    if (y<len(arr[0])-1 and arr[x][y+1]==0 and not visited[x][y+1]):
        return False
    if (x<len(arr)-1 and arr[x+1][y]==0 and not visited[x+1][y]):
        return False
    if (y>0 and arr[x][y-1]==0 and not visited[x][y-1]):
        return False
    return True

#untuk rekursi dfs dengan urutan atas-kanan-bawah-kiri
def dfs(x, y):

    #sudah visited
    visited[x][y] = 1

    #cek apakah merupakan jalan keluar
    if (arr[x][y] == 2):
        stack.push("KELUAR")
        list_ = stack.get_list()
        print(list_)

    #cek checkpoint
    if is_checkpoint(x,y):
        s = str(x)+","+str(y)
        if s == tail:
            stack.pop()
        if s == '0,3':
            stack.push('1')
        elif s == '0,8':
            stack.push('2')
        elif s == '0,16':
            stack.push('3')
        elif s == '0,21':
            stack.push('4')
        elif s == '0,26':
            stack.push('5')
        elif s == '2,8':
            stack.push('6')
        elif s == '2,14':
            stack.push('7')
        elif s == '2,16':
            stack.push('8')
        elif s == '2,21':
            stack.push('9')
        elif s == '2,26':
            stack.push('10')
        elif s == '4,0':
            stack.push('11')
        elif s == '4,2':
            stack.push('12')
        elif s == '5,21':
            stack.push('13')
        elif s == '5,27':
            stack.push('14')
        elif s == '7,2':
            stack.push('15')
        elif s == '7,8':
            stack.push('16')
        elif s == '7,14':
            stack.push('17')
        elif s == '7,21':
            stack.push('18')
        elif s == '9,23':
            stack.push('19')
        elif s == '9,27':
            stack.push('20')
        elif s == '11,2':
            stack.push('21')
        elif s == '11,8':
            stack.push('22')
        elif s == '11,17':
            stack.push('23')
        elif s == '11,21':
            stack.push('24')
        elif s == '11,23':
            stack.push('25')
        elif s == '13,8':
            stack.push('26')
        elif s == '13,14':
            stack.push('27')
        elif s == '13,17':
            stack.push('28')
        elif s == '14,0':
            stack.push('29')
        elif s == '14,2':
            stack.push('30')
        elif s == '14,23':
            stack.push('31')
        elif s == '14,25':
            stack.push('32')
        elif s == '14,27':
            stack.push('33')
        elif s == '16,2':
            stack.push('34')
        elif s == '16,8':
            stack.push('35')
        elif s == '17,16':
            stack.push('36')
        elif s == '17,19':
            stack.push('37')
        elif s == '17,25':
            stack.push('38')
        elif s == '19,2':
            stack.push('39')
        elif s == '19,5':
            stack.push('40')
        elif s == '19,8':
            stack.push('41')
        elif s == '19,16':
            stack.push('42')
        elif s == '20,19':
            stack.push('43')
        elif s == '2,2':
            stack.push('44')
        else:
            stack.push(s)

    #cek atas
    if (x>0 and arr[x-1][y]!=1 and not visited[x-1][y]):
        dfs(x-1, y)

    #cek kanan
    if (y<len(arr[0])-1 and arr[x][y+1]!=1 and not visited[x][y+1]):
        dfs(x, y+1)
    
    #cek bawah
    if (x<len(arr)-1 and arr[x+1][y]!=1 and not visited[x+1][y]):
        dfs(x+1, y)
    
    #cek kiri
    if (y>0 and arr[x][y-1]!=1 and not visited[x][y-1]):
        dfs(x, y-1)
    
    #cek mentok
    if (is_buntu(x,y) and not stack.is_empty() and is_checkpoint(x, y)):
        stack.pop()

#start
dfs(x,y)
