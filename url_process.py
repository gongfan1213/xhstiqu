import urllib.parse

def double_url_encode(text):
    # 进行第一次URL编码
    encoded_text = urllib.parse.quote(text)
    # 进行第二次URL编码
    encoded_text = urllib.parse.quote(encoded_text)
    return encoded_text

def generate_urls(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    with open(output_file, 'w', encoding='utf-8') as f:
        for line in lines:
            # 去除行尾的换行符
            line = line.strip()
            # 直接写入原始URL
            f.write(line + '\n')