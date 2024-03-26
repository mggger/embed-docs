import os
import re
from langchain_community.document_loaders import UnstructuredMarkdownLoader
from langchain_text_splitters import CharacterTextSplitter
from concurrent.futures import ThreadPoolExecutor, as_completed
import requests
import logging
import sys
import glob

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def parse_markdown(markdown_paths):
    data = []
    for markdown_path in markdown_paths:
        logging.info(f'parse markdown {markdown_path}')
        loader = UnstructuredMarkdownLoader(markdown_path)
        splitter = CharacterTextSplitter(separator="\n\n", chunk_size=680, chunk_overlap=50, length_function=len,
                                         is_separator_regex=False)
        pages = loader.load_and_split(splitter)

        for page in pages:
            page_content = page.page_content.replace("\n", ' ')
            page_data = {"description": page_content, "text": page_content, "type": "markdown"}
            data.append(page_data)
    return data


def submit_batch(batch, url, batch_number, token):
    logging.info(f'Starting submission of batch {batch_number}')

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
    }
    max_retries = 2
    retries = 0

    while retries < max_retries:
        try:
            response = requests.post(url, json=batch, headers=headers)
            response.raise_for_status()  # 如果响应状态码不是200，则抛出异常
            logging.info(f'Successfully submitted batch {batch_number}')

            break  # 成功提交后退出循环
        except requests.exceptions.HTTPError as e:
            retries += 1
            logging.error(f'Failed to submit batch {batch_number}, attempt {retries}. Error: {e}')
            if retries == max_retries:
                logging.error(f'Failed to submit batch {batch_number} after {max_retries} attempts.')
                raise  # 在最后一次重试失败后抛出异常

def get_all_file_paths(directory):
    # Construct the pattern to match all files within the directory
    pattern = os.path.join(directory, '*')
    # Use glob.glob to get all file paths
    file_paths = glob.glob(pattern)
    # Filter out directories, leaving only files
    file_paths = [path for path in file_paths if os.path.isfile(path)]
    # Join the file paths into a single string separated by commas
    return  file_paths

if __name__ == '__main__':
    if len(sys.argv) < 2:
        logging.error("Usage: python script.py <markdown_paths>")
        sys.exit(1)

    markdown_paths_input = sys.argv[1]  # Get markdown paths from command line arguments
    markdown_paths = markdown_paths_input.split(',')
    data = parse_markdown(markdown_paths)
    batch_size = 50
    submission_url = 'https://api.gptdevelopment.online/api/embeddings/train/text'  # 更改为你的提交端点URL

    token = os.environ.get("USER_TOKEN")

    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = []
        for i in range(0, len(data), batch_size):
            batch = data[i:i + batch_size]
            batch_number = i // batch_size + 1
            futures.append(executor.submit(submit_batch, batch, submission_url, batch_number, token))

        for future in as_completed(futures):
            try:
                future.result()  # 如果有异常，这里会抛出
            except requests.exceptions.RequestException as e:
                logging.error(f'Failed to submit a batch: {e}')