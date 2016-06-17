#!/bin/sh

CLOUDLET_USER=$1

# Update libvirtd's qemu config so that it will run under the proper user when started as at system level.
echo 'Setting libvirtd user, group and file ownership for qemu.'
sudo sed -i -e "s:#user = \"root\":user = \"${CLOUDLET_USER}\":g" /etc/libvirt/qemu.conf
sudo sed -i -e "s:#group = \"root\":group = \"${CLOUDLET_USER}\":g" /etc/libvirt/qemu.conf
sudo sed -i -e "s:#dynamic_ownership = 1:dynamic_ownership = 0:g" /etc/libvirt/qemu.conf

# Restart libvirtd, if it was running, to ensure it uses these settings.
sudo stop libvirt-bin
sudo start libvirt-bin

# Add the user to the appropriate groups.
sudo adduser ${CLOUDLET_USER} kvm
sudo adduser ${CLOUDLET_USER} libvirtd
