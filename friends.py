import urllib
import json
 
def save_image(friend):
  size = '/picture?width=200&height=200'
  url = 'https://graph.facebook.com/'+ friend['id'] + size
  image = urllib.urlopen(url).read()
  f = open('fotos/'+ friend['name'] + '.jpg', 'wb')
  f.write(image)
  f.close()
  print (friend['name'] + '.jpg descargado')
#get the token https://developers.facebook.com/tools/explorer
url = 'https://graph.facebook.com/me/friends?access_token=CAACEdEose0cBAHZCQsCZCyKhcPBpVrU8MXZCZB6zKOukvRCSJqoIyvb6xG78vM0b23oHeltrJHL7P0FBIE8Kc5hKu6oVa1JMzVc8nRTYCC7MJvN03hYzMaPaTmcD8LDZBgBjYdW7XLFx8ZBq1b9oYhMG4UiZA5v3e8iOm2TUTZCl9o5tyKC31bvjKL7eFhdBZCyZBChOm1G3yfQr0QnwZCElWuEMo4tErKVvC8ZD'
resp = urllib.urlopen(url).read()
data = json.loads(resp.decode('utf-8'))
 
for friend in data['data']:
  save_image(friend)