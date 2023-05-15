# discord-pacer-bot
Discord Pacer Test
  
Discord bot to track user's running progression.  

Ways of logging are through a screenshot mainly through a screenshot of the Strava app or through manually logging progression  

TODO: Commands to get stats, motivaltional replies, private dm reminders can opt in  
  
General Flow:  
1. Input data (manually or screenshot)  
2. Run image through tesseract ocr
3. Extract text (needs work)
4. Store in database
5. Respond to users  
  
#Requirements
pip install -r requirements.txt 

#Resources
https://discordpy.readthedocs.io/en/stable/

 
