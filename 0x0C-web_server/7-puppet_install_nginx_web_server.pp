# automatic install and config nginx
exec { 'update':
  command => 'apt-get update',
  path    => '/usr/bin/:/bin/'
}->
package { 'nginx':
  ensure   => present, # must be present not any else
  provider => apt
}->
file { '/etc/nginx/sites-enabled/default':
  ensure => link,
  target => '/etc/nginx/sites-available/default',
}->
file { '/var/www/html/index.html':
  ensure  => file,
  mode    => '0644',
  content => 'Holberton School',
}->
file_line {'add_redirection':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => "location /redirect_me {\n\t\treturn 301 https://www.youtube.com/watch?v=dQw4w9WgXcQ;\n\t\t}",
  notify => Service['nginx']
}
service { 'nginx':
  ensure     => running,
}


