# folder named index.html
file { '/var/www/html/index.html':
    ensure  => 'present',
    mode    => '0744',
    owner   => 'www-data',
    group   => 'www-data',
    content => 'I love Puppet',
    notify  => Service['apache2'],
}

service { 'apache2':
    ensure => running
}
