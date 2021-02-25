# Change limit
exec { 'user-limit':
  command => "sed -i 's/5/3000/g; s/4/3000/g' /etc/security/limits.conf",
  path    => [ '/bin/', '/sbin/', '/usr/bin', '/usr/sbin/' ]
}