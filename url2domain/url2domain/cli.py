import tldextract
from urllib.parse import urlparse
import argparse
import sys

extractor = tldextract.TLDExtract()

def parse_url(url: str) -> str:
    """
    从 URL 中提取一级域名
    定义：一级域名 = 域名 + 后缀
    例如：
    - 输入: "https://www.example.com/path?query=123"
    - 输出: "example.com"
    """
    parsed = urlparse(url)
    extracted = extractor(parsed.netloc)
    return f"{extracted.domain}.{extracted.suffix}"

def main():
    parser = argparse.ArgumentParser(description="提取 URL 的一级域名")
    parser.add_argument("url", help="输入的 URL")
    args = parser.parse_args()
    print(parse_url(args.url))

if __name__ == "__main__":
    main()