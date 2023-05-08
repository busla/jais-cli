# import json
# import requests


# def _get_token():
#     try:
#         return os.environ["JA_SEARCH_API_KEY"]
#     except KeyError as err:
#         logger.error("JA_SEARCH_API_KEY is missing, leaving now...")
#         raise


# def _get_url(post_code):
#     return f"https://api.ja.is/search/v6/?q={post_code}&scope=businesses"


# def _get_meta(url):
#     token = _get_token()
#     return Request(url, headers={"Accept": "application/json", "Authorization": token})


# def _search(post_code, start=1, count=1):
#     token = _get_token()
#     url = f"{_get_url(post_code)}&start={start}&count={count}"
#     return Request(url, headers={"Accept": "application/json", "Authorization": token})


# def _meta(post_code):
#     url = _get_url(post_code)
#     with urlopen(_get_meta(url)) as response:
#         body = response.read()
#     parsed = json.loads(body)
#     return parsed["meta"]
#     # print(json.dumps(parsed["meta"], indent=2))


# _meta(104)
