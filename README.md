# NoDM

## To-Do
- [ ] Write better readme
- [ ] Multi-platform Support
- [x] [Termux Support](#termux)
- [x] Heroku Support
- [ ] Media support
- [ ] Save Self-Destruct media
- [ ] Better database management (without using any cloud database)

## ⚠️Caution
Your telegram account might get banned. I should not be held responsible for this. Just mail recover@telegram.org to unban your account. 

<details>
<summary>

## Before you start
</summary>

You will need these required variables.

`API_ID` - You will get this from [here](https://my.telegram.org)

`API_HASH` - You will get this from [here](https://my.telegram.org)

`SESSION` - By running `wget -O session.py https://bit.ly/3ydVZyV && python session.py`

Save everything in `.env` file as shown in [`sample.env`](https://github.com/buddhhu/NoDM/blob/main/sample.env)
</details>

## Installations 
<details>
<summary>

### Termux
</summary>

```bash
pkg update
pkg upgrade
pkg install python git
git clone https://github.com/buddhhu/NoDM
cd NoDM
pip install -r requirements.txt
python -m bot
```
</details>

### Deploy On Heroku
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

Made with turu lob 👻

Don't forget to give a 🌟
