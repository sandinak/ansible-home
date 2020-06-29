#! /bin/sh

printf "Set GPIO"
printf "\n"

{% for relay in pirelay_relays %}
#relay pos1
echo 17 > /sys/class/gpio/export
sudo sh -c "echo '1' >> /sys/class/gpio/gpio17/active_low"
echo high > /sys/class/gpio/gpio17/direction

#relay pos2
echo 27 > /sys/class/gpio/export
sudo sh -c "echo '1' >> /sys/class/gpio/gpio27/active_low"
echo high > /sys/class/gpio/gpio27/direction
exit 0