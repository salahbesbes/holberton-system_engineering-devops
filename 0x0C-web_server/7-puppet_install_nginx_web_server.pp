# automatic install and config nginx
exec { 'update':
  command => 'sudo apt-get update',
  path    => '/usr/bin/:/usr/local/bin/:/bin/';
} ->
package { 'nginx':
  ensure   => present,
  provider => apt;
} ->
file { '/etc/nginx/sites-enabled/default':
  ensure => link,
  path   => '/etc/nginx/sites-available/default';
}->
file { '/usr/www/html/index.html':
  ensure  => file,
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0644',
  content => 'Holberton School';
}


