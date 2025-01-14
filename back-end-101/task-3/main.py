from utils.utils import brush_teeth, do_laundry, make_coffee, prepare_breakfast, read_book

def start_day():
    print("Starting my day...\n")
    brush_teeth()
    print()
    do_laundry()
    print()
    make_coffee()
    print()
    prepare_breakfast()
    print()
    read_book()
    print("Day started successfully!")

if __name__ == "__main__":
    start_day() 