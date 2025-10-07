# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  # Use Ubuntu 22.04
  config.vm.box = "ubuntu/jammy64"

  config.vm.network "forwarded_port", guest: 8000, host: 8000

  config.vm.provision "shell", inline: <<-SHELL
    # Disable automatic apt updates
    systemctl disable apt-daily.service
    systemctl disable apt-daily.timer

    # Update and install packages
    sudo apt-get update
    sudo apt-get install -y python3.10 python3.10-venv python3.10-dev zip

    # Make python3.10 the default python3
    sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.10 2
    sudo update-alternatives --config python3 <<< '1'

    # Setup bash alias
    touch /home/vagrant/.bash_aliases
    if ! grep -q PYTHON_ALIAS_ADDED /home/vagrant/.bash_aliases; then
      echo "# PYTHON_ALIAS_ADDED" >> /home/vagrant/.bash_aliases
      echo "alias python='python3.10'" >> /home/vagrant/.bash_aliases
    fi
  SHELL
end
