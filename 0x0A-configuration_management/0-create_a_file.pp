# Using Puppet, create a file in /tmp

file {'school':
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',
  path    => '/tmp/school',
}
