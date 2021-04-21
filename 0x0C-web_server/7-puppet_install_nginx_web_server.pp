# automatic install and config nginx
exec { 'update':
  command => '/usr/bin/apt-get update',
}
->
package { 'nginx':
  ensure   => present,
  provider => apt;
} ->
file { '/etc/nginx/sites-enabled/default':
  ensure => link,
  target => '/etc/nginx/sites-available/default';
}->
file { '/usr/www/html/index.html':
  ensure  => file,
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0644',
  content => 'Holberton School';
}


