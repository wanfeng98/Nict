import random


def show():
    banner = [r"""
    __      _    _____     ____   ________  
   /  \    / )  (_   _)   / ___) (___  ___) 
  / /\ \  / /     | |    / /         ) )    
  ) ) ) ) ) )     | |   ( (         ( (     
 ( ( ( ( ( (      | |   ( (          ) )    
 / /  \ \/ /     _| |__  \ \___     ( (     
(_/    \__/     /_____(   \____)    /__\    
    """, r"""
     .-') _                  .-') _    
    ( OO ) )                (  OO) )   
,--./ ,--,' ,-.-')   .-----./     '._  
|   \ |  |\ |  |OO) '  .--./|'--...__) 
|    \|  | )|  |  \ |  |('-.'--.  .--' 
|  .     |/ |  |(_//_) |OO  )  |  |    
|  |\    | ,|  |_.'||  |`-'|   |  |    
|  | \   |(_|  |  (_'  '--'\   |  |    
`--'  `--'  `--'     `-----'   `--'    
    """, r"""
,---.   .--..-./`)     _______ ,---------.  
|    \  |  |\ .-.')   /   __  \\          \ 
|  ,  \ |  |/ `-' \  | ,_/  \__)`--.  ,---' 
|  |\_ \|  | `-'`"`,-./  )         |   \    
|  _( )_\  | .---. \  '_ '`)       :_ _:    
| (_ o _)  | |   |  > (_)  )  __   (_I_)    
|  (_,_)\  | |   | (  .  .-'_/  ) (_(=)_)   
|  |    |  | |   |  `-'`-'     /   (_I_)    
'--'    '--' '---'    `._____.'    '---'                                         
    """, r"""
 _____  ___    __     ______  ___________  
(\"   \|"  \  |" \   /" _  "\("     _   ") 
|.\\   \    | ||  | (: ( \___))__/  \\__/  
|: \.   \\  | |:  |  \/ \        \\_ /     
|.  \    \. | |.  |  //  \ _     |.  |     
|    \    \ | /\  |\(:   _) \    \:  |     
 \___|\____\)(__\_|_)\_______)    \__|                                           
    """, """
 ____  _____  _____   ______  _________  
|_   \|_   _||_   _|.' ___  ||  _   _  | 
  |   \ | |    | | / .'   \_||_/ | | \_| 
  | |\ \| |    | | | |           | |     
 _| |_\   |_  _| |_\ `.___.'\   _| |_    
|_____|\____||_____|`.____ .'  |_____|                                         
    """]
    print(banner[random.randint(0, len(banner)-1)])
    print('\t[Author:CJero | Version:1.0]\n')