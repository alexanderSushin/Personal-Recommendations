from anime_api import getReq

def getTopAllTime(cntInTop = 10):
    if cntInTop > 50:
        return []
    ans = []
    res = getReq(f'https://shikimori.one/api/animes?limit={cntInTop}&order=ranked&page=1')
    for i in res:
        ans.append(i["id"])
    return ans
