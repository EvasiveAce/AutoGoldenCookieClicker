# Auto Golden Cookie Clicker
![Static Badge](https://img.shields.io/badge/Python-4584b6?style=flat-square&logo=python&logoColor=FFFFFF)

![gifForGithub](https://github.com/user-attachments/assets/7e1a3904-48f3-4c2e-982b-db0d0de09b4e)

This program is for the idle-based browser game "Cookie Clicker" by Orteil, created to automatically click golden cookies. I developed this app so I could get the [golden cookie achievements](https://cookieclicker.fandom.com/wiki/Golden_Cookie_Achievements) easier, and without a third party plugin. 

## How It Works
I developed this app to work by using the Python module ```pyautogui```. It works by using the screen's resolution to take a temporary screenshot, and using that screenshot to find the correct colors by using a for-loop scan method; I used ```GetSystemMetrics``` to find out the monitor's width and height to determine how large the screenshot needs to be. If the color is scanned, it will move the mouse cursor to that position, and click. 

## Getting Started
> Please know that it only detects contract golden cookies. The fix for this is to enable the [Business Day Season](https://cookieclicker.fandom.com/wiki/Business_Day_season), or replace the normal golden cookie image in ```D:..\SteamLibrary\steamapps\common\Cookie Clicker\resources\app\src\img```, with this image:
>
> ![goldCookie](https://github.com/user-attachments/assets/95405c2f-6ed7-445d-b1a5-cda597abcdfc)
>
> Make sure it has the filename ```goldCookie.png```.

### Running Locally
1.  Once you have contract golden cookies spawning, open the exe file by downloading it [here](https://github.com/EvasiveAce/AutoGoldenCookieClicker/releases/tag/1.0).
2.  Simply press Start, and then click on your main monitor to start the automatic clicking.

## Contributing
If you have a suggestion to make this project better, please feel free to fork the repository or create an issue. I will do my best to respond to any feedback as soon as possible.

### Any contributions are greatly appreciated.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/FeatureHere`)
3. Commit your Changes (`git commit -m 'Add some FeatureHere'`)
4. Push to the Branch (`git push origin feature/FeatureHere`)
5. Open a Pull Request 

#### Thanks for Reading!
