def main():
    with open('test.cfg') as file:
        cfg = {k:v for k,v in [line.split() for line in file]}
        print cfg

        

main()
