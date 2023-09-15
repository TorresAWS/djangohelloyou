VAGRANTFILE_API_VERSION = "2"
Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.ssh.insert_key = false

  config.vm.define :gserver do |vagrant|
    vagrant.vm.box = "ubuntu/trusty64"
    vagrant.vm.hostname = "gserver"
    vagrant.vm.network "forwarded_port", host: 8000, guest: 8000
#    vagrant.vm.network "private_network", ip: "192.168.99.30"
  end

    config.vm.provision :ansible do |ansible|
        ansible.raw_arguments = Shellwords.shellsplit(ENV["ANSIBLE_ARGS"]) if ENV["ANSIBLE_ARGS"]
       # ansible.verbose = "-vvv"
        ansible.inventory_path = "provisioning/hosts"
        ansible.playbook = "provisioning/playbook.yml"
    end



end
