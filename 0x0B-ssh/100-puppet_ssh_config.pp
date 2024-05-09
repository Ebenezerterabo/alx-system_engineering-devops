# Configuring a client file using puppet

exec { 'puppet config_file':
    path => ['/usr/bin', 'usr/sbin'],
    command => 'echo "Host server1\n \
       Hostname 54.162.46.100\n    IdentityFile ~/.ssh/school\n \
           PasswordAuthentication no\n" >> /etc/ssh/ssh_config'
}