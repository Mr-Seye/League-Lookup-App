URL = {
    'base': 'https://{proxy}.api.riotgames.com/lol/{url}',
    'total_mastery_points_by_champion': 'champion-mastery/v{version}/champion-masteries/by-summoner/{summonerId}',
    'champion_mastery': 'champion-mastery/v{version}/champion-masteries/by-summoner/{summonerId}/by-champion/{championId}',
    'total_champion_mastery': 'champion-mastery/v{version}/scores/by-summoner/{summonerId}',
    'champion_rotations': 'platform/v{version}/champion-rotations',
    'apex_queues': 'league-exp/v{version}/entries/{queue}/{tier}/{division}',
    'challenger_league': 'league/v{version}/challengerleagues/by-leagues/{queue}',
    'grand_master_league': 'league/v{version}/grandmasterleagues/by-leagues/{queue}',
    'master_league': 'league/v{version}/masterleagues/by-leagues/{queue}',
    'match_entries': 'league/v{version}/entries/by-summoner/{summonerId}',
    'league_status': 'status/v{version}/shard-data',
    'match': 'match/v{version}/matches/{matchId}',
    'account_match_list': 'match/v{version}/matchlists/by-account/{accountId}',
    'match_timeline': 'match/v{version}/timelines/by-match/{matchId}',
    'spectate_match_info': 'spectator/v{version}/active-games/by-summoner/{summonerId}',
    'summoner_by_name': 'summoner/v{version}/summoners/by-name/{names}',
    'third_party_code': 'platform/v{version}/third-party-code/by-summoner/{summonerId}',
    'ddragon': 'https://ddragon.leagueoflegends.com/cd/{patch}/data/{language}/',
    'champion_info': 'champion.json'
}
#  This is the base URL for any API address on the Riot API, it uses HTTP
#  Secure, followed by a proxy in this case "EUW1", then the api link,
#  then /lol which specifies that it is referring to League of Legends
#  then {url} which is derived from riotAPI

#  Essentially a module which referres to summoner information based on
#  summoner name

API_VERSIONS = { 
    'champion-mastery': '4',
    'champion': '3',
    'league-exp': '4',
    'league': '4',
    'lol-status': '3',
    'match': '4',
    'spectator': '4',
    'summoner': '4',
    'third-party-code': '4'
    
}

#  Current patch for data dragon

DDRAGON_PATCH = {
    'current_patch': '9.24.2'
}

#  Desired data dragon language

DDRAGON_LANGUAGE = {
    'english_uk': 'en_GB'
}

#  This is a list of the appropriate module versions

REGIONS = { 
    'brazil': 'br1',
    'europe_nordic_east': 'eun1',
    'europe_west': 'euw1',
    'japan': 'jp1',
    'korea': 'kr',
    'latin_america_north': 'la1',
    'latin_america_south': 'la2',
    'north_america': 'na1',
    'oceana': 'oc1',
    'turkey': 'tr1',
    'russia': 'ru1'

}

#  The codes for the modules being used
#  This is not required as of now

PROXIES = { 
    'europe_west': 'euw1',
    'north_america': 'na1'
}
