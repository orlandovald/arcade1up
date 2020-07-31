## Arcade1up scripts

Want to use the original Power and Volume buttons of your modded Arcade1Up machine? These scripts will help you do it. In addition, you can configure a power relay to turn on/off everything from the cabinet switch.

Please follow the wiring instructions in the below videos:

- Power and Volume switches: video coming soon
- Power relay: video coming soon

You will need to connect to your Pi from a terminal (Putty on Windows) and run the below command:

```bash
bash <(curl -s https://raw.githubusercontent.com/orlandovald/arcade1up/master/setup.sh)
```

This is what the script will do,

1. Install all required dependencies (python libraries and Git)
2. Clone this repo to get the python, bash and other scripts
3. It will prompt if you want to configure the Power switch, press 'Y' or 'y' to configure. Skip with any other key.
4. It will prompt if you want to configure the Volume switch, press 'Y' or 'y' to configure. Skip with any other key.
5. It will prompt if you want to configure the Power relay, press 'Y' or 'y' to configure. Skip with any other key.

You skipped one by mistake? No worries, you can re-run the command. The script will automatically skip anything that has been already configured.

## Pin configuration
After installation you should make any neccesary updates to the default configuration which can be found in the `/home/pi/arcade1up/config/config.ini` file.

You can see the default values here [config/config.ini](config/config.ini)