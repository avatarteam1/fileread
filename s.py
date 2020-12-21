#Drust Krdn w Nusine File
def main():
    f = open("kalary.txt", "w+")
    for i in range(10):
        f.write("Ahmed Up\n")
    f.close()
main()

#Xwendnaway File
def main():
    try:
        x = input("File Bnusa:")
        f = open(x, "r+")
        for f in f.readlines():
            print(f)
    except FileNotFoundError:
        print("File Byne nya")
main()