# encoding: utf-8

def  read_filed_config(file_path_name, file_path_connection):
    with open(file_path_name, 'r', encoding='utf8') as name, open(file_path_connection, 'r', encoding='utf8') as connection:
        filed_name = [line.strip() for line in name.readlines()]
        filed_connection = {line.strip().split('\t')[0]:line.strip().split('\t')[1] for line in connection}
        print(filed_name)
        print(filed_connection)
        



if __name__ == '__main__':
    file_path_name = 'test_data/filed_name.txt'
    file_path_connection = 'test_data/filed_connection.txt'
    read_filed_config(file_path_name, file_path_connection)