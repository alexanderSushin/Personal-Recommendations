from anime_api import getInfoById
from anime import Anime
import time
from db import insertAnime

normal_list = '1535,11757,11771,10719,14813,28121,431,2001,13759,15809,18897,26055,918,934,2966,6045,6547,14741,7054,8074,10620,11665,1887,10087,11111,11617,19815,11061,28999,31043,4898,13601,20787,22319,245,263,269,270,18679,23283,24833,226,18153,23273,32995,199,23755,9919,22199,28851,31933,33950,121,4224,16498,22135,26243,28805,6746,7785,20583,30276,1575,5680,10793,28223,20,21,30,9253,9756,20507,32281,1,26145,22535,31240,5081,6114,457,3588,28171,12355,164,170'
j = 1

for id in normal_list.split(','):
	cur = getInfoById(int(id))
	anime = Anime()
	anime.id = j
	j += 1
	anime.shikimory_id = cur["id"]
	anime.name = cur["name"]
	anime.russian = cur["russian"]
	anime.url = cur["url"]
	anime.status = cur["status"]
	anime.score = int(float(cur["score"]))
	anime.episodes = cur["episodes"]
	anime.year = "2000"
	anime.rating = str(anime.score)
	anime.description = cur["description"]
	anime.image_url = cur["image"]["original"]
	anime.genres = []
	insertAnime(anime)
	print(anime.id, 'ok')
	time.sleep(0.5)