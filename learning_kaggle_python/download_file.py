import kagglehub as kh

def download_file_from_kaggle(dataset_name):
    try:

        path= kh.dataset_download(dataset_name)
        print(f'the file is downloaded to the path : {path}')

    except Exception as exc:
        print(f"Error: {exc}")


if __name__ == '__main__':
    download_file_from_kaggle(dataset_name='nelgiriyewithana/top-spotify-songs-2023')
