import requests
from tqdm import tqdm
#url = 'http://corsmal.eecs.qmul.ac.uk/data/CCM/train/ccm_train_view2_rgb.zip'
#file_name=url.split('/')[-1]
#with open(file_name, 'wb') as out_file:
  #content = requests.get(url, stream=True).content
  #out_file.write(content)

def download(url, filename):
    with open(filename, 'wb') as f:
        response = requests.get(url, stream=True)
        total = response.headers.get('content-length')
        if total is None:
            f.write(response.content)
        else:
            downloaded = 0
            total = int(total)
            for data in tqdm(response.iter_content(chunk_size=max(int(total/1000), 1024*1024)),total=total):
                downloaded += len(data)
                f.write(data)

def get_dataset(url):
    file_name=url.split('/')[-1]
    download(url,file_name)