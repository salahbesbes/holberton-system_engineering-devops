# kill some program
exec { 'pkill killmenow':
  path => '/usr/bin',
}
