import cProfile
import calendar
import collections
import functools
import getpass
import glob
import http.client
import importlib.util
import inspect
import json
import math
import multiprocessing
import os
import platform
import site
import socket
import struct
import subprocess
import sys
import datetime
import textwrap
import time
import timeit
import traceback
from stat import ST_CTIME, S_ISREG, ST_MODE


### Python Basic (Part - I)
# 1. Formatted Twinkle Poem
def formatted_twinkle_poem():
    print(
        "Twinkle, twinkle, little star, \n\tHow I wonder what you are!\n\t\tUp above the world so high,\n\t\tLike a diamond in the sky.\nTwinkle, twinkle, little star,\n\tHow I wonder what you are!")


# 2. Python Version Checker
def python_version_checker():
    print("Python version: ", sys.version)
    print("Python version info: ", sys.version_info)


# 3. Current DateTime Display
def current_datetime_display():
    print("Current date and time: ", datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))


# 4. Circle Area Calculator
def circle_area_calculator():
    r = float(input("Radius: "))
    print("Area: ", math.pi * r * r)


# 5. Reverse Full Name
def reverse_full_name():
    first_name = input("First name: ")
    last_name = input("Last name: ")
    print("Full name: ", last_name + " " + first_name)


# 6. List and Tuple Generator
def list_and_tuple_generator():
    values = input("Input some comma-separated numbers: ")
    list1 = values.split(",")
    tuple1 = tuple(list1)
    print("Tuple: ", tuple1)
    print("List: ", list1)


# 7.  File Extension Extractor
def file_extension_extractor():
    extension = input("File extension: ")
    print(repr(extension.split(".")[-1]))
    print((extension.split(".")[-1]))


# 8. First and Last Colors
def first_and_last_colors():
    color_list = ["Red", "Green", "White", "Black"]
    print("First color: ", color_list[0])
    print("Last color: ", color_list[-1])
    print("%s %s" % (color_list[0], color_list[-1]))


# 9. Exam Schedule Formatter
def exam_schedule_formatter():
    exam_st_date = (20, 12, 2024)
    print("%s/%s/%s" % exam_st_date)


# 10. Number Expansion Calculator
def number_expansion_calculator():
    a = int(input("Enter a number: "))
    n1 = int("%s" % a)
    n2 = int("%s%s" % (a, a))
    n3 = int("%s%s%s" % (a, a, a))
    print(n1 + n2 + n3)


# 11. Function Documentation Printer
def function_documentation_printer():
    print(datetime.__doc__)


# 12. Monthly Calendar Display
def monthly_calendar_display():
    month = int(input("Month: "))
    year = int(input("Year: "))
    print(calendar.month(year, month))


# 13. Multi-line Here Document
def multi_line_here_document():
    print("""
        a string that you "dont't" have to escape
        This
        is a......multi-line
        heredoc string ----------> example
     """)


# 14. Days Between Dates
def days_between_dates():
    day1 = datetime.datetime(2024, 12, 20)
    day2 = datetime.datetime(2025, 1, 29)
    print((day2 - day1).days, "days")


# 15. Sphere Volume Calculator
def sphere_volume_calculator():
    r = float(input("Radius: "))
    v = 4 / 3 * r ** 3 * math.pi
    print("Volume of the sphere: ", v)


# 16. Difference from 17
def difference_from_17():
    x = int(input("x: "))
    minus = x - 17
    if minus < 0:
        print(abs(minus))
    else:
        print(minus * 2)


# 17. Number Range Tester
def number_range_tester():
    x = int(input("x: "))
    print((abs(1000 - x) <= 100) or (abs(2000 - x) <= 100))


# 18. Triple Sum Calculator
def triple_sum_calculator():
    x = int(input("x: "))
    y = int(input("y: "))
    z = int(input("z: "))
    if x == y == z:
        print((x + y + z) * 3)
    else:
        print(x + y + z)


# 19. Prefix "Is" String Modifier
def prefix_is_string_modifier():
    text = str(input("Text: "))
    if text.startswith("Is") and len(text) > 2:
        print(text)
    else:
        print("Is", text)


# 20. String Copy Generator
def string_copy_generator():
    text = str(input("Text: "))
    x = int(input("x: "))
    print(text * x)


# 21. Even or Odd Checker
def even_or_odd_checker():
    x = int(input("x: "))
    if x % 2 == 0:
        print("Even")
    else:
        print("Odd")


# 22. Count 4 in a list
def count_4_in_list():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(numbers.count(4))


# 23. String Prefix Copies
def string_prefix_copies():
    text = str(input("Text: "))
    n = int(input("n: "))
    if len(text) > 2:
        print(text[:2] * n)
    else:
        print(text * n)


# 24. Vowel Tester
def vowel_tester():
    all_vowel = 'aeiou'
    input_vowel = str(input("Vowel characters: "))
    print(input_vowel in all_vowel)


# 25. Value in Group Tester
def value_in_group_tester():
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    x = input("x: ")
    print(x in array)


# 26. List Histogram
def list_histogram():
    array = [2, 4, 3, 2]
    for i in array:
        print("*" * i)


# 27. List to String Concatenator
def list_to_string_concatenator():
    # array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # text = ''
    # for i in array:
    #     text += str(i)
    # print(text)

    array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    text = ''.join(map(str, array))
    print(text)


# 28. Even Numbers Until 237
def even_numbers_until_237():
    numbers = [
        386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
        399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
        815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
        958, 743, 527
    ]
    for i in numbers:
        if i == 237:
            print(i)
            break
        elif i % 2 == 0:
            print(i)


# 29. Unique Colors Finder
def unique_colors_finder():
    color_list_1 = {"White", "Black", "Red"}
    color_list_2 = {"Red", "Green"}
    colors_finder = color_list_1.difference(color_list_2)
    print(colors_finder)


# 30. Triangle Area Calculator
def triangle_area_calculator():
    b = float(input("b: "))
    h = float(input("h: "))
    area = 1 / 2 * b * h
    print(area)


# 31. GCD Calculator
def gcd_calculator():
    x = int(input("x: "))
    y = int(input("y: "))
    print(math.gcd(x, y))


# 32. LCM Calculator
def lcm_calculator():
    x = int(input("x: "))
    y = int(input("y: "))
    print(math.lcm(x, y))


# 33. Triple Sum with Equality Rule
def triple_sum_with_equality_rule():
    x = int(input("x: "))
    y = int(input("y: "))
    z = int(input("z: "))
    if x == y or x == z or y == z:
        print(0)
    else:
        print(x + y + z)


# 34. Conditional Sum to 20
def conditional_sum_to_20():
    x = int(input("x: "))
    y = int(input("y: "))
    result = x + y
    if result in range(15, 20):
        print(20)
    else:
        print(x + y)


# 35. Equality or 5 Rule Checker
def equality_or_5_rule_checker():
    x = int(input("x: "))
    y = int(input("y: "))
    if x == y or abs(x - y) == 5 or abs(x + y) == 5:
        print(True)
    else:
        print(False)


# 36. Add Integers Validator
def add_integers_validator(x, y):
    if not (isinstance(x, int) and isinstance(y, int)):
        return print("Please enter two integers.")
    return print(x + y)


# 37. Personal Info Formatter
def personal_info_formatter():
    name = str(input("Name: "))
    age = int(input("Age: "))
    address = str(input("Address: "))
    print("Name: {}\nAge: {}\nAddress: {}".format(name, age, address))


# 38. Expression Solver
def expression_solver():
    x = int(input("x: "))
    y = int(input("y: "))
    result = (x + y) * (x + y)
    print("(({} + {}) ^ 2) = {}".format(x, y, result))


# 39. Future Value Calculator
def future_value_calculator():
    amount = float(input("Amount: "))
    rate_of_interest = float(input("Rate of interest: "))
    years = int(input("Years: "))
    print(round(amount * ((1 + (0.01 * rate_of_interest)) ** years), 3))


# 40. Distance Between Points
def distance_between_points():
    p1 = [4, 0]
    p2 = [6, 6]
    distance = math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
    print(distance)


# 41. File Existence Checker
def file_existence_checker():
    print(os.path.isfile("part1.py"))


# 42. Shell Mode Detector
def shell_mode_detector():
    print(struct.calcsize("P") * 8, "bit")


# 43. OS and Platform Info
def os_and_platform_info():
    print("Name of the operating system: ", os.name)
    print("Name of the OS platform: ", platform.system())
    print("Version of the operating system: ", platform.release())


# 44. Python Site Packages Locator
def python_site_packages_locator():
    print(site.getsitepackages())


# 45. External Command Runner
def external_command_runner():
    subprocess.check_call(["cmd", "/c", "dir"])


# 46. File Path and Name Finder
def file_path_and_name_finder():
    print(os.path.realpath("part1.py"))


# 47. CPU Count Finder
def cpu_count_finder():
    print(multiprocessing.cpu_count())


# 48. String to Numeric Parser
def string_to_numeric_parser():
    x = input("x: ")
    print(x.isnumeric())
    print(float(x))
    print(int(float(x)))


# 49. Directory Files Lister
def directory_files_lister():
    files_list = [file for file in os.listdir("C:/Users/nguyn/Documents/Zalo Received Files") if
                  os.path.isfile(os.path.join("C:/Users/nguyn/Documents/Zalo Received Files", file))]
    print(files_list)


# 50. Print Without Newline
def print_without_newlines():
    for i in range(0, 10):
        print("*", end="")


# 51. Program Profiler
def program_profiler():
    cProfile.run("print(2 + 3)")


# 52. Print to STDERR
def print_to_stderr():
    sys.stderr.write("Standard Error")


# 53. Access Environment Variables
def access_environment_variable():
    print(os.environ)
    print(os.environ['PATH'])


# 54. Get Current Username
def get_current_username():
    subprocess.call(["whoami"])
    print(getpass.getuser())


# 55. Find Local IPs
def find_local_ips():
    local_hostname = socket.gethostname()
    ip_addresses = socket.gethostbyname_ex(local_hostname)[2]
    filtered_ips = [ip for ip in ip_addresses if not ip.startswith("127.")]
    first_ip = filtered_ips[0]
    print(first_ip)


# 56. Console Dimensions
def console_dimensions():
    if platform.system() == "Windows":
        try:
            size = os.get_terminal_size()
            print(size.lines, size.columns, 0, 0)
        except OSError:
            print("Unable to get console dimensions on Windows")


# 57. Method Execution Time
def method_execution_time():
    start = time.time()
    s = 0
    for i in range(0, 100):
        s += i
    end = time.time()
    print(s, "Time: ", end - start)


# 58. Sum of First n Positives
def sum_of_first_n_positives():
    x = int(input("x: "))
    result = 0
    # for i in range(0, x + 1):
    #     result += i
    result = (x * (x + 1) / 2)
    print(int(result))


# 59. Height to Centimeters
def height_to_centimeters():
    height_feet = int(input("Feet: "))
    height_inch = int(input("Inch: "))
    height_inch += height_feet * 12
    height_meters = round(height_inch * 2.54, 2)
    print("Your height is: %d cm" % height_meters)


# 60. Triangle Hypotenuse Calculator
def triangle_hypotenuse_calculator():
    a = float(input("a: "))
    b = float(input("b: "))
    c = math.sqrt(a ** 2 + b ** 2)
    print("The length of the hypotenuse is: %s" % round(c, 2))


# 61. Feet to Other Units
def feet_to_other_units():
    feet = float(input("Feet: "))
    feet_to_inch = feet * 12
    feet_to_yard = feet * (1 / 3)
    feet_to_mile = feet / 5280
    print("Feet to inch: {}\nFeet to yard: {}\nFeet to mile: {}".format(feet_to_inch, feet_to_yard, feet_to_mile))


# 62. Time to Seconds Converter
def time_to_seconds_converter():
    day = int(input("Day: "))
    hour = int(input("Hour: "))
    minute = int(input("Minute: "))
    second = int(input("Second: "))
    second = day * 24 * 60 * 60 + hour * 60 * 60 + minute * 60 + second
    print("Seconds: %s" % int(second))


# 63. Absolute File Path Finder
def absolute_file_path_finder(file_name):
    print(os.path.abspath(file_name))


# 64. File Timestamps
def file_timestamps(path_file_name):
    print("Last modified: ", time.ctime(os.path.getmtime(path_file_name)))
    print("Created: ", time.ctime(os.path.getctime(path_file_name)))


# 65. Seconds to DHMS Converter
def seconds_to_dhms_converter():
    second = int(input("Second: "))
    day = second // (24 * 60 * 60)
    second = second % (24 * 60 * 60)
    hour = second // (60 * 60)
    second = second % (60 * 60)
    minute = second // 60
    second = second % 60
    second = second
    print("%sd:%sh:%sm:%ss" % (day, hour, minute, second))


# 66. BMI Calculator
def bmi_calculator():
    kg = float(input("kg: "))
    cm = float(input("cm: ")) / 100
    bmi = kg / cm ** 2
    print(bmi)


# 67. Pressure Unit Converter
def pressure_unit_converter():
    kpa = float(input("Input pressure in kilopascals: "))
    psi = kpa / 6.89475729
    mmhg = kpa * 760 / 101.325
    atm = kpa / 101.325
    print("The pressure in pounds per square inch: %.2f psi" % psi)
    print("The pressure in millimeters of mercury: %.2f mmHg" % mmhg)
    print("Atmosphere pressure: %.2f atm." % atm)


# 68. Sum of Digits
def sum_of_digits():
    x = input("x: ")
    summary = 0
    for i in x:
        summary += int(i)
    print(summary)


# 69. Sort Three Numbers
def sort_three_numbers():
    x = int(input("x: "))
    y = int(input("y: "))
    z = int(input("z: "))
    a = min(x, y, z)
    c = max(x, y, z)
    b = (x + y + z) - a - c
    print(a, b, c)


# 70. Sort Files by Date
def sort_files_by_dates():
    files = glob.glob("*.py")
    files.sort(key=os.path.getmtime)
    print("\n".join(files))


# 71. Directory Listing by Creation Date
def directory_listing_by_creation_date():
    dir_path = sys.argv[1] if len(sys.argv) == 2 else r"."
    data = (os.path.join(dir_path, fn) for fn in os.listdir(dir_path))
    data = ((os.stat(path), path) for path in data)
    data = ((stat[ST_CTIME], path) for stat, path in data if S_ISREG(stat[ST_MODE]))
    for cdate, path in sorted(data):
        print(time.ctime(cdate), os.path.basename(path))


# 72. Math Module Details
def math_module_details():
    print(dir(math))


# 73. Line Midpoint Calculator
def line_midpoint_calculator():
    x1 = float(input("x1: "))
    y1 = float(input("y1: "))

    x2 = float(input("x2: "))
    y2 = float(input("y2: "))

    x = (x1 + x2) / 2
    y = (y1 + y2) / 2

    print("({}, {})".format(x, y))


# 74. Word Hasher
def word_hasher():
    print("Updating...")


# 75. Copyright Information
def copyright_information():
    print(sys.copyright)


# 76. Command-line Arguments
def command_line_arguments():
    print("This is the name/path of the script:"), sys.argv[0]
    print("Number of arguments:", len(sys.argv))
    print("Argument List:", str(sys.argv))


# 77. Endianness Checker
def endianness_checker():
    print(sys.byteorder)
    if sys.byteorder == "little":
        print("Little-endian")
    else:
        print("Big-endian")


# 78. List Built-in Modules
def list_built_in_modules():
    module_name = ','.join(sorted(sys.builtin_module_names))
    print(textwrap.fill(module_name, width=100))


# 80. Current Recursion Limit
def current_recursion_limit():
    print(sys.getrecursionlimit())


# 81. Concatenate Strings
def concatenate_strings():
    strings = ['Nguyen', 'Duc', 'Huy']
    print("Full name:", ' '.join(strings))


# 82. Sum of Container Items
def sum_of_container_items():
    print(sum([2, 3, 4]))
    print(sum((2, 3, 4)))
    print(sum({2, 3, 4}))
    # dictionary


# 83. List Greater-Than Test
def list_greater_than_test():
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    n = int(input("n: "))
    print(all(x > n for x in numbers))


# 84. Character Frequency Counter
def character_frequency_counter():
    text = input("Text: ")
    char = input("Character: ")
    # count = 0
    # for i in text:
    #     if i == char:
    #         count += 1
    #
    # print(count)
    print('Count:', text.count(char))


# 85. File or Directory Checker
def file_or_directory_checker():
    print(os.path.isfile("test.py"))
    print(os.path.isdir("test.py"))


# 86. Character ASCII Value
def character_ascii_value():
    char = input("Character: ")
    print(ord(char))


# 87. File Size Finder
def file_size_finder():
    print(os.path.getsize("part1.py"), 'bytes')
    print(os.stat("part1.py").st_size, 'bytes')
    print(open('part1.py').seek(0, os.SEEK_END), 'bytes')


# 88. Sum Expression Printer
def sum_expression_printer():
    a = int(input("a: "))
    b = int(input("b: "))
    print('{} + {} = {}'.format(a, b, a + b))


# 89. Conditional Action
def conditional_action():
    x = int(input('x: '))
    if x == 1:
        print('First day a month!')
    else:
        print('Nothing')


# 90. Self-replicating Program
def self_replication_program():
    print('Updating...')


# 91. Swap Variables
def swap_variables():
    a = int(input('a: '))
    b = int(input('b: '))
    print('a = {}, b = {}'.format(a, b))
    c = a
    a = b
    b = c
    print('a = {}, b = {}'.format(a, b))


# 92. Special Characters in String
def special_characters_in_string():
    # Print a raw string using triple-quotes with special characters.
    print(r"""\#{'}${"}@/""")

    # Print a raw string using triple-quotes with special characters.
    print(r'''\#{'}${"}@/''')


# 93. Object Identity and Type
def object_identity_and_type():
    x = input('x: ')
    print('Identity:', x)
    print('Type:', type(x))
    print('Value:', id(x))


# 94. String Bytes to Integers
def string_bytes_to_integers():
    strings = str(input('Strings: '))
    x = b'2'
    print(list(x))
    print(list(ord(i) for i in strings))


# 95. Check if a string is numeric
def check_if_string_is_numeric():
    text = input('Text: ')
    try:
        i = float(text)
        print('Numeric')
    except (ValueError, TypeError):
        print('Not numeric')


# 96. Print Call Stack
def print_call_stack():
    traceback.print_stack()


# 97. List Special Variables
def list_special_variables():
    s_var_names = sorted((set(globals().keys()) | set(__builtins__.__dict__.keys())) - set('_ names i'.split()))
    print('\n'.join(' '.join(s_var_names[i:i + 8]) for i in range(0, len(s_var_names), 8)))


# 98. Get System Time
def get_system_time():
    print(time.ctime())


# 99. Clear Terminal
def clear_terminal():
    os.system('dir')
    time.sleep(2)
    os.system('cls')


# 100. Get Host Name
def get_host_name():
    print(platform.node())
    print(platform.uname()[1])


# 101. URL Content Printer
def url_content_printer():
    conn = http.client.HTTPSConnection('www.google.com')
    conn.request('GET', '/')
    response = conn.getresponse()
    content = response.read()
    print(content)


# 102. System Command Output
def system_command_output():
    returned_text = subprocess.check_output('dir', shell=True, universal_newlines=True)
    print(returned_text)


# 103. Extract Filename
def extract_filename():
    print(os.path.basename('test.py'))


# 104. Process Group and User IDs
def process_group_and_user_ids():
    print(os.getpid())


# 105. User Environment Retriever
def user_environment_retriever():
    print(os.environ)


# 106. Path Extension Splitter
def path_extension_splitter():
    for os.path in ['test.txt', 'filename', '/user/system/test.txt', '/', '']:
        print('%s :' % os.path, os.path.splitlines(os.path))


# 107. File Properties Retriever
def file_properties_retriever():
    print('File         :', __file__)
    print('Access time  :', time.ctime(os.path.getatime(__file__)))
    print('Modified time:', time.ctime(os.path.getmtime(__file__)))
    print('Change time  :', time.ctime(os.path.getctime(__file__)))
    print('Size         :', os.path.getsize(__file__))


# 108. File or Directory Path Finder
def file_or_directory_path_finder():
    for file in [__file__, os.path.dirname(__file__), '/']:
        print('File        :', file)
        print('Absolute    :', os.path.isabs(file))
        print('Is File?    :', os.path.isfile(file))
        print('Is Dir?     :', os.path.isdir(file))
        print('Is Link?    :', os.path.islink(file))
        print('Exists?     :', os.path.exists(file))
        print('Link Exists?:', os.path.lexists(file))


# 109. Resolve Path Name
def resolve_path_name():
    print('Updating...')


# 110. Divisible by 15 Finder
def divisible_by_15_finder():
    num_list = [45, 55, 60, 37, 100, 105, 220]
    result = list(filter(lambda x: (x % 15 == 0), num_list))
    print(result)


# 111. Wildcard File Lister
def wildcard_file_lister():
    print(glob.glob('*.*'))
    print(glob.glob('*.py'))
    print(glob.glob('test.*'))


# 112. Remove First List Item
def remove_first_list_item():
    color = ["Red", "Black", "Green", "White", "Orange"]
    print(color)
    del color[0]
    print(color)


# 113. Number Input Validator
def number_input_validator():
    while True:
        try:
            number = int(input('Number: '))
            break
        except ValueError:
            print('Invalid number!')


# 114. Filter Positive Numbers
def filter_positive_numbers():
    num_list = [1, 2, -3, 4, 5, -6, 7, 8, 9]
    result = list(filter(lambda x: x >= 1, num_list))
    print(result)


# 115. List Product Calculator
def list_product_calculator():
    nums = [10, 20, 30]
    print(functools.reduce(lambda x, y: x * y, nums))


# 116. Print Unicode Characters
def print_unicode_characters():
    str = u'\u0050\u0079\u0074\u0068\u006f\u006e \u0045\u0078\u0065\u0072\u0063\u0069\u0073\u0065\u0073 \u002d \u0077\u0033\u0072\u0065\u0073\u006f\u0075\u0072\u0063\u0065'
    print(str)


# 117. String Memory Location Test
def string_memory_location_test():
    str1 = "Python"
    str2 = "Python"
    print("\nMemory location of str1 =", hex(id(str1)))
    print("Memory location of str2 =", hex(id(str2)))


# 118. Create Bytearray from List
def create_bytearray_from_list():
    nums = [10, 20, 56, 35, 17, 99]
    values = bytearray(nums)
    for x in values:
        print(x, end=' ')


# 119. Round Float to Decimals
def round_float_to_decimals():
    x = 1.23456789
    n = int(input('n: '))
    print(round(x, n))


# 120. String Formatter with Length Limit
def string_formatter_with_length_limit():
    str_num = "1234567890"
    print('%.2s' % str_num)
    print('%.3s' % str_num)
    print('%.9s' % str_num)


# 121. Variable Defined Checker
def variable_defined_checker():
    try:
        x
    except NameError:
        print("Variable is not defined....!")
    else:
        print("Variable is defined.")


# 122. Empty Variable Without Deletion
def empty_variable_without_deletion():
    n = 20
    d = {"x": 200}
    l = [1, 3, 5]
    t = (5, 7, 8)
    print(type(n)())
    print(type(d)())
    print(type(l)())
    print(type(t)())


# 123. Max and Min of Number Types
def max_and_min_of_number_types():
    print(sys.float_info)
    print(sys.float_info.max)
    print(sys.maxsize)


# 124. Variable Equality Checker
def variable_equality_checker():
    x = int(input('x: '))
    y = int(input('y: '))
    z = int(input('z: '))
    if x == y == z:
        print(x + y + z)
    else:
        print('Not equal')


# 125. Sum Collection Counts
def sum_collection_counts():
    num = [2, 2, 4, 6, 6, 8, 6, 10, 4]
    result = sum(collections.Counter(num).values())
    print(result)


# 126. Get Module Object
def get_module_object():
    print(inspect.getmodule(math.sqrt))


# 127. Integer Fits in 64 Bits
def integer_fits_in_64_bits():
    int_val = 6
    if int_val < 64:
        print((2 ** 63).bit_length())
        print((-2 ** 63).bit_length())


# 128. Lowercase Letters Checker
def lowercase_letters_checker():
    str1 = 'A8238i823acdeOUEI'
    print(any(c.islower() for c in str1))


# 129. Add Leading Zeroes
def add_leading_zeroes():
    str1 = 'abcd'
    print(str1.ljust(10, '0'))
    print(str1.rjust(10, '0'))


# 130. Double Quotes String Display
def double_quotes_string_display():
    data = {'Alex': 1, 'Suresh': 2, 'Agnessa': 3}
    print(json.dumps(data))


# 131. Split Variable Length String
def split_variable_length_string():
    var_list = ['a', 'b', 'c', 'd', 'e']
    v, w, x, y, z = var_list
    print(v, w, x, y, z)


# 132. List Home Directory
def list_home_directory():
    print(os.path.expanduser('~'))


# 133. Program Runtime Calculator
def program_runtime_calculator():
    start = timeit.default_timer()
    print(start)
    n = int(input('n: '))
    for i in range(0, n):
        print(i)
        time.sleep(1)

    print(timeit.default_timer() - start)


# 134. Input Two Integers
def input_two_integers():
    a, b = [int(x) for x in input().split()]
    print(a, b)


# 135. Print Variable Without Spaces
def print_variable_without_spaces():
    x = int(input('x: '))
    print('"{}"'.format(x))
    print('\"%s\"' % x)


# 136. Files Only in Directory
def files_only_in_directory():
    print([f for f in os.listdir('.') if os.path.isfile(os.path.join('.', f))], '\n')

    user_path = 'C:/Users/nguyn'
    for fname in os.listdir(user_path):
        path = os.path.join(user_path, fname)
        if os.path.isdir(path):
            continue
        print(fname)


# 137. Extract Dictionary Pair
def extract_dictionary_pair():
    item = {'Red': 'Green'}
    (item1, item2), = item.items()
    print(item1)
    print(item2)


# 138. Boolean to Integer Converter
def boolean_to_integer_converter():
    x = 'true'
    print(int(x == 'true'))
    print(int(x == 'false'))


# 140. Binary with Leading Zeroes
def binary_with_leading_zeroes():
    x = 12
    print(bin(x).replace('0b', ''))
    print(format(x, '08b'))
    print(format(x, '010b'))


# 141. Decimal to Hexadecimal
def decimal_to_hexadecimal():
    x = 55
    print(hex(x).replace('0x', ''))


# 142. Consecutive Zero-One Checker
def consecutive_zero_one_checker():
    x = '00110011'
    while '01' in x:
        x = x.replace('01', '')

    print(len(x) == 0)


# 143. Shell Bit Mode Detector
def shell_bit_mode_detector():
    print(struct.calcsize('P') * 8)


# 145. Check List, Tuple, or Set
def check_list_tuple_or_set():
    x = ['tuple', False, 3.2, 1]

    if type(x) is list:
        print('x is a list')
    elif type(x) is set:
        print('x is a set')
    elif type(x) is tuple:
        print('x is a tuple')
    else:
        print('Neither a list nor a set nor a tuple.')

    if isinstance(x, tuple):
        print('The variable x is a tuple')
    elif isinstance(x, list):
        print('The variable x is a list')
    elif isinstance(x, set):
        print('The variable x is a set')
    else:
        return 'Neither a list or a set or a tuple.'


# 146. Locate Python Module Sources
def locate_python_module_sources():
    print(importlib.util.find_spec('math'))


# 147. Divisibility Tester
def divisibility_tester():
    x = int(input('x: '))
    y = int(input('y: '))
    print(True if x % y == 0 else False)


# 148. Max and Min Without Built-ins
def max_and_min_without_built_ins():
    nums = [0, 10, 15, 40, -5, 42, 17, 28, 75]
    max_nums = nums[0]
    min_nums = nums[0]
    for x in nums:
        if x > max_nums:
            max_nums = x
        elif x < min_nums:
            min_nums = x
    print(max_nums, min_nums)


# 149. Cube Sum of Smaller Integers
def cube_sum_of_smaller_integers():
    x = int(input('x: '))
    x -= 1
    total = 0
    while x > 0:
        total += x ** 3
        x -= 1

    print(total)


# 150. Odd Product Pair Checker
def odd_product_pair_checker(list):
    for i in range(len(list)):
        for j in range(len(list)):
            if i != j:
                product = list[i] * list[j]
                if product & 1:
                    return True

    return False
