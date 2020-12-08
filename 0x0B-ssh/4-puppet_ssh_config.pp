# Make changes to configuration file
file_line { '/etc/ssh/ssh_config':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => '    PasswordAuthentication no',
}
file_line { '/etc/ssh/ssh_config':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => '    IdentityFile ~/.ssh/holberton',
}