import csv
from argparse import ArgumentParser
from multiprocessing import Pool


def read_lines(filepath: str) -> GeneratorExit:

    with open(filepath) as f:
        rowvalues = csv.reader(f)
        for row in rowvalues:
            yield (row)

            
def extract_fields(entry: list[str]1) -> list:
    
    
    
        
        

            
def main():
    
    parser = ArgumentParser()
    parser.add_argument("--path", help="Path to the file")
    
    file_location_obj = parser.parse_args()
    file_location = file_location_obj.path
    
    iterator = iter(read_lines(file_location))
    
    for _ in range(3):
        print(next(iterator))
    
    
    
    
if __name__ == "__main__":
    
    main()
    
    