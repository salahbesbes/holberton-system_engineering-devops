exec { 'update':
  command => 'apt-get apdate -y',
  path    => '/bin/:/usr/bin';
}->
package { 'nginx':
  ensure   => installed,
  provider => apt;
}->
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
->
file_line {'redirect':
  ensure => present,
  after  => 'listen \[::\]:80',
  path   => '/etc/nginx/sites-available/default',
  line   => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=dQw4w9WgXcQ permanent;'
}


