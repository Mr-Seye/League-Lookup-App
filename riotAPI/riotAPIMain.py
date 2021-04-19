from riotAPI import RiotAPI
import json
#import tkinter

#home = tkinter.Tk()
#home.configure(background='#343F3E')

#home.title('EPQ API Application')
#home.mainloop()
looping = True
key = open("Key.txt" , "r")
api = RiotAPI(key.read())
print('Welcome to my League of Legends stat checker application')
name = input("Enter your summoner name: ")
def main(summonerName, summonerId, accountId, summonerLevel, api):
    r=api.get_summoner_by_name(name)

    summonerName=r['name']
    summonerId=r['id']
    accountId=r['accountId']
    summonerLevel=r['summonerLevel']
    #print(r)

r=api.get_summoner_by_name(name)
summonerName=r['name']
summonerId=r['id']
accountId=r['accountId']
summonerLevel=r['summonerLevel']



print('What would you like to do? ', '\n Summoner Profile', '\n Champion Information') #'\n Apex Queues', '\n Spectate Information')
selection = input()
selection.capitalize()    




if selection == 'Summoner Profile':
    t=api.get_total_champion_mastery(r['id'])
    rank=api.get_league_entries_summoner(r['id'])
    def summonerProf(summonerName, summonerId, accountId, summonerLevel, r, t, rank, looping):
        print('Summoner Information \n')
        print('Summoner Name: ', summonerName, '\n', 'Level: ', summonerLevel, '\n', 'Total Mastery: ', t)

        #if rank[0]['queueType'] != '' is True:
         #   print('This user has no ranked games.')

        if rank[0]['queueType'] == 'RANKED_SOLO_5x5': 
            #An index error here means that the user has no ranked games
            print('\n Queue Type: Ranked Solo/Duo')
            print('\n', rank[0]['tier'], rank[0]['rank'], 'LP:', rank[0]['leaguePoints'], '\n Games Played:', rank[0]['wins']+rank[0]['losses'], '\n Wins:', rank[0]['wins'], '\n Losses:', rank[0]['losses'])
            winpercent= round((rank[0]['wins']/(rank[0]['wins']+rank[0]['losses'])*100),2)
            print('Win Percentage=', winpercent,'%')

            
elif selection == 'Champion Information':
   champname = input('What champion would you like information about? ')
   def championInformation(champname, looping):
    with open('D:\\Documents\\EPQ Application\\riotAPI\\Data Dragon\\9.24.2\\data\\en_GB\\championFull.json', encoding='utf8') as f:
        result = json.load(f)
        champname = champname.capitalize()
        if champname == result['data'][champname]['name']:
            print(result['data'][champname]['id'], result['data'][champname]['title'],'\n', '\n Resource Type:', 
            result['data'][champname]['partype'],'\n', '\n Blurb:', result['data'][champname]['blurb'],
             '\n','\n Role: ', result['data'][champname]['tags'],'\n', '\n Abilites:\n','\n', 'Passive:', result['data'][champname]['passive']['name'], '\n', result['data'][champname]['passive']['description'],
             '\n', '\n','Q:', 
             result['data'][champname]['spells'][0]['name'], '\n',
             result['data'][champname]['spells'][0]['description'], '\n',
             'Cooldown: ', result['data'][champname]['spells'][0]['cooldownBurn'], '\n',
             'Cost: ', result['data'][champname]['spells'][0]['costBurn'], '('+result['data'][champname]['spells'][0]['costType']+')', '\n',
             '\n','W:', 
             result['data'][champname]['spells'][1]['name'], '\n',
             result['data'][champname]['spells'][1]['description'], '\n',
             'Cooldown:', result['data'][champname]['spells'][1]['cooldownBurn'], '\n',
             'Cost:', result['data'][champname]['spells'][1]['costBurn'], '('+result['data'][champname]['spells'][1]['costType']+')'
             '\n',
             '\n','E:', 
             result['data'][champname]['spells'][2]['name'], '\n',
             result['data'][champname]['spells'][2]['description'], '\n',
             'Cooldown:', result['data'][champname]['spells'][2]['cooldownBurn'], '\n',
             'Cost:', result['data'][champname]['spells'][2]['costBurn'], '('+result['data'][champname]['spells'][2]['costType']+')',
             '\n','\n','R:', 
             result['data'][champname]['spells'][3]['name'], '\n',
             result['data'][champname]['spells'][3]['description'], '\n',
             'Cooldown:', result['data'][champname]['spells'][3]['cooldownBurn'], '\n',
             'Cost:', result['data'][champname]['spells'][3]['costBurn'], '('+result['data'][champname]['spells'][3]['costType']+')')

    #print('Your summoner name is, ',  summonerName, ' your summonerID is, ',  summonerId, ' and your accountID is, ',  account`Id, '.')

    #return r

    
    #print(r)
    
if __name__ =="__main__":
    main(summonerName, summonerId, accountId, summonerLevel, api)
    if selection == 'Summoner Profile':
        summonerProf(summonerName, summonerId, accountId, summonerLevel, r, t, rank, looping)
    elif selection == 'Champion Information':
        championInformation(champname, looping)

