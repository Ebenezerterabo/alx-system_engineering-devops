# Kill a process with the exec puppet resource

exec { 'kill process':
    command => 'pkill -f killmenow',
    path    => ['/usr/bin/', '/usr/sbin'],
}