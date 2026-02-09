# A Home Assistant Integration to monitor and control NBE pelletburners using the  UDP protocol

This integration should be able to connect to a scotte/RTB V7/V13 controllers (and apparently also aduro pellet hybrid stoves). The software 
is based on the NBE Test program https://github.com/motoz/nbetest by https://github.com/motoz plus work from https://github.com/svanggaard/NBEConnect and https://github.com/Brille783/NBEConnectfyr

## Purpose

To reduce pellet consumption. The easiest way to reduce pellet consumption is to turn the pelletboiler off. The RTB App/Stokercloud makes it 
possible to set up weekly operating schedules for the boiler and for DHW. However it is only possible to define timeslots with a granularity 
of 2 hours. It is only possible to start and stop the boiler in equal hours (e.g. 04:00 or 06:00). The controller does not allow you to run the boiler for e.g. 3 hours. 

This can be adressed by adding an external switch/relay or by letting the Home Assistant communicate with the boiler directly. 

## Prerequsites

You'll need the boiler serial and the boiler password (should be printet on a boiler label). You're using the same seriel/password when setting up your App, or logging in to StokerCloud.

Optionally you can choose to enter the boiler IP address. Either you need to set a fixed IP address in the boiler controller or you'll eed to make the address static with the help of your router. 

You can also choose to leave the IP-field empty. In that case, this integration will autodiscover the boiler. 

## Installation via HACS

If you use **HACS (Home Assistant Community Store)**, installing this integration is straightforward:

1. **Install HACS** if you haven’t already:  
   Follow the instructions here: [https://hacs.xyz/docs/installation/prerequisites](https://hacs.xyz/docs/installation/prerequisites)

2. **Add the repository to HACS**:
   - Open **Home Assistant → HACS → Integrations → +**  
   - Select **“Custom repository”** at the bottom.  
   - Enter the GitHub repository URL for this integration:  

     ```
     https://github.com/MichaelOE/homeassistant-NBEConnect
     ```

   - Choose **Integration** as the type.  
   - Click **Add**.

3. **Install the integration**:
   - After adding the repository, it will appear in HACS under **Integrations → Explore & Add Repositories → Installed**.  
   - Click **Install**.

4. **Restart Home Assistant**:
   - Go to **Settings → System → Restart** to load the new integration.

5. **Add the integration in Home Assistant**:
   - Go to **Settings → Devices & Services → Add Integration**.  
   - Search for **NBEConnect**.  

6. **Configuration**:
   - Enter your boiler’s **serial number** and **password** (found on the boiler label).  
   - Optionally, enter the **boiler IP address** or leave blank for autodiscovery.

> 💡 **Tips:**  
> - Using HACS ensures the integration can be **easily updated** when new releases are published.  
> - If you encounter issues, make sure your HA version matches the **`manifest.json`** requirements.
