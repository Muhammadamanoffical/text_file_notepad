def create_file(filename):
    try:
        with open(filename,"x") as f:
            data=input("enter your data that you want to store in file ")
            f.write(data)
    except FileExistsError:
        print(f"file {filename} has been created already")
    except Exception as e:
        print("something went wrong")
def update_data(filename):
    try:
        with open(filename,"a") as f:
            data=input("enter your data")
            f.write(f" \n {data}")
            print("your data successfully update")
    except Exception as e:
        print(f"the error is :{e}")
def read_data(filename):
    try:
        with open (filename,"r") as f:
            content=f.read()
            print(content)
    except Exception as e:
        print(f"Error caught is {e}")