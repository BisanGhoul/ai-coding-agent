from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content

def test_get_file_info():
    print("Result for current directory:")
    print(get_files_info("calculator", "."))

    print("\nResult for 'pkg' directory:")
    print(get_files_info("calculator", "pkg"))

    print("\nResult for '/bin' directory:")
    print(get_files_info("calculator", "/bin"))

    print("\nResult for '../' directory:")
    print(get_files_info("calculator", "../"))

def test_get_file_content():

    result = get_file_content("calculator", "lorem.txt")
    print(f"lorem.txt length: {len(result)}")
    print(f"lorem.txt truncated: {'truncated' in result}")

    print(get_file_content("calculator", "main.py"))
    print(get_file_content("calculator", "pkg/calculator.py"))
    print(get_file_content("calculator", "/bin/cat"))
    print(get_file_content("calculator", "pkg/does_not_exist.py"))


# test_get_file_info();
test_get_file_content();