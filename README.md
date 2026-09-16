Inspired by https://github.com/richardbmh/hadashboard


## Helpers

refering to the vars/room_vars.yml file, this assumes that you need to create a Home Assistant Group Helper:
* Settings -> Devices & services -> Helpers -> Create Helper -> Group
* create a group for switches, lights, mediaplayers named the plug_type
 * as an example for all the office switches the group name would be office_switches
* create the group even if there is only a single entity, there is logic in the dashboard that checks the status of these groups and highlights the icon if any device in the group is on

## Components

- [Lovelace Mini Graph Card](https://github.com/kalkih/mini-graph-card)
- [Bubble Card](https://github.com/Clooos/Bubble-Card)
- [Yet Another Media Player](https://github.com/jianyu-li/yet-another-media-player)
- [Navbar Card](https://github.com/joseluis9595/lovelace-navbar-card)
- [Calendar Card Pro](https://github.com/alexpfau/calendar-card-pro)
- [Mushroom](https://github.com/piitaya/lovelace-mushroom)
- [button-card](https://github.com/custom-cards/button-card)
- [card-mod](https://github.com/thomasloven/lovelace-card-mod)
- [layout-card](https://github.com/thomasloven/lovelace-layout-card)
- [Vacuum Card](https://github.com/denysdovhan/vacuum-card)
- [Vertical Stack In Card](https://github.com/ofekashery/vertical-stack-in-card)
- [Custom Brand Icons](https://github.com/elax46/custom-brand-icons)
- [Kiosk Mode](https://github.com/NemesisRE/kiosk-mode)
- [Stack In Card](https://github.com/custom-cards/stack-in-card?tab=readme-ov-file)

---