PLACEHOLDER = "user"

with open("/Users/karthik.kumarb/PycharmProjects/pythonProject/file-handling/input/name_list.txt") as name_file:
    words_list =name_file.readlines()

with open("/Users/karthik.kumarb/PycharmProjects/pythonProject/file-handling/input/format.txt",mode="r") as format_file:
    format_Read_content =format_file.read()
    for word in words_list:
        stripped_word =word.strip()
        new_Text =format_Read_content.replace(PLACEHOLDER,stripped_word)
        print(new_Text)
        with open(f"/Users/karthik.kumarb/PycharmProjects/pythonProject/file-handling/output/letter_for_{stripped_word}.txt",mode="w") as write_file:
            write_file.write(new_Text)