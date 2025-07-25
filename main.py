import pandas as pd
import file_name


def df_to_string(df):
    result = ''

    for index, row in df.iterrows():
        result += f'{row['content']}. {row['comment']} {row['created_at']}\n\n'

    return result


def read_data_from_csv(current_file):

    df =  pd.read_csv(current_file, sep=',')
    df = df[['content', 'comment', 'created_at']]
    df['content'] = df['content'].apply(add_quotes)
    df['comment'] = df['comment'].apply(remove_quotes)
    df['created_at'] = df['created_at'].apply(string_to_date)

    return df


def add_quotes(item):
    return '«' + item + '»'


def remove_quotes(item):
    return item.replace('"', '').rstrip('\n')


def string_to_date(item):
    item = list(item.split())
    final_string_date = '.'.join(list(item[0].split('-'))[::-1])
    final_string_date += ', ' + item[1]
    return '(' + final_string_date + ')'


def main():
    current_file = file_name.CSV_FILE_NAME
    df = read_data_from_csv(current_file)
    result = df_to_string(df)
    with open('result_quotes.md', 'w') as file:
        file.write(result)


if __name__ == '__main__':
    main()