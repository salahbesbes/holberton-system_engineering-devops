# to validate the file use puppet parser validate filename
# use pupet-lint ..

$content = "# Added Nginx limits \nnginx       soft    nofile  30000 \nnginx       hard    nofile  50000 \n"
# exec { 'module':
#   command => 'puppet module install puppetlabs-stdlib --version 4.9.1',
#   path    => '/usr/bin/:/bin/'
# } ->

file_line { 'replace':
  ensure   => present,
  path     => '/etc/default/nginx',
  multiple => false,
  replace  => true,
  line     => 'ULIMIT="-n 4096"',
  match    => '^ULIMIT'
} ->

exec {'append to file':
  command => "echo ${content} >> /etc/security/limits.conf",
  path    => '/usr/bin/:/bin/'
  } ->

file_line { 'rate per time':
  ensure => present,
  after  => 'pid /run/nginx.pid;',
  path   => '/etc/nginx/nginx.conf',
  line   => 'worker_rlimit_nofile 30000;',
  notify => Service['nginx']
} ->

service { 'nginx':
    ensure => running
}
