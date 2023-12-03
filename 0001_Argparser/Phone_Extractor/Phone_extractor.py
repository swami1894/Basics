from argparse import ArgumentParser
from pathlib import Path
import re
from time import perf_counter


def update_phone_pattern(phone_number:str) ->str:

    phone_number = re.sub(r'\D', r'', phone_number)

    return f"({phone_number[:3]})-{phone_number[3:6]}-{phone_number[6:]}"


def extractor(filepath:str) -> dict:

    phone_dict = dict()

    with open(filepath) as f:
        lines = f.readlines()

    for line in lines:

        line_content = line.strip().split(' ')

        person = line_content[0]
        phone = update_phone_pattern(line_content[-1])
        
        if person in phone_dict:
            phone_dict[person] .append(phone)
        else:
            phone_dict.setdefault(person, [phone])

    return phone_dict


def validate_file(arg):

    if (file := Path(arg)).is_file():
        return file
    else:
        raise FileNotFoundError(arg)


def main():

    start = perf_counter()
    parser = ArgumentParser()

    parser.add_argument('--path', type=validate_file,
                        help="""Enter the absolute text file path or the relative path if in 
                        the same folder from which numbers have to be extracted.""",
                        required=True)
    
    filepath = parser.parse_args().path
    
    numbers_extracted = extractor(filepath)

    print(numbers_extracted)
    print(f"Time Elapsed: {perf_counter() - start}")
    return None


if __name__ == "__main__":

    main()
