from fake_useragent import UserAgent

headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
    "Connection": "keep-alive",
    "content-type": "application/json",
    "Host": "api.detmir.ru",
    'If-None-Match': 'W/"197923-DeM36OUQBCU1P50vvYCA6SplnIA"',
    "Origin": "https://www.detmir.ru",
    "Referer": "https://www.detmir.ru/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "TE": "trailers",
    "User-Agent": str(UserAgent().random),
    "x-requested-with": "detmir-ui",
}
proxy = {
    'http': 'http://130.41.65.206:8080'
}
