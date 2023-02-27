import requests
import riotAPIConsts as Consts

#   Import of downloaded module 'requests' and my custom module
#   riotAPIConstants

#   RiotAPI class

class RiotAPI(object):


    def __init__(self, api_key, region=Consts.REGIONS['europe_west']):
        self.api_key = api_key
        self.region = region


    def _request(self, api_url, params={}):
            args = {'api_key': self.api_key}
            for key, value in params.items():
                if key not in args:
                    args[key]=value

            response = requests.get(
                Consts.URL['base'].format(
                    proxy=self.region,
                    region=self.region,
                    url=api_url
                    ),
                params=args
                )
            #  print(response.url) - DEBUGGING
            #  print(response.json) - DEBUGGING

            return response.json()

    def get_summoner_by_name(self, name):
        api_url = Consts.URL['summoner_by_name'].format(
             version=Consts.API_VERSIONS['summoner'],
             names=name
             )
        return self._request(api_url)

    def get_total_champion_mastery(self, summonerId):
        api_url = Consts.URL['total_champion_mastery'].format(
            version=Consts.API_VERSIONS['champion-mastery'],
            summonerId=summonerId
        )
        return self._request(api_url)

    def get_league_entries_summoner(self, summonerId):
        api_url = Consts.URL['match_entries'].format(
            version=Consts.API_VERSIONS['league'],
            summonerId=summonerId
        )
        return self._request(api_url)


#  VISUALS

#  class ddragon(object):
    #  def __init__(self, patch=Consts.DDRAGON_PATCH['current_patch'], language=Consts.DDRAGON_LANGUAGE['english_uk']):
        #  self.patch = patch
        #  self.language = language

    #  def _ddragon(self, ddragon_url, patch, language):
        #  ddresponse = requests.get(
          #  Consts.URL['ddragon'].format(
           #     patch=self.patch,
            #    language=self.language,
             #   url=ddragon_url
          #  )
#        )
 #       print(ddresponse.json)
  #      return ddresponse.json()
     #       #print(response.url)
   #         #print(response.json)
        
    #  def get_champion_info(self, ddragon_url):
      #  ddragon_url = Consts.URL['champion_info'].format(
       #     patch=Consts.DDRAGON_PATCH['current_patch'],
        #    language=Consts.DDRAGON_LANGUAGE['english_uk']
      #  )
        #  return self._ddragon

    #  def new(self, name):
        #  api_url = Consts.URL['summoner_by_name'].format(
             #  version=Consts.API_VERSIONS['summoner'],
             #  names=name
             #  )
