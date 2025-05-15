def main():
    
    # pointing to which file to read
    filename = "test.txt"

    # read the file
    with open(filename, "r") as f:
        
        # print the current content
        for line in f.readlines():
            print(line, end="")

        # when there's new content, print it
        try:
            while True:
                line = f.readline()
                if line:
                    print(line, end="")
        
        # close the file
        except KeyboardInterrupt as e:
            f.close()
            print(f"Keyboard Interrupt! Closing the file")

if (__name__ == "__main__"):
    main()
